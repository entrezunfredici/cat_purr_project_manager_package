import subprocess

def get_repository(repo_name):
    subprocess.run("git clone "+repo_name, shell=True, text=True)
