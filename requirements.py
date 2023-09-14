import importlib

# List of libraries to install
libraries = [
    "matplotlib",
    "pandas",
    "numpy",
    "seaborn",
    "torch",
    "Pillow",
    "pickle",
    "opencv-python"
]

# Iterate through the list of libraries
for library in libraries:
    try:
        importlib.import_module(library)
        print(f"{library} is already installed.")
    except ImportError:
        try:
            import pip
            pip.main(["install", library])
            print(f"{library} has been successfully installed.")
        except Exception as e:
            print(f"Failed to install {library}: {e}")