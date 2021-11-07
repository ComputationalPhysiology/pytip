from collections import namedtuple
from pathlib import Path as _Path

from rich.markdown import Markdown

Text = namedtuple("Text", ["text", "metadata"])

_here = _Path(__file__).parent.absolute()

files = (_here.joinpath(p) for p in _here.iterdir() if p.suffix == ".md")
names = (p.stem for p in files)


def extract_metadata(src: str) -> Text:
    src_split = src.split("---")
    if len(src_split) < 3:
        # There is no metadata
        return Text(text=Markdown(src), metadata={})

    meta = "".join(src_split[:2]).strip("\n").split("\n")
    text = "".join(src_split[2:])
    metadata = {}
    for arg in meta:
        key, value = arg.split(":")
        metadata[key.strip()] = value.strip()
    return Text(text=Markdown(text), metadata=metadata)


def get_tips():
    data = {}
    for p in files:
        with open(p, "r") as f:
            data[p.stem] = extract_metadata(f.read())
    return data
