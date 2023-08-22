import os


# Set file path
def set_file_path(instance, filename):
    owner = instance.owner
    return os.path.join("users", str(owner.id), "files", filename)
