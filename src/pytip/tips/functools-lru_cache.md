---
name: functools.lru_cache
keywords: python,functools
description: Cache results of Least-recently-used arguments
---

Cache results of Least-recently-used arguments

```python
import functools

def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return n
    return fib(n-1) + fib(n-2)

@functools.lru_cache(maxsize=128)
def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return n
    return fib(n-1) + fib(n-2)
```
Open IPython and time the execution
```
>>> %time fib1(40)
CPU times: user 31.1 s, sys: 117 ms, total: 31.3 s
Wall time: 31.4 s

>>> %time fib2(40)
CPU times: user 29.8 s, sys: 50.8 ms, total: 29.9 s
Wall time: 29.9 s
```
Now time it again
```
>>> %time fib1(40)
CPU times: user 31.1 s, sys: 90.8 ms, total: 31.2 s
Wall time: 31.3 s

>>> %time fib2(40)
CPU times: user 3 µs, sys: 0 ns, total: 3 µs
Wall time: 6.2 µs
```
