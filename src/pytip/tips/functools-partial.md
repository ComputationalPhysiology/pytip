---
name: functools.partial
keywords: python,functools
description: Create a new function with partial application of arguments
---

Create a new function with partial application of the given arguments and keywords

```python
def add(x, y):
    return x + y

import functools
add_one = functools.partial(add, 1)
add_one(2) # returns 3
```
