# bounty-proof

A deliberately small target used to prove the autonomous bounty pipeline end to end: a real
defect, a failing test that reproduces it, and CI that goes green only when the fix is right.

`parse_duration` in [`src/duration.py`](src/duration.py) does not handle uppercase units and
does not reject invalid input. The test suite in `tests/` reproduces both.

    python -m unittest discover -s tests -v
