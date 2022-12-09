from src.const import Paths

# Convert path ot actual os path
def convert_path(path: str):
    return path.replace("/", Paths.SEPARATOR).replace("\\", Paths.SEPARATOR)