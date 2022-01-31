run-tests:
	python -m unittest discover tests

lint:
	black */**.py
	isort src
	flake8 */**.py