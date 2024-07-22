import os
import sys
import pytest
import importlib


def reload_project_modules():
    project_dir = os.path.abspath("hypothesis_testing_tool")

    for _, module in list(sys.modules.items()):
        if module and hasattr(module, "__file__") and module.__file__:
            module_path = os.path.abspath(module.__file__)
            if module_path.startswith(project_dir):
                importlib.reload(module)


while True:
    user_input = input("Press Enter to run the tests (or type 'exit' to quit): ").strip().lower()
    if user_input == "exit":
        break

    reload_project_modules()
    pytest.main(["-q", "tests"])
