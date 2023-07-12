#!/usr/bin/python3
"""this ddfines a text file-reading function."""


def read_file(filename=""):
    """this prints the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
