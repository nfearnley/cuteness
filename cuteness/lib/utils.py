def getParam(name, kwargs):
    hasparam = name in kwargs
    param = kwargs.get(name)
    return hasparam, param


def find_one(iterable):
    try:
        return next(iterable)
    except StopIteration:
        return None
