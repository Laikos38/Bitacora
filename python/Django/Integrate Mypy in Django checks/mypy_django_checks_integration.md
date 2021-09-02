# Integrate Mypy in Django checks

[Django checks documentation](https://docs.djangoproject.com/en/3.2/topics/checks/)

1. Install Mypy `pip install mypy`
2. Create a check file with the folowing code:

```python
import re
from typing import List

from django.core.checks import register
from mypy import api


@register()
def mypy(app_configs, **kwargs) -> List:
    print("Performing mypy checks...\n")
    results = api.run(["--config-file=./configs/mypy.ini", "-p", "ggwp"])
    print("""####### MYPY #######""")
    error_messages = results[0]
    if not error_messages:
        print("Check passed successfully!  :D")
        return []
    pattern = re.compile("^(.+\d+): (\w+): (.+)")
    success = re.compile("^Success")
    for message in error_messages.rstrip().split("\n"):
        if re.match(success, message):
            print("Check passed successfully!  :D\n\n")
            return []
        parsed = re.match(pattern, message)
        if not parsed:
            continue
        location = parsed.group(1)
        message = parsed.group(3)
        print(message, location)
    print("\n\n")
    return []

```

With this configuration, the check will never raise errors preventing the project to run, but it will prompt you the mypy warnings and errors.
