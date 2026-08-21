"""Manage user settings such as theme, language, and notifications.

Note: each function both mutates the dictionary and returns a display string.
The lab spec requires this, but the two jobs would normally be separated.
"""


def add_setting(settings: dict, setting: tuple) -> str:
    """Add a new setting, unless the key is already taken."""
    key, value = setting
    key, value = key.lower(), value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: dict, setting: tuple) -> str:
    """Change the value of a setting that already exists."""
    key, value = setting
    key, value = key.lower(), value.lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings: dict, key: str) -> str:
    """Remove a setting by key."""
    key = key.lower()

    if key not in settings:
        return "Setting not found!"

    del settings[key]
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings: dict) -> str:
    """List every setting, one per line, with keys capitalised."""
    if not settings:
        return "No settings available."

    lines = [f"{key.capitalize()}: {value}" for key, value in settings.items()]
    return "Current User Settings:\n" + "\n".join(lines) + "\n"


test_settings = {"theme": "dark", "language": "en", "notifications": "enabled"}


if __name__ == "__main__":
    print(add_setting(test_settings, ("Volume", "High")))
    print(update_setting(test_settings, ("Volume", "Low")))
    print(delete_setting(test_settings, "Volume"))
    print(view_settings(test_settings))
