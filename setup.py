import cx_Freeze

executables = [cx_Freeze.Executable("maingame.py")]

cx_Freeze.setup(
    name="Raising the Steaks",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar.png"]}},
    executables = executables

    )
