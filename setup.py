from cx_Freeze import setup, Executable

base = None
executables = [Executable("app.py", base=base)]


packages = ['flask', 'io', 'base64', 'numpy', 'matplotlib']
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
