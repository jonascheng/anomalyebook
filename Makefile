.DEFAULT_GOAL := help

APPLICATION?=anomalyebook
COMMIT_SHA?=$(shell git rev-parse --short HEAD)
DOCKER?=docker
DOCKERHUB_OWNER?=jonascheng
DOCKER_IMG_NAME=${DOCKERHUB_OWNER}/${APPLICATION}
PWD?=$(shell pwd)

# py version
PYTHON_VERSION = 3.11

# ANSI color codes
GREEN=$(shell tput -Txterm setaf 2)
YELLOW=$(shell tput -Txterm setaf 3)
RED=$(shell tput -Txterm setaf 1)
BLUE=$(shell tput -Txterm setaf 6)
RESET=$(shell tput -Txterm sgr0)

.PHONY: setup
setup: ## setup
	@$(MAKE) -s check-dependencies
	@$(MAKE) -s install-python-dependencies

check-dependencies:
	@echo "$(YELLOW)Checking dependencies...$(RESET)"
	@$(MAKE) -s check-python

check-python:
	@echo "$(YELLOW)Checking Python installation...$(RESET)"
	@if command -v python$(PYTHON_VERSION) > /dev/null; then \
		echo "$(BLUE)$(shell python$(PYTHON_VERSION) --version) already installed.$(RESET)"; \
	else \
		echo "$(RED)Python $(PYTHON_VERSION) is not installed. Please install Python $(PYTHON_VERSION) to continue.$(RESET)"; \
		exit 1; \
	fi

install-python-dependencies:
	@echo "$(GREEN)Installing Python dependencies...$(RESET)"
	python -m pip install --upgrade pip
	pip install -r requirements.txt -q

.PHONY: jupyter
jupyter: setup ## start jupyter notebook
	jupyter lab build
	Jupyter-lab

.PHONY: help
help: ## prints this help message
	@echo "Usage: \n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
