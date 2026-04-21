# Sample Workspace Tasks

A comprehensive sample repository containing multiple task definition types for testing VSCode extensions and task runners. This repository includes examples of various build tools, scripting languages, and task automation systems.

## 📁 Repository Structure

```
sample-workspace-tasks/
├── nodejs/              # Node.js npm scripts
├── makefile/            # GNU Make tasks
├── shell/               # Shell scripts
├── maven/               # Maven tasks
├── python/              # Python executable scripts
├── batch/               # Windows Batch files
├── powershell/          # PowerShell scripts
├── gradle/              # Gradle tasks
├── grunt/               # Grunt tasks
├── gulp/                # Gulp tasks
├── justfile/            # Just task runner
├── mise/                # mise task config variants
├── .vscode/             # VSCode tasks.json
└── .github/workflows/   # GitHub Actions workflows
```

## 🚀 Task Types

### 1. Node.js (npm scripts)

**Location:** `nodejs/package.json`

Simple npm scripts that can be run with `npm run <script>`.

**Available tasks:**
- `npm run hello` - Simple hello world
- `npm run long-running` - 10-second task simulation
- `npm run failing-task` - Intentionally fails with exit code 1
- `npm run build` - Simulated build process
- `npm run test` - Simulated test execution
- `npm run watch` - Continuous watching task

**Usage:**
```bash
cd nodejs
npm run hello
```

### 2. Makefile

**Location:** `makefile/Makefile`

GNU Make tasks for build automation.

**Available tasks:**
- `make hello` - Simple hello world
- `make long-running` - 8-second task
- `make failing-task` - Intentionally fails
- `make build` - Simulated build
- `make test` - Simulated tests
- `make clean` - Clean operation
- `make all` - Runs hello, build, and test

**Usage:**
```bash
cd makefile
make hello
```

### 3. Shell Scripts

**Location:** `shell/`

Bash scripts that can be executed directly (Linux/macOS).

**Available scripts:**
- `./hello.sh` - Simple hello world
- `./long-running.sh` - 10-second loop
- `./failing.sh` - Exits with error code 1

**Usage:**
```bash
cd shell
./hello.sh
```

### 4. Maven

**Location:** `maven/pom.xml`

Maven project with custom execution configurations.

**Available tasks:**
- `mvn exec:exec@hello` - Execute hello task
- `mvn clean` - Clean the project
- `mvn compile` - Compile sources
- `mvn test` - Run tests

**Usage:**
```bash
cd maven
mvn exec:exec@hello
```

### 5. Python Script

**Location:** `python/tasks.py`

Directly executable Python script with multiple commands.

**Available commands:**
- `./tasks.py` or `./tasks.py hello` - Simple hello
- `./tasks.py long-running` - 10-second task
- `./tasks.py failing` - Exits with error code 1

**Usage:**
```bash
cd python
./tasks.py hello
# or
python3 tasks.py hello
```

### 6. Batch Files

**Location:** `batch/`

Windows Batch scripts.

**Available scripts:**
- `hello.bat` - Simple hello world
- `long-running.bat` - 10-second task
- `failing.bat` - Exits with error code 1

**Usage (Windows):**
```cmd
cd batch
hello.bat
```

### 7. PowerShell Scripts

**Location:** `powershell/`

PowerShell scripts for Windows/Linux/macOS.

**Available scripts:**
- `hello.ps1` - Simple hello world
- `long-running.ps1` - 10-second task
- `failing.ps1` - Exits with error code 1

**Usage:**
```powershell
cd powershell
pwsh hello.ps1
# or
powershell -File hello.ps1
```

### 8. Gradle

**Location:** `gradle/build.gradle`

Gradle build script with custom tasks.

**Available tasks:**
- `gradle hello` - Simple hello world
- `gradle longRunning` - 10-second task
- `gradle failingTask` - Intentionally fails
- `gradle customBuild` - Build task
- `gradle customTest` - Test task

**Usage:**
```bash
cd gradle
gradle hello
# or if gradle wrapper is installed
./gradlew hello
```

### 9. Grunt

**Location:** `grunt/Gruntfile.js`

Grunt task runner configuration.

**Available tasks:**
- `grunt hello` - Simple hello world
- `grunt long-running` - 10-second task
- `grunt failing-task` - Intentionally fails

**Setup and Usage:**
```bash
cd grunt
npm install
npx grunt hello
```

### 10. Gulp

**Location:** `gulp/gulpfile.js`

Gulp task runner configuration.

**Available tasks:**
- `gulp hello` - Simple hello world
- `gulp longRunning` - 10-second task
- `gulp failingTask` - Intentionally fails
- `gulp build` - Build task
- `gulp test` - Test task

**Setup and Usage:**
```bash
cd gulp
npm install
npx gulp hello
```

### 11. Justfile

**Location:** `justfile/justfile`

