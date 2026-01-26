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

build:
	@echo "Building with Make..."
	@sleep 2
	@echo "Build successful!"

test:
	@echo "Running tests with Make..."
	@echo "Tests passed!"

clean:
	@echo "Cleaning up..."
	@echo "Clean complete!"
