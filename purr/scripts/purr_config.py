from purr.classes import *
from purr.utils import *
import questionary
import requests

def config():
    config_choises = {
        "set workspace": "workspace",
        "create framework": "framework",
        "create layer": "layer",
        "create architecture": "architerture",
        "exit": "exit"
    }

    config_save = SaveFile(
        "config_file",
        {}
    )

    langage_dict = {}
    try:
        json_langages = requests.get("https://api.github.com/languages").json()
        for language in json_langages:
            langage_dict[language["name"]]=language["name"]
    except:
        print("fail to connect github api")
        langage_dict = config_save.read_data(["languages"])

    configuration = config_save.read_data(["architectures","layers","frameworks"])
    configuration ["languages"] = langage_dict
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
            configuration["architectures"][infos["name"]] = (
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
            configuration["layers"][infos["name"]] = (
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
            configuration["frameworks"][infos["name"]] = (
                Framework(
                    infos["name"],
                    language,
                    infos["description"],
                    infos["repository"]
                )
            )
        case "workspace":
            configuration ["workspace"] = get_infos(["workspace path"])
        case _:
            return
    config_save.save_data(configuration)
    config()

def get_infos(info_list):
    dict = {}
    for info in info_list:
        dict[info] = input("Enter %s?" % info)
    return dict
