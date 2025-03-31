from .framework import Framework

class Architecture():
    def __init__(self, architecture_name, architecture_framework_dict):
        self.name = architecture_name
        self.framework_dict = architecture_framework_dict

    def get_framework_by_achitecture_layer(self, name):
        return self.framework_dict[name]

    def add_framework(self, layer_name, framework_name, framework_language, framework_description, framework_repo):
        self.framework_dict[layer_name] = Framework(framework_name, framework_language, framework_description, framework_repo)

    def __del__(self):
        print(f"Framework {self.name} supprimé")
