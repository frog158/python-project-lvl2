build:
	poetry build
install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl
uninstall:
	python3 -m pip uninstall dist/hexlet_code-0.1.0-py3-none-any.whl
run:
	poetry run gendiff
	