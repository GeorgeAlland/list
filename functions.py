FILEPATH = "list.txt"


def get_todos(filepath = FILEPATH):
    """Read a text file and return contents"""
    with open (filepath, "r")as file_local:
        todos_local = file_local.readlines()

    return todos_local

def write_todos(todos_arg,filepath = FILEPATH):
    """write input to a text file"""
    with open(filepath,"w") as file:
        file.writelines(todos_arg)
