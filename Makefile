run-tests:
	python -m unittest discover tests

lint:
	black src/**.py
	isort src
	flake8 src/**.py