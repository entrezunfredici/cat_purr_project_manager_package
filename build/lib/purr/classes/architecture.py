from .layer import Layer

class Architecture():
    def __init__(self, architecture_name, architecture_layer_list):
        self.name = architecture_name
        self.layer_list = architecture_layer_list

    def add_layer(self, layer):
        return self.layer_list.append(layer)

    def get_layer_list(self):
        return self.layer_list

    def get_layer(self, layer_name):
        for layer in self.layer_list:
            if layer.name == layer_name:
                return layer

    def __del__(self):
        print(f"Architecture  {self.name} deleted")
