def isFileExist(path):
    try:
        f = open(path)
    except FileNotFoundError:
        return False
    else:
        f.close()
        return True

def safeWrite(path, content, force):
    if not isFileExist(path) or force:
        with open(path, "w") as f:
            f.write(content)
    else:
        raise FileExistsError(f"error: file {path} exist") 

# def genPath():
#     from pathlib import Path
#     cwd = Path.cwd()
#     print(f"cwd: {cwd}")
#     parent = cwd.parent
#     while parent and parent.parent != parent:
#         print(parent)
#         parent = parent.parent 
