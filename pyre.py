#!/usr/bin/python3
import sys
import re

def print_help():
    print("pyre <regex> [output_format]")
    print("output_format: '1:2'")
    print("where 1 and 2 are replaced with capture group from regex")
    print("Example: ")
    print("echo 'Firstname Lastname' | pyre '(.*) (.*)' '2, 1'")

def main():
    arg_count = len(sys.argv)

    if arg_count < 2:
        print("Missing parameter: regex required")
        sys.exit(1)

    regex = sys.argv[1]

    output_format = None
    if arg_count > 2:
        output_format = sys.argv[2]

    for line in sys.stdin:
        results = re.search(regex, line)
        if results:
            if output_format:
                output = output_format
                for i in range(0, len(results.groups()) + 1):
                    output = output.replace(str(i), results.group(i))
                print(output)
            else:
                print(results.group(0))


if __name__ == "__main__":
    main()
