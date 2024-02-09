sources = neurovista

.PHONY: test format lint unittest coverage pre-commit clean
test: format lint unittest

format:
	ruff format $(sources) tests

lint:
	ruff check $(sources) tests
	mypy $(sources) tests

unittest:
	pytest

pre-commit:
	pre-commit run --all-files

clean:
	rm -rf .mypy_cache .pytest_cache
	rm -rf *.egg-info
	rm -rf .tox dist site
	rm -rf coverage.xml .coverage
