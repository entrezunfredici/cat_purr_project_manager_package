import os

def folder_setup(workspace_path):
    home_dir = os.path.expanduser("~")
    folder= home_dir+workspace_path+"/"
    os.makedirs(folder, exist_ok=True)
    return folder
