cmake_minimum_required(VERSION 3.16)

project(sample_workspace_tasks_cmake LANGUAGES CXX)

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
