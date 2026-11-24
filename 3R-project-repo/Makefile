AWS_REGION=us-east-1
AWS_ACCOUNT_ID=123456789012
AWS_ECR_URL=$(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com

CODE_ARTIFACT_REPO=python-packages
CODE_ARTIFACT_DOMAIN=code-artifacts

.PHONY: clean
clean:		## Clean up python build files
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -fr build
	rm -f .coverage

.PHONY: install
install:	## Install package
	pip install .

.PHONY: install-dev
install-dev:	## Install package with dev and test dependencies and allow code edits to the installed package 
	pip install -e .[test,dev]

.PHONY: install-test
install-test:	## Install package with test dependencies for testing locally and in CI
	pip install .[test]

.PHONY: update-requirements
update-requirements:	## Generate or update the requirements.txt file based on requirements from setup.cfg
	pip-compile setup.cfg

.PHONY: test-all
test-all: 	## Run all the formating/linting and pytest tests
test-all: test-formatting-linting test-pytest

.PHONY: test-formatting-linting
test-formatting-linting: 	## Run all the formating/linting
test-formatting-linting: test-isort test-black test-flake8 test-pylint 

.PHONY: test-isort
test-isort:	## Check that all files have their import statements correctly formatted, fails if not
	isort --profile black --check .

.PHONY: test-black
test-black:	## Check that Black formatting is correct, fails if not
	black --check .

.PHONY: test-flake8
test-flake8:	## Check flake8 formatting, fails if not
	flake8

.PHONY: test-pylint
test-pylint:	## Check pylint is OK or fails
	pylint src

.PHONY: test-pytest
test-pytest:	## Run tests with pytest
	# Run coverage only on the unit tests
	pytest --cov=3R-project-repo tests/unit

	# Then run tests without coverage
	pytest

.PHONY: format
format:		## Applies isort and black formatting
	isort --profile black .
	black .


.PHONY: get-code-artifact-url
get-code-artifact-url:
	$(eval CODEARTIFACT_AUTH_TOKEN := $(shell aws codeartifact get-authorization-token --domain $(CODE_ARTIFACT_DOMAIN) --domain-owner $(AWS_ACCOUNT_ID) --query authorizationToken --output text))
	$(eval CODEARTIFACT_URL := https://aws:$(CODEARTIFACT_AUTH_TOKEN)@$(CODE_ARTIFACT_DOMAIN)-$(AWS_ACCOUNT_ID).d.codeartifact.$(AWS_REGION).amazonaws.com/pypi/$(CODE_ARTIFACT_REPO)/simple/)

.PHONY: code-artifact-read-access
code-artifact-read-access: get-code-artifact-url	## Login in to AWS Code Artifact requires AWS credentials to be set
	# This sets pip index url on a user level
	@pip config set --user global.extra-index-url https://pypi.org/simple/
	# This allows us to add the Code Artifact URL with temporary credentials as an extra index
	@pip config set --user global.index-url $(CODEARTIFACT_URL) 

help:		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

# Define a function that gets the current package version
# Note: python must be set up with release dependencies installed first.
define get_current_version
$(shell semantic-release print-version --current)
endef
