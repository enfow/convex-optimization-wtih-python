format:
	black .
	isort .

lint:
	env PYTHONPATH=. pytest --flake8 --pylint --mypy

setup:
	pip install -U pip 
	pip install -U setuptools
	cat requirements.txt | xargs -n 1 pip install
