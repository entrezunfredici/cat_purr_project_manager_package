from purr.classes import *
from purr.utils import *
import questionary
import requests

def config():
    config_choises = {
        "create architecture": "architerture",
        "create layer": "layer",
        "create framework": "framework",
        "exit": "exit"
    }
    json_langages = requests.get("https://api.github.com/languages").json()
    langage_dict = {}
    save = SaveFile(
        "config_file",
        {}
    )
    
    for language in json_langages:
        print(language["name"])
        langage_dict[language["name"]]=language["name"]

    configuration = {
        "architectures": [],
        "layers": [],
        "frameworks": [],
        "languages": langage_dict
    }
    match selector(
        'config selector',
        'What configuration do you want to do?',
        config_choises
    ):
        case "architerture":
            infos = get_infos(["name"])
            layer_list = questionary.checkbox(
                "Choose yours layers :",
                choices=configuration["layers"]
            ).ask()
            configuration["architectures"]=(
                Architecture(
                    infos["name"],
                    layer_list
                )
            )
        case "layer":
            infos = get_infos(["name"])
            framework_list = questionary.checkbox(
                "Choose yours frameworks :",
                choices=configuration["frameworks"]
            ).ask()
            configuration["layers"]=(
                Architecture(
                    infos["name"],
                    framework_list
                )
            )
        case "framework":
            infos = get_infos(["name","description","repository"])
            language = selector(
                'language selector',
                'Which language choosen?',
                langage_dict
            )
            configuration["frameworks"]=(
                Framework(
                    infos["name"],
                    language,
                    infos["description"],
                    infos["repository"]
                )
            )
        case _:
            return
    config()

def get_infos(info_list):
    dict = {}
    for info in info_list:
        dict[info] = input("Enter %s?" % info)
    return dict

def get_config():
    return


