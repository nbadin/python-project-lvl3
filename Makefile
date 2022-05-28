build:
	poetry build

package-install:
	pip install --user dist/*.whl

install:
	poetry install