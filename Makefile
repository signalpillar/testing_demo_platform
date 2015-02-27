deps:
	pip install -r requirements.txt

testinious:
	py.test --capture=no --lf -x -v --pep8 --looponfail

test:
	py.test --capture=no --lf -x -v --pep8
