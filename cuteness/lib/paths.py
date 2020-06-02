from pathlib import Path

import appdirs

datadir = Path(appdirs.user_data_dir("cuteness", "nfearnley"))
confpath = datadir / "cuteness.conf"
