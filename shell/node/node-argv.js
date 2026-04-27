#!/usr/bin/env -S node --experimental-vm-modules

console.log("Arguments passed to the script:");
console.log("--------------------------------------------");

for (let i = 2; i < process.argv.length; i++) {
  console.log(`Argument ${i}: ${process.argv[i]}`);
}

console.log("--------------------------------------------");