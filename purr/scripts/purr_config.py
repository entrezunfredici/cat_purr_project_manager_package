from purr.classes import *
from purr.utils import *
import requests

def config():
    config_choises = {
        "create architecture": "architerture",
        "create framework": "framework",
        "exit": "exit"
    }
    json_langages = requests.get("https://api.github.com/languages").json()
    langage_list = []
    for language in json_langages:
        if language not in langage_list:
            langage_list.append(language["name"])

    configuration = {
        "architectures": [],
        "frameworks": [],
        "languages": langage_list
    }
    match selector(
        'config selector',
        'What configuration do you want to do?',
        config_choises
    ):
        case "architerture":
            infos = get_infos(["name"])
            configuration["architectures"]=(
                Architecture(
                    infos["name"],
                    {}
                )
            )
        case "framework":
            infos = get_infos(["name","description","repository"])
            language = selector(
                'language selector',
                'Which language choosen?',
                langage_list
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
    save = SaveFile(
        "config_file",
        configuration
    )
    config()

def get_infos(info_list):
    dict = {}
    for info in info_list:
        dict[info] = input("Enter %s?" % info)
    return dict

def get_config():
    return


