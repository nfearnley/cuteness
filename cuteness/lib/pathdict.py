def getListDictItem(data, key, *, create=False):
    try:
        key = int(key)
    except ValueError:
        pass
    try:
        return data[key]
    except (KeyError, IndexError):
        raise KeyError


class PathDict:
    def __init__(self, data={}):
        try:
            # Try to convert directly to dict
            self._values = dict(data)
        except ValueError:
            # If unable to covert directly to dict, try to convert an iterable to dict
            self._values = {i: v for i, v in enumerate(data)}

    def __getitem__(self, path):
        """value = PathDict[path]"""
        branch = self._values
        components = path.split(".")

        for c in components:
            try:
                branch = getListDictItem(branch, c)
            except KeyError:
                err = KeyError(f"Path not found: {path!r}")
                err.path = path
                raise err

        return branch

    def __setitem__(self, path, value):
        """PathDict[path] = value"""
        branch = self._values
        components = path.split(".")
        last = components.pop()

        for c in components:
            try:
                branch = getListDictItem(branch, c)
            except KeyError:
                branch[c] = dict()
                branch = getListDictItem(branch, c)
        branch[last] = value

    def get(self, path, default=None):
        """value = PathDict.get(path, default)"""
        try:
            return self[path]
        except KeyError:
            return default

    def toDict(self):
        return self._values
