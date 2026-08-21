# User Configuration Manager

A small settings manager that adds, updates, deletes, and displays user
configuration values such as theme, language, and notifications.

Built as a certification lab for the freeCodeCamp *Scientific Computing with
Python* course.

## Functions

| Function | Parameters | Behaviour |
|---|---|---|
| `add_setting` | `settings`, `(key, value)` | Adds the pair unless the key already exists |
| `update_setting` | `settings`, `(key, value)` | Updates the value if the key exists |
| `delete_setting` | `settings`, `key` | Removes the key if present |
| `view_settings` | `settings` | Returns a formatted listing of all settings |

All keys and values are normalised to lowercase on write; keys are capitalised
for display.

## Example

```python
settings = {"theme": "dark", "language": "en"}

add_setting(settings, ("Volume", "High"))
# "Setting 'volume' added with value 'high' successfully!"

view_settings(settings)
# Current User Settings:
# Theme: dark
# Language: en
# Volume: high
```

## Run it

```bash
python config_manager.py
```

## Notes

The lab specification requires each function to both mutate the dictionary and
return a display message. In production code these would be separated — the
function would return a success or failure result, and the caller would decide
how to present it.

Possible extensions: JSON persistence, an `argparse` CLI, and a pytest suite
in place of the `__main__` print calls.
