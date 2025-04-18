from .framework import Framework

class Layer():
    def __init__(self, layer_name, layer_framework_list):
        self.name = layer_name
        self.framework_list = layer_framework_list

    def add_framework(self, layer_framework):
        self.framework_list.append(layer_framework)

    def get_framework_list(self):
        return self.framework_list

    def get_framework(self, framework_name):
        for framework in self.framework_list:
            if framework.name == framework_name:
                return framework

    def __del__(self):
        for framework in self.framework_list:
            framework.__del__()
        print(f"LAyer  {self.name} deleted")
