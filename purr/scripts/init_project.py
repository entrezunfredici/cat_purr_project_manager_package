import inquirer

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
    project_architecture = [
        inquirer.List('Project architecture',
                message="What project architecture do you need?",
                choices=config_infos.keys(),
            ),
    ]
    architecture_choosen = config_infos[inquirer.prompt(project_architecture)]
    for layer in architecture_choosen.keys():
        print(layer)
        framework_languages = [
            inquirer.List('Framework language',
                message="What language do you need?",
                choices=architecture_choosen[layer].keys(),
            ),
        ]
        language_choosen = architecture_choosen[inquirer.prompt(framework_languages)]
        framework 

