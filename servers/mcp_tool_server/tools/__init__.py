import pkgutil, importlib, inspect
from pathlib import Path

def load_tools():
    """
    Load all Tool classes inside tools/ folder.
    """
    tools = {}
    package_dir = Path(__file__).resolve().parent

    for module_info in pkgutil.iter_modules([str(package_dir)]):
        module_name = f"{__name__}.{module_info.name}"
        module = importlib.import_module(module_name)

        # tìm class có name + run
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if hasattr(obj, "name") and hasattr(obj, "run"):
                tools[obj.name] = obj
    return tools
