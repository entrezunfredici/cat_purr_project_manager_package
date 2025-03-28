import inquirer

def init_project():
    project_architecture = [
    inquirer.List('Project architecture',
            message="What project architecture do you need?",
            choices=['n-tier', 'mvc'],
        ),
    ]
    architecture_choosen = inquirer.prompt(project_architecture)
