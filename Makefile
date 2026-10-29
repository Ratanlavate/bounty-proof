.PHONY: build test lint

# Python has no separate compile step in most projects; compiling the bytecode is the real,
# verifiable equivalent and it fails on a syntax error.
build:
	python -m compileall -q src tests

test:
	python -m unittest discover -s tests -v

lint:
	ruff check .
