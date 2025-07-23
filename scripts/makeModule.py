"""
installation:
    - Windows
        - add environment variable "PYTHONPATH" and append your python file into it
    - Macos/Linux
        - add "export PYTHONPATH="/path/to/your/directory:$PYTHONPATH" into ~/.bashrc or ~/.zshrc
usage:
    $ python -m makeModule ModuleName RootName 
"""

def getPathInDot(path, rootName):
    if not path: 
        return ""
    s = path.stem
    path = path.parent
    while path and path != path.parent and path.name != rootName:
        s = f"{path.name}.{s}" 
        path = path.parent
    return s

def main():
    from sys import argv
    if len(argv) < 2:
        raise Exception("error: need module name argument")
    elif len(argv) < 3:
        raise Exception("error: need root name argument") 
    name = argv[1]
    rootName = argv[2]

    # create module 
    from tmodule import TModule
    m = TModule(name)

    from pathlib import Path
    cwd = Path.cwd()

    # create module dir
    moduleDir = cwd.joinpath(m.name)
    moduleDir.mkdir()

    # create m,c,v dir
    mDir = moduleDir.joinpath("m")
    mDir.mkdir()
    vDir = moduleDir.joinpath("v")
    vDir.mkdir()
    cDir = moduleDir.joinpath("c")
    cDir.mkdir()

    # create open command file
    ocFileName = f"{m.name}OpenCommand.lua"
    m.ocPath = cDir.joinpath(ocFileName) 
    m.ocPathInDot = getPathInDot(m.ocPath, rootName)  
    from addCommand import addOpenCommand
    try:
        addOpenCommand(m)
    except Exception as e:
        print(e)

    # create mediator file
    from addMediator import addMediator
    mediatorFileName = f"{m.name}Mediator.lua"  
    m.medPath = vDir.joinpath(mediatorFileName)
    m.medPathInDot = getPathInDot(m.medPath, rootName) 
    m.medABPath = (f"{m.name}/{m.name}panel.u3d").lower() # asset bundle path should be lower case
    try:
        addMediator(m)
    except Exception as e:
        print(e)

    # print mvc const value
    command = (f"{m.name}_panel_open_cmd").upper() 
    constValue = f"""
    mvcconst
        - command
            - {command} = "{m.ocPathInDot}"
        - mediator
            - {m.name}Mediator = "{m.medPathInDot}"
    mvcnoticeconst
        - MVCConst.{command} = "{command}"
    """
    print(constValue)

if __name__ == "__main__":
    main()
