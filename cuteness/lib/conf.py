import toml

from cuteness.lib.attrdict import AttrDict
from cuteness.lib.pathdict import PathDict
from cuteness.lib.utils import getParam
from cuteness.lib import paths


class ConfigError(Exception):
    pass


class ConfigField:
    def __init__(self, var, path, *, type=lambda v: v, **kwargs):
        self.var = var
        self.path = path
        self.hasdefault, self.default = getParam("default", kwargs)
        self._hasinitdefault, self._initdefault = getParam("initdefault", kwargs)
        self.type = type

    @property
    def hasinitdefault(self):
        return self._hasinitdefault or self.hasdefault

    @property
    def initdefault(self):
        if self._hasinitdefault:
            return self._initdefault
        if self.hasdefault:
            return self.default
        raise AttributeError("This field does not an intial default")

    def load(self, config, configDict):
        if self.hasdefault:
            config[self.var] = self.type(configDict[self.path])
        else:
            config[self.var] = self.type(configDict.get(self.path, self.default))


class Config(AttrDict):
    fields = [
        ConfigField("prefix", "cuteness.prefix", default="&"),
        ConfigField("authtoken", "discord.authtoken", initdefault="INSERT_BOT_TOKEN_HERE")
    ]

    def __init__(self):
        super().__init__()

    def load(self):
        try:
            configDict = PathDict(toml.load(paths.confpath))
        except FileNotFoundError as e:
            raise ConfigError(f"Configuration file not found: {e.filename}")

        try:
            for f in self.fields:
                f.load(self, configDict)
        except KeyError as e:
            raise ConfigError(f"Required configuration field not found: {e.path}")

    def init(self):
        if paths.confpath.exists():
            raise FileExistsError(f"Configuration file already exists: {paths.confpath}")
        paths.confpath.parent.mkdir(parents=True, exist_ok=True)

        configDict = PathDict()
        for f in self.fields:
            if f.hasinitdefault:
                configDict[f.path] = f.initdefault
        with open(paths.confpath, "w") as f:
            toml.dump(configDict.toDict(), f)


conf = Config()
