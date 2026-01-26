module.exports = function(grunt) {
  // Project configuration
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    
    // Custom shell commands
    shell: {
      hello: {
        command: 'echo "Hello from Grunt!"'
      },
      longRunning: {
        command: 'node -e "console.log(\'Starting long running Grunt task...\'); for(let i=1; i<=10; i++) { console.log(\'Progress: \' + i + \'/10\'); require(\'child_process\').execSync(\'sleep 1\'); } console.log(\'Long running task completed!\');"'
      },
      failing: {
        command: 'echo "This Grunt task will fail..." && exit 1'
      }
    }
  });

  // Load the plugin that provides shell commands
  grunt.loadNpmTasks('grunt-shell');

  // Default task
  grunt.registerTask('default', ['shell:hello']);
  
  // Register tasks
  grunt.registerTask('hello', ['shell:hello']);
  grunt.registerTask('long-running', ['shell:longRunning']);
  grunt.registerTask('failing-task', ['shell:failing']);
};
