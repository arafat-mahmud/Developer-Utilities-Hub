import os
import sys
from pathlib import Path


def hello_world(name, age=25):
    message = f"Hello {name}, you are {age} years old"
    return message


if __name__ == "__main__":
    result = hello_world("Alice", 30)
    print(result)
