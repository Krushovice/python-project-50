install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	pip install --force-reinstall dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 hexlet_python_package

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

run diff:
	poetry run python3 -m gendif.scripts.gendiff file1.json file2.json
