"""Parse compact duration strings such as ``1h30m`` into seconds."""
import re

_UNITS = {"h": 3600, "m": 60, "s": 1}
_GROUPS = re.compile(r"(\d+)([hmsHMS])")


def parse_duration(text):
    """Return the number of seconds described by a compact duration string.

    Supported form: one or more ``<integer><unit>`` groups, for example ``"1h30m"``,
    ``"90s"`` or ``"2m30s"``. Units are ``h`` (hours), ``m`` (minutes) and ``s``
    (seconds).
    """
    if not isinstance(text, str):
        raise ValueError("invalid input")

    total = 0
    matches = _GROUPS.findall(text)
    if not matches:
        raise ValueError("invalid input")

    # Ensure the entire string is consumed by valid groups
    reconstructed = "".join(f"{value}{unit}" for value, unit in matches)
    if reconstructed.lower() != text.replace(" ", "").lower():
        raise ValueError("invalid input")

    for value, unit in matches:
        total += int(value) * _UNITS[unit.lower()]
    return total
