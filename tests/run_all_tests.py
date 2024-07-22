import os
import sys
import pytest
import importlib


def reload_project_modules():
    project_dirs = [os.path.abspath("hypothesis_testing"), os.path.abspath("tests")]

    for module_name, module in list(sys.modules.items()):
        if module and hasattr(module, "__file__") and module.__file__:

            if any(os.path.abspath(module.__file__).startswith(project_dir) for project_dir in project_dirs):
                if module_name == "__main__":
                    continue
                try:
                    importlib.reload(module)
                except ImportError as e:
                    print(f"Error reloading module {module_name}: {e}")


while True:
    user_input = input("Press Enter to run the tests (or type 'exit' to quit): ").strip().lower()
    if user_input == "exit":
        break

    reload_project_modules()
    pytest.main(["tests"])
