.PHONY: hello long-running failing-task build test clean all

all: hello build test

hello:
	@echo "Hello from Makefile!"

long-running:
	@echo "Starting long running task..."
	@sleep 8
	@echo "Long running task completed!"

failing-task:
	@echo "This task will intentionally fail..."
	@exit 1

test2:
	@echo "test all the things"

nbuild:
	@echo "Building with Make..."
	@sleep 2
	@echo "Build successful!"

test:
	@echo "Running tests with Make..."
	@echo "Tests passed!"
	@echo "TEST_TOKEN: $$TEST_TOKEN"
	@echo "MY_TEST_TOKEN: $$MY_TEST_TOKEN"
	@echo "TEST_API_KEY: $$TEST_API_KEY"
	@echo "NO_TEST_TOKEN: $$NO_TEST_TOKEN"

clean:
	@echo "Cleaning up..."
	@echo "Clean complete!"
