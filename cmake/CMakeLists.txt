cmake_minimum_required(VERSION 3.16)

project(SampleProject VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --------------------------------------------------------------------------
# Executables
# --------------------------------------------------------------------------

add_executable(hello_world src/hello.cpp)

add_executable(greeter src/greeter.cpp)

# --------------------------------------------------------------------------
# Custom targets — these appear as tasks in the Workspace Tasks panel
# --------------------------------------------------------------------------

# Build and run the hello_world binary
add_custom_target(run_hello
  COMMAND hello_world
  DEPENDS hello_world
  COMMENT "Running hello_world"
)

# Build and run the greeter binary
add_custom_target(run_greeter
  COMMAND greeter
  DEPENDS greeter
  COMMENT "Running greeter"
)

# Remove all generated build artefacts
add_custom_target(clean_all
  COMMAND ${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR} --target clean
  COMMENT "Cleaning all build artefacts"
)

# Format source files with clang-format (requires clang-format on PATH)
add_custom_target(format
  COMMAND clang-format -i src/hello.cpp src/greeter.cpp
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  COMMENT "Formatting source files"
)

# Run static analysis with cppcheck (requires cppcheck on PATH)
add_custom_target(lint
  COMMAND cppcheck --enable=all --suppress=missingIncludeSystem src/
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  COMMENT "Running cppcheck static analysis"
)

# Targets discovered by the extension's CMake task provider.
add_custom_target(sample-hello
	COMMAND ${CMAKE_COMMAND} -E echo "Hello from sample CMake task"
	VERBATIM
)

add_custom_target(sample-info
	COMMAND ${CMAKE_COMMAND} -E echo "Source dir: ${CMAKE_SOURCE_DIR}"
	COMMAND ${CMAKE_COMMAND} -E echo "Build dir: ${CMAKE_BINARY_DIR}"
	VERBATIM
)


# --------------------------------------------------------------------------
# Tests — registered with CTest
# --------------------------------------------------------------------------

enable_testing()

add_test(NAME HelloWorldTest COMMAND hello_world)
add_test(NAME GreeterTest    COMMAND greeter)
