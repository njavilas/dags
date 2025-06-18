venv:
	python3 -m venv venv

install:
	pip install -r libs.txt -c constraints.txt