class PathDict:
    def __init__(self, data={}):
        self._values = dict(data)

    def __getitem__(self, path):
        """value = PathDict[path]"""
        branch = self._values
        components = path.split(".")

        for c in components:
            try:
                branch = branch[c]
            except (KeyError):
                err = KeyError(f"Path not found: {self.path!r}")
                err.path = path
                raise KeyError

        return branch

    def __setitem__(self, path, value):
        """PathDict[path] = value"""
        branch = self._values
        components = path.split(".")
        last = components.pop()

        for c in components:
            if c not in branch:
                branch[c] = dict()
            branch = branch[c]
        branch[last] = value

    def get(self, path, default=None):
        """value = PathDict.get(path, default)"""
        try:
            return self[path]
        except (KeyError):
            return default

    def toDict(self):
        return self._values
