#!/usr/bin/env python

""" Calculates version64 value for semver string """

import os
import sys


def int2bin(tag: int, length) -> str:
    """ Converts integer to binary string """
    return format(tag, f"0{length}b")


def version_to_binary(version: str, lengths=[9, 8, 16, 31]) -> str:
    """
    Converts semver to version64 binary string

    For example:
    1.0.1.0 => 000000001 00000000 0000000000000001 0000000000000000000000000000000

    """
    version64_binary = ""
    for i, v in enumerate(version.split('.')):
        version64_binary += int2bin(int(v), lengths[i])

    return version64_binary


def binary_to_decimal(binary: str) -> int:
    """ Converts binary string to integer """
    return int(binary, 2)


def usage():
    print("Please provide semver string as argument!")
    print("Example: ./version.py 1.0.1.0")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()

    version = sys.argv[1]
    print(f"Version:  ", version)
    binary = version_to_binary(version)
    print(f"Binary:   ", binary)
    print(f"Version64:", binary_to_decimal(binary))
