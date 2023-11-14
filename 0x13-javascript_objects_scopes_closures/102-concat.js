#!/usr/bin/env node

const fileSync = require('fs');
const args = process.argv.slice(2);
const content1 = fileSync.readFileSync(args[0], 'utf-8');
const content2 = fileSync.readFileSync(args[1], 'utf-8');
fileSync.writeFileSync(args[2], (content1 + content2), 'utf-8');
