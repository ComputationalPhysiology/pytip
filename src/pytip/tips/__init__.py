from pathlib import Path as _Path
from rich.markdown import Markdown

_here = _Path(__file__).parent.absolute()

files = (_here.joinpath(p) for p in _here.iterdir() if p.suffix == ".md")
names = (p.stem for p in files)


def get_tips():
    data = {}
    for p in files:
        with open(p, "r") as f:
            data[p.stem] = Markdown(f.read())
    return data
