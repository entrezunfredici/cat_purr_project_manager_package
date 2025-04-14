import inquirer
from purr.classes import *
from purr.utils import *

config_infos = {
    "mvc": {
        "main framework": {
            "python": ["Django"],
            "PHP": ["Synfony", "Laravel"],
        },
    },
    "n-tiers":{
        "framework back": {
            "node JS": ["express_js"],
        },
        "framework front": {
            "JS": ["VueJS"],
        },
        "sgbd": {
            "Yes i want SGBD": ["Postgres"],
            "No i want sqlite": []
        }
    }
}

def init_project():
    #Choose project architecture
    architecture_choosen = selector(
        'Project architecture',
        'What project architecture do you need?',
        config_infos
    )
    for layer in architecture_choosen.keys():
        #Choose main languages
        language_choosen = selector(
            'Framework language',
            'What language do you need?',
            architecture_choosen[layer]
        )
        #choose framework
        framewor_choosen = selector(
            'Framework',
            'What framework do you need?',
            architecture_choosen[layer[language_choosen]]
        )


