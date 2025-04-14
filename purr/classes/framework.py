import subprocess

class Framework():
    def __init__(self, framework_name, framework_language, framework_description, framework_repo):
        self.name = framework_name
        self.language = framework_language
        self.description = framework_description
        self.repository = framework_repo

    def get_name(self):
        return self.name

    def get_language(self):
        return self.language

    def get_description(self):
        return self.description

    def get_repository(self):
        return self.repository

    def set_name(self, name):
        self.name = name
        return True

    def set_language(self, language):
        self.language = language
        return True

    def set_description(self, description):
        self.description = description
        return True

    def set_repository(self, repository):
        self.repository = repository
        return True

    def dowload_git_repository(self):
        subprocess.run("git clone "+self.repository, shell=True, text=True)

    def __del__(self):
        print(f"Framework class  {self.name} deleted")
