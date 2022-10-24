#!/usr/bin/env python
from gendiff import cli, engine


def main():
    args = cli.parse_args()
    print(engine.generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
