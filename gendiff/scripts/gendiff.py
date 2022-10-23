#!/usr/bin/env python
from gendiff import cli, engine


def main():
    args = cli.parse_args()
    engine.start_program(args)


if __name__ == '__main__':
    main()
