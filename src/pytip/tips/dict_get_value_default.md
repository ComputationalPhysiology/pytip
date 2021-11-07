---
name: dict_get_value_default
keywords: python,dict
description: Get a default value from a dictionary if key does not exist
---
Get a default value from a dictionary if key does not exist

```python
settings = {"solver_type": lu, "tol": 1e-8}
...
max_iter = settings["max_iter"] # raises KeyError
max_iter = settings.get("max_iter") # returns None
max_iter = settings.get("max_iter", 100) # max_iter = 100 if not set
```
