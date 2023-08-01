# Pyre - Python regex tool

Didn't learn to use awk or grep? This tool uses python regex syntax to parse stdin.

## Installation

Clone:
`git clone git@github.com:jarvainen/pyre.git`
or just copy the code, it's one simple script.

Add to PATH or symlink to `/bin`.

## Usage

First parameter is regex, second parameter is output format:
`echo 'Firstname Lastname' | pyre '(.*) (.*)' '2, 1'`

Output format is string where numbers represent capture group.