Just command runner configuration.

**Available recipes:**
- `just` or `just default` - Default recipe
- `just hello` - Simple hello world
- `just long-running` - 10-second task
- `just failing-task` - Intentionally fails
- `just build` - Build task
- `just test` - Test task
- `just clean` - Clean task

**Setup:**
Install Just: https://github.com/casey/just#installation

**Usage:**
```bash
cd justfile
just hello
```

### 12. mise

**Location:** `mise/`

Examples of supported mise config file locations and naming variants. Every file contains `echo`-based tasks only.

**Included file patterns:**
- `mise.toml`
- `mise.local.toml`
- `.mise.toml`
- `mise/config.toml`
- `.mise/config.toml`
- `.config/mise.toml`
- `.config/mise/config.toml`
- `.config/mise/conf.d/dev.toml`

**Usage:**
```bash
cd mise
mise run rootTask
```

### 13. VSCode Tasks

**Location:** `.vscode/tasks.json`

VSCode-specific task definitions that appear in the Command Palette.

**Available tasks:**
- `VSCode: Hello` - Simple hello world
- `VSCode: Long Running` - 10-second task
- `VSCode: Failing Task` - Intentionally fails
- `VSCode: Build` - Build task (default build)
- `VSCode: Test` - Test task (default test)
- `Run Node.js Hello` - Executes Node.js hello task
- `Run Shell Script` - Executes shell script
- `Run Python Script` - Executes Python script
- `Run Make Hello` - Executes Make hello task

**Usage:**
1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
2. Type "Tasks: Run Task"
3. Select a task from the list

### 13. GitHub Actions

**Location:** `.github/workflows/sample-tasks.yml`

GitHub Actions workflow with multiple jobs.

**Available workflows:**
- `hello-task` - Simple hello world job
- `long-running-task` - 10-second task job
- `failing-task` - Intentionally failing job
- `test-all-samples` - Tests multiple sample scripts

**Trigger options:**
- Manual trigger via workflow_dispatch (with task type selection)
- Automatic trigger on push to main
- Automatic trigger on pull requests to main

**Usage:**
1. Push to main branch or create a pull request
2. Or manually trigger via GitHub Actions tab in the repository

## 📋 Task Categories

### ✅ Successful Tasks
Most tasks are designed to complete successfully, demonstrating normal operation.

### ⏱️ Long-Running Tasks
Tasks that simulate longer operations (8-10 seconds):
- `npm run long-running`
- `make long-running`
- `./shell/long-running.sh`
- `./python/tasks.py long-running`
- `long-running.bat`
- `long-running.ps1`
- `gradle longRunning`
- `grunt long-running`
- `gulp longRunning`
- `just long-running`
- `VSCode: Long Running`

### ❌ Failing Tasks
Tasks that intentionally fail with non-zero exit codes:
- `npm run failing-task`
- `make failing-task`
- `./shell/failing.sh`
- `./python/tasks.py failing`
- `failing.bat`
- `failing.ps1`
- `gradle failingTask`
- `grunt failing-task`
- `gulp failingTask`
- `just failing-task`
- `VSCode: Failing Task`

## 🧪 Testing VSCode Extensions

This repository is designed to test VSCode extensions that work with task runners. All tasks are minimal and focused on demonstrating different task definition formats.

### Test Scenarios

1. **Task Detection**: Extensions should detect all task types
2. **Task Execution**: All successful tasks should run without errors
3. **Long-Running Tasks**: Extensions should handle long-running operations
4. **Failing Tasks**: Extensions should properly report failed tasks
5. **Output Parsing**: Extensions should capture and display task output
6. **Multi-Format Support**: Extensions should support multiple task definition formats

## 🛠️ Prerequisites

Depending on which samples you want to run, you may need:

- **Node.js & npm**: For Node.js, Grunt, and Gulp samples
- **Make**: For Makefile samples (usually pre-installed on Linux/macOS)
- **Python 3**: For Python samples
- **Java & Maven**: For Maven samples
- **Gradle**: For Gradle samples
- **Just**: For Justfile samples (needs separate installation)
- **PowerShell**: For PowerShell samples (pre-installed on Windows, available for Linux/macOS)

## ⚠️ Platform Compatibility

Some samples use platform-specific commands for demonstration purposes:

- **Shell scripts** (`.sh`): Designed for Linux/macOS with Bash
- **Batch files** (`.bat`): Designed for Windows Command Prompt
- **PowerShell scripts** (`.ps1`): Cross-platform with PowerShell Core, or Windows PowerShell
- **Makefile, Justfile, Node.js tasks**: Some use Unix-specific commands (e.g., `sleep`) and may need adaptation for Windows

This variety is intentional to provide comprehensive testing scenarios for VSCode extensions across different platforms and task types.

## 📝 License

This is a sample repository for testing purposes. Feel free to use and modify as needed.
