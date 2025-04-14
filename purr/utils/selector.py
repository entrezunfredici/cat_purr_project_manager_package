import inquirer

def selector(selector_name, selector_message, selector_choices_dict):
    select = [
        inquirer.List(selector_name,
                message=selector_message,
                choices=selector_choices_dict.keys(),
            ),
    ]
    return selector_choices_dict[inquirer.prompt(select)]
