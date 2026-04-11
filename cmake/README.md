# CMake Sample

This directory contains a minimal C++ project that demonstrates how the
**CMake** task provider discovers and presents targets from `CMakeLists.txt`.

## Discovered Tasks

The Workspace Tasks extension will automatically find this `CMakeLists.txt` and
present the following targets in the task panel:

| Target | Type | Description |
|---|---|---|
| `hello_world` | `add_executable` | Build the hello-world binary |
| `greeter` | `add_executable` | Build the greeter binary |
| `run_hello` | `add_custom_target` | Build and run hello_world |
| `run_greeter` | `add_custom_target` | Build and run greeter |
| `clean_all` | `add_custom_target` | Remove all build artefacts |
| `format` | `add_custom_target` | Format source files with clang-format |
| `lint` | `add_custom_target` | Run static analysis with cppcheck |

## Building Manually

```bash
# 1. Configure (Debug build, build/ directory)
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug

# 2. Build all targets
cmake --build build

# 3. Build a specific target
cmake --build build --target hello_world

# 4. Run tests with CTest
ctest --test-dir build

# 5. Install
cmake --install build
```

## Extension Settings

The following `workspaceTasks` settings control how CMake tasks are built and run:

| Setting | Default | Description |
|---|---|---|
| `workspaceTasks.applicationPath.cmake` | `cmake` | Path to the cmake executable |
| `workspaceTasks.cmake.buildDirectory` | `build` | Build dir relative to `CMakeLists.txt` |
| `workspaceTasks.cmake.buildType` | `Debug` | `Debug` / `Release` / `RelWithDebInfo` / `MinSizeRel` |
| `workspaceTasks.cmake.generator` | _(empty)_ | Generator name, e.g. `Ninja` |
