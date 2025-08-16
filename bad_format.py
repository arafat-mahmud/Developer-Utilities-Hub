import csv
import json
import os
import sys


def bad_function(x, y, z=10):
    result = x + y + z
    long_string = "This is a very long string that should be wrapped to multiple lines according to PEP 8 style guidelines"
    return result, long_string
