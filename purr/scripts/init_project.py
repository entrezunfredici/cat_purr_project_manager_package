from purr.classes import *
from purr.utils import *

def init_project(project_name):
    config = SaveFile(
        "config_file",
        {}
    )
    folder = folder_setup(config["workspace"]+"/"+project_name)
    #Choose project architecture
    architecture_choosen = selector(
        'Project architecture',
        'What project architecture do you need?',
        config["architectures"]
    )
    for layer in architecture_choosen.get_layer_list():
        #Choose main languages
        language_choosen = selector(
            'Framework language',
            'What language do you need?',
            config["languages"]
        )
        framework_dict = {}
        for framework in layer.get_framework_list():
            if framework.get_language() == language_choosen:
                framework_dict[framework.get_name()] = framework
        #choose framework
        framewor_choosen = selector(
            'Framework',
            'What framework do you need?',
            framework_dict
        )



