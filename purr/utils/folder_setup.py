import os

def folder_setup():
    home_dir = os.path.expanduser("~")
    folder= home_dir+"/Workspace/"
    os.makedirs(folder, exist_ok=True)
    return folder
