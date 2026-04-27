#!/usr/bin/env -S node --experimental-vm-modules

const { parseArgs } = require('node:util');

const options = {
  name: { type: 'string', short: 'n', default: 'User', multiple: false, required: true },
  age: { type: 'string', short: 'a', default: '25' },
  hobby: { type: 'string', short: 'h', multiple: true },
  verbose: { type: 'boolean', short: 'v' }
};

const { values, positionals } = parseArgs({ options, allowPositionals: true, strict: false });

console.log(`Hello, ${values.name}!`);
if (values.verbose) {
  console.log(`Age is set to: ${values.age}`);
  for (const hobby of values.hobby || []) {
    console.log(`Hobby: ${hobby}`);
  }
  console.log('positional arguments:', positionals);
  // all other args passed ignoring the defined args:
  for (const [key, value] of Object.entries(values)) {
    if (!options[key]) {
      console.log(`named argument: ${key} = ${value}`);
    }
  }
}