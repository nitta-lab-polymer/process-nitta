.PHONY: test-local
test-local:
	@echo "Running tests..."
	pip install pytest .
	pytest tests

.PHONY: clean
clean:
	@echo "Cleaning up..."
	@find . | grep __pycache__ | xargs rm -rf
	@find . | grep .pytest_cache | xargs rm -rf
	@find . | grep result_images | xargs rm -rf