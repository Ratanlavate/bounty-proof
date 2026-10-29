"""Parse compact duration strings such as ``1h30m`` into seconds."""
import re

_UNITS = {"h": 3600, "m": 60, "s": 1}
_GROUPS = re.compile(r"(\d+)([hms])")


def parse_duration(text):
    """Return the number of seconds described by a compact duration string.

    Supported form: one or more ``<integer><unit>`` groups, for example ``"1h30m"``,
    ``"90s"`` or ``"2m30s"``. Units are ``h`` (hours), ``m`` (minutes) and ``s``
    (seconds).
    """
    total = 0
    for value, unit in _GROUPS.findall(text):
        total += int(value) * _UNITS[unit]
    return total
