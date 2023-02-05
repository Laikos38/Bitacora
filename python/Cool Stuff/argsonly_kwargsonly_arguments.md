# Positional-only and keyword-only arguments in Python

## The basics
```python
def f(a, b, c):
    print(f"{a}, {b}, {c}")

# Calling the function normally
f(1, 2, 3)  # Arguments passed as args (positional arguments)
f(a=1, b=2, c=3)  # Arguments passed as kwargs (keyword arguments)
f(b=2, c=3, a=1)  # The order of the arguments doesn't matter when we use kwargs
f(1, c=3, b=2)  # We can mix args and kwargs, but always args goes first
```

## Forcing keyword arguments
```python
def f(a, b, *, kw_only):
    print(f"{a}, {b}, {kw_only}")

f(1, 2, kw_only=3)  # Ok
f(1, b=2, kw_only=3)  # Ok
f(1, 2, 3)  # Error
f(1, b=2, 3)  # Error
```

The difference in using `*args` like `def f(a, b, *args, kw_only):`, is that:
```python
def f_1(a, b, *args, kw_only):
    print(f"{a}, {b}, {kw_only}")

def f_2(a, b, *, kw_only):
    print(f"{a}, {b}, {kw_only}")

f_1(1, 2, 3, 4, kw_only=3)  # args=(3, 4)
f_2(1, 2, 3, 4, kw_only=3)  # Error
```

But why? One simple use case, is that if you want to make sure that the arguments are not mixed, for example:
```python
def log_order(*, item, quantity, price):
    print(f"{quantity} units of {item} at ${price}")

f_1(quantity=2, item="golden beans", price=0.12)
```

## Forcing positional arguments
```python
def f(a, b, /, c, d, *, e):  # f(pos_only, /, pos_or_kw, *, kw_only)
    print("...")
```
