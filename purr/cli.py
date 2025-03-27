import sys
import inspect
import os
from .scripts import *
from .utils import *

def cli():
    if len(sys.argv) < 2:
        print("Usage: sudokeys <function_name> <arguments>")
        sys.exit(2)

    arguments = sys.argv[2:]

    try:
        function_name = os.path.basename(sys.argv[1])
        func = globals().get(function_name)
        if not func or not callable(func):
            raise ValueError(f"Function {function_name} not found!")
        signature = inspect.signature(func)
        parameters = list(signature.parameters.keys())
        if len(arguments) != len(parameters):
            print(f"Expected {len(parameters)} arguments, got {len(arguments)}")
            sys.exit(1)
        func(*arguments)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    cli()

