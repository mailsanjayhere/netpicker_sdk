.PHONY: install test lint clean

install:
	pip install -e .[dev]

test:
	pytest tests

lint:
	flake8 netpicker_sdk

clean:
	rm -rf __pycache__ */__pycache__ *.pyc *.pyo *.egg-info dist build .pytest_cache