import os, json

cf_path = "/mnt/c/Users/paulb/curseforge/minecraft/Instances/Herobrine.fr - Optimized/"
title_screen_path = cf_path + "config/isxander-main-menu-credits.json"
warning_path = cf_path + "config/fabric_loader_dependencies.json"

def load_json(path):
    return json.load(open(path))

def save_file(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, separators=(',', ':'))

title_screen_obj = load_json(title_screen_path)
existing_version = title_screen_obj["main_menu"]["bottom_right"][0]["text"]

print("Current version: " + existing_version)
new_version = input("Enter new version: Herobrine.fr - Optimized ")

title_screen_obj["main_menu"]["bottom_right"][0]["text"] = "Herobrine.fr - Optimized " + new_version
save_file(title_screen_path, title_screen_obj)

warning_file_obj = load_json(warning_path)
try:
    warning_file_obj["overrides"]["fabric-api"]["+recommends"]["Herobrine.fr - Optimized"] = ">" + new_version
except KeyError:
    warning_file_obj["overrides"]["fabric"]["+recommends"]["Herobrine.fr - Optimized"] = ">" + new_version
save_file(warning_path, warning_file_obj)