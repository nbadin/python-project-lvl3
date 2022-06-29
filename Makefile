build:
	poetry build

package-install:
	pip install --user dist/*.whl

install:
	poetry install

test:
		poetry run pytest

lint:
		poetry run flake8 page_loader

reinstall:
	pip install --force-reinstall --user dist/*.whl