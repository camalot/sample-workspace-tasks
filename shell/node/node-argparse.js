#!/usr/bin/env -S node --experimental-vm-modules
const { ArgumentParser } = require('argparse');

const parser = new ArgumentParser({
  description: 'Node.js version of Python argparse'
});

parser.add_argument('-n', '--name', { help: 'The user name', required: true, type: 'str', default: 'User' });
parser.add_argument('-a', '--age', { help: 'The user age', default: 25, type: 'int' });
parser.add_argument('-v', '--verbose', { action: 'store_true', help: 'Show more details' });

const args = parser.parse_args();

console.log(`Hello, ${args.name}!`);
if (args.verbose) console.log(`Age is set to: ${args.age}`);
console.log('positional arguments:', args.positionals);
// all other args passed ignoring the defined args:
for (const [key, value] of Object.entries(args)) {
  if (!parser._option_string_actions[key]) {
    console.log(`named argument: ${key} = ${value}`);
  }
}