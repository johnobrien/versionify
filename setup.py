import cx_Freeze
exe = [cx_Freeze.Executable("versionify.py")]
cx_Freeze.setup( name = "versionify", version = "1.0", description = "cx_Freeze versionify", executables = exe )