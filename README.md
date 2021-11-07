# Pytip

cli for tips and tricks using [`typer`](https://typer.tiangolo.com) and [`rich`](https://rich.readthedocs.io/en/stable/).

## Install

Clone repo and execute
```
python -m pip install .
```
inside the root directory

## Development install

If you want to contribute to the project you should also install the development dependencies using the command

```
python -m pip install -e ".[dev]"
```
This will also install the package in editable mode.
You should also install the pre-commit hook using the command
```
pre-commit install
```
This will make sure that you don't commit code to the repo that doesn't follow the guidelines.



## Usage

To get a random tip do
```
python -m pytip
```

To list all available tips do
```
python -m pytip --list-tips
```

## Todo

- [ ] Make `CONTRIBUTING.md`
- [ ] Create tests
- [ ] Setup GitHub actions
- [ ] Setup pre-commit CI
- [ ] Create API documentation using Sphinx
- [ ] Host documentation on GitHub pages
- [ ] Publish on PyPi
- [ ] Publish on conda
- [ ] Publish on conda-forge
- [ ] Connect to slack and make setup cron-job so that is publishes weekly tips



## Ideas for tips

The focus is currently around the python standard library, but this can change in the future.

### Python

#### `itertools`
- [ ] `product`
- [ ] `chain`
- [ ] `cycle`
- [ ] `accumulate`
- [ ] `combinations`
- [ ] `zip_longest`
- [ ] `starmap`
- [ ] `groupby`
- [ ] `compress`
- [ ] `islice`
- [ ] `takewhile`
- [ ] `tee`

#### `functools`
- [ ] `singledispatch`
- [ ] `cached_property`
- [x] `lru_cache`
- [ ] `wrapped`
- [ ] `reduce`
- [x] `partial`
- [ ] `total_ordering`

#### `collections`
- [ ] `Counter`
- [ ] `defaultdict`
- [ ] `namedtuple`
- [ ] `ChainMap`

#### `difflib`
- [ ] Find best match of words

#### `filecmp`
- [ ] Check if two files are different

#### `pathlib`
- [ ] Find location of current file
- [ ] Create directory with parents and if exists already


#### `datetime`


#### `operator`

- [ ] `itemgetter`

#### General

- [ ] Merge dictionaries
- [ ] Sort with custom key
- [x] Get value in dictionary with missing keys
- [ ] Get value in nested dictionary with missing keys
- [ ] Create dictionary for zip
- [ ] Generator comprehension vs list comprehension
- [ ] `iter` - Get first value in a dictionary

#### Funny
- [ ] `import antigravity`
- [ ] `import this`
