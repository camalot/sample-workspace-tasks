const { src, dest, series, parallel } = require('gulp');
const { exec } = require('child_process');
const util = require('util');
const execPromise = util.promisify(exec);

// Simple hello task
function hello(cb) {
  console.log('Hello from Gulp!');
  cb();
}

// Long running task
function longRunning(cb) {
  console.log('Starting long running Gulp task...');
  let count = 1;
  const interval = setInterval(() => {
    console.log(`Progress: ${count}/10`);
    count++;
    if (count > 10) {
      clearInterval(interval);
      console.log('Long running task completed!');
      cb();
    }
  }, 1000);
}

// Failing task
function failingTask(cb) {
  console.log('This Gulp task will fail...');
  cb(new Error('Simulated task failure'));
}

// Build task
function build(cb) {
  console.log('Building with Gulp...');
  setTimeout(() => {
    console.log('Build successful!');
    cb();
  }, 2000);
}

// Test task
function test(cb) {
  console.log('Running tests with Gulp...');
  console.log('Tests passed!');
  cb();
}

// Export tasks
exports.hello = hello;
exports.longRunning = longRunning;
exports.failingTask = failingTask;
exports.build = build;
exports.test = test;
exports.default = hello;
