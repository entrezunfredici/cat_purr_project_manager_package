from .framework import Framework

class Architecture():
    def __init__(self, architecture_name, architecture_framework_list):
        self.name = architecture_name
        for framework_info in architecture_framework_list:
            self.framework_dict = Framework(
                framework_info["name"],
                framework_info["language"],
                framework_info["description"],
                framework_info["repository"]
            )

    def get_framework_by_achitecture_layer(self, name):
        return self.framework_dict[name]

    def add_framework(self, layer_name, framework_name, framework_language, framework_description, framework_repo):
        self.framework_dict[layer_name] = Framework(framework_name, framework_language, framework_description, framework_repo)

    def __del__(self):
        print(f"Architecture  {self.name} deleted")
