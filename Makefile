env = dev

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

run:
	@python run.py

# -- test
check-debugger:
	@find cool_editor -type f -exec egrep -iH "set_trace" {} \+ && echo "Ooops! Found 1 set_trace on your source code!" && exit 1 || exit 0

test-travis: clean check-debugger
	py.test -n 2 cool_editor

test: SHELL:=/bin/bash
test: clean
	py.test cool_editor --pdb

test-matching: SHELL:=/bin/bash
test-matching: clean
	py.test cool_editor -k $(test) --pdb

coverage: SHELL:=/bin/bash
coverage: clean
	py.test --cov-config .coveragerc --cov cool_editor cool_editor --cov-report term-missing

# -- instalation and execution

.env: SHELL:=/bin/bash
.env: required-env
	@if [ $(env) == "dev" -a ! -e .env ]; then cp contrib/env-sample .env; fi
	@if [ $(env) == "test" -a ! -e .env ]; then cp contrib/env-sample .env; fi

required-env: SHELL:=/bin/bash
required-env:
	@if [ -z $(env) ]; then echo "env paramether is not set"; exit 1; fi
	@if [ $(env) != "prod" -a $(env) != "dev" -a $(env) != "test" ]; then echo "env paramether is not a valid value: dev, prod or test"; exit 1; fi

requirements: SHELL:=/bin/bash
requirements: required-env
	@if [ $(env) == "prod" ]; then pip install -r requirements.txt; fi
	@if [ $(env) == "dev" ]; then pip install -r requirements/development.txt; fi
	@if [ $(env) == "test" ]; then pip install -r requirements/development.txt; fi

