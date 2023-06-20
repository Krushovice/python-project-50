install: # Для первого git clone
	poetry install

build: #  Сборка пакета
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

.PHONY: install build publish package-install lint check test-coverage
