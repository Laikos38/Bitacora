# F strings

## Equals
Since Python 3.8 you can do:
```python
value = 123
print(f"Value is {value}")
print(f"{value=}")
print(f"{value % 2 = }")

# Out:
# Value is 123
# value=123
# value % 2 = 1
```

## Conversions
```python
value = "Im diamond! ❖"
print(f"{value!a}")  # This one prints ascii
print(f"{value!r}")  # This one calls __repr__ instead of __str__

# Out:
# Im diamond! \u2756
# Im diamond! ❖
```

## Formatting
```python
import datetime

class Example:
    def __format__(self, format) -> str:
        return "Example"[:int(format)]

num = 123.412341
format = ".3f"
date = datetime.datetime.utcnow()
print(f"{date:%d/%m/%y}")
print(f"{num:.2f}")
print(f"{num:{format}}")
print(f"{Example():3}")

# Out:
# 24/12/21
# 123.41
# 123.412
# Exa
```