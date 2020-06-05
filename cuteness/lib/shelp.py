import pydoc
from pydoc import getdoc, inspect, visiblename, classname, deque, _split_list, classify_class_attrs, builtins, sort_attributes


class SummaryDoc(pydoc._PlainTextDoc):
    def docclass(self, object, name=None, mod=None, *ignored):
        """Produce text documentation for a given class object."""
        realname = object.__name__
        name = name or realname
        bases = object.__bases__

        def makename(c, m=object.__module__):
            return classname(c, m)

        if name == realname:
            title = 'class ' + self.bold(realname)
        else:
            title = self.bold(name) + ' = class ' + realname
        if bases:
            parents = map(makename, bases)
            title = title + '(%s)' % ', '.join(parents)

        contents = []
        push = contents.append

        try:
            signature = inspect.signature(object)
        except (ValueError, TypeError):
            signature = None
        if signature:
            argspec = str(signature)
            if argspec and argspec != '()':
                push(name + argspec)

        doc = getdoc(object)
        if doc:
            push(self.indent(doc.splitlines()[0]))

        # List the mro, if non-trivial.
        mro = deque(inspect.getmro(object))
        if len(mro) > 2:
            push("Method resolution order:")
            for base in mro:
                push('    ' + makename(base))

        # List the built-in subclasses, if any:
        subclasses = sorted(
            (str(cls.__name__) for cls in type.__subclasses__(object)
             if not cls.__name__.startswith("_") and cls.__module__ == "builtins"),
            key=str.lower
        )
        no_of_subclasses = len(subclasses)
        MAX_SUBCLASSES_TO_DISPLAY = 4
        if subclasses:
            push("Built-in subclasses:")
            for subclassname in subclasses[:MAX_SUBCLASSES_TO_DISPLAY]:
                push('    ' + subclassname)
            if no_of_subclasses > MAX_SUBCLASSES_TO_DISPLAY:
                push('    ... and ' + str(no_of_subclasses - MAX_SUBCLASSES_TO_DISPLAY) + ' other subclasses')
            push('')

        def header(msg):
            push(f"\n{msg}\n" + ("-" * len(msg)))

        def spill(msg, attrs, predicate):
            ok, attrs = _split_list(attrs, predicate)
            if ok:
                header(msg)
                for name, kind, homecls, value in ok:
                    try:
                        value = getattr(object, name)
                    except Exception:
                        # Some descriptors may meet a failure in their __get__.
                        # (bug #1785)
                        push(self.docdata(value, name, mod))
                    else:
                        push(self.document(value, name, mod, object))
            return attrs

        def spilldescriptors(msg, attrs, predicate):
            ok, attrs = _split_list(attrs, predicate)
            if ok:
                header(msg)
                for name, kind, homecls, value in ok:
                    push(self.docdata(value, name, mod))
            return attrs

        def spilldata(msg, attrs, predicate):
            ok, attrs = _split_list(attrs, predicate)
            if ok:
                header(msg)
                for name, kind, homecls, value in ok:
                    if callable(value) or inspect.isdatadescriptor(value):
                        doc = getdoc(value)
                    else:
                        doc = None
                    try:
                        obj = getattr(object, name)
                    except AttributeError:
                        obj = homecls.__dict__[name]
                    push(self.docother(obj, name, mod, maxlen=70, doc=doc))
            return attrs

        attrs = [(name, kind, cls, value)
                 for name, kind, cls, value in classify_class_attrs(object)
                 if visiblename(name, obj=object)]

        while attrs:
            if mro:
                thisclass = mro.popleft()
            else:
                thisclass = attrs[0][2]
            attrs, inherited = _split_list(attrs, lambda t: t[2] is thisclass)

            if object is not builtins.object and thisclass is builtins.object:
                attrs = inherited
                continue
            elif thisclass is object:
                tag = "defined here"
            else:
                tag = "inherited from %s" % classname(thisclass,
                                                      object.__module__)

            sort_attributes(attrs, object)

            # Pump out the attrs, segregated by kind.
            attrs = spill("Methods %s" % tag, attrs,
                          lambda t: t[1] == 'method')
            attrs = spill("Class methods %s" % tag, attrs,
                          lambda t: t[1] == 'class method')
            attrs = spill("Static methods %s" % tag, attrs,
                          lambda t: t[1] == 'static method')
            attrs = spilldescriptors("Readonly properties %s" % tag, attrs,
                                     lambda t: t[1] == 'readonly property')
            attrs = spilldescriptors("Data descriptors %s" % tag, attrs,
                                     lambda t: t[1] == 'data descriptor')
            attrs = spilldata("Data and other attributes %s" % tag, attrs,
                              lambda t: t[1] == 'data')

            assert attrs == []
            attrs = inherited

        contents = '\n'.join(contents)
        if not contents:
            return title + '\n'
        return title + '\n' + self.indent(contents.rstrip(), ' |  ') + '\n'

    def docroutine(self, *args, **kwargs):
        output = super().docroutine(*args, **kwargs)
        lines = [line for line in output.splitlines() if not line.endswith("|coro|") and line.strip() != ""]
        return "\n".join(lines[:2])

    def docdata(self, *args, **kwargs):
        output = super().docdata(*args, **kwargs)
        return "\n".join(output.splitlines()[:2])


# A cheaty way to get multiline output in the debug console
class HelpDoc():
    def __init__(self, contents):
        self.contents = contents

    def __str__(self):
        return self.contents

    def __repr__(self):
        return self.contents


def shelp(thing):
    return HelpDoc(pydoc.render_doc(thing, renderer=SummaryDoc()))
