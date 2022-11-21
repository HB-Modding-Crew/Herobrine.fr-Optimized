import os, shutil

cf_path = "/mnt/c/Users/paulb/curseforge/minecraft/Instances/Herobrine.fr - Optimized/"
mmc_path = "/mnt/e/mmc-stable-win32/MultiMC/instances/Herobrine.fr-Optimized/"
git_path = "/mnt/e/Bureau/Progs/Perso/HB-Modding-Crew/Modpackwork/Herobrine.fr-Optimized/"
minecraft_version = "1.19.2"
packwiz_path = git_path + "Packwiz/" + minecraft_version

# Functions

def remove_dir(path, description):
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("Deleted " + description)
    else:
        print("Skipped " + description + " deletion, didn't exist")

def remove_file(path, description):
    if os.path.isfile(path):
        os.remove(path)
        print("Deleted " + description)
    else:
        print("Skipped " + description + " deletion, didn't exist")

def copy_dir(from_path, to_path, from_desc, to_desc):
    if os.path.isdir(from_path):
        ret = shutil.copytree(from_path, to_path, dirs_exist_ok=True)
        print("Copied " + from_desc + " to " + to_desc)
    else:
        print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

def copy_file(from_path, to_path, from_desc, to_desc):
    if os.path.isfile(from_path):
        shutil.copy2(from_path, to_path)
        print("Copied " + from_desc + " to " + to_desc)
    else:
        print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

# CurseForge to MultiMC directory
remove_dir(mmc_path + "minecraft/config/", "MultiMC configs")
remove_dir(mmc_path + "minecraft/mods/", "MultiMC mods")
remove_dir(mmc_path + "minecraft/resourcepacks/", "MultiMC resourcepacks")
copy_dir(cf_path + "config/", mmc_path + "minecraft/config/", "CurseForge configs", "MultiMC")
copy_dir(cf_path + "mods/", mmc_path + "minecraft/mods/", "CurseForge mods", "MultiMC")
copy_dir(cf_path + "resourcepacks/", mmc_path + "minecraft/resourcepacks/", "CurseForge resource packs", "MultiMC")

# CurseForge to MultiMC files
remove_file(mmc_path + "minecraft/options.txt", "MultiMC options.txt")
remove_file(mmc_path + "minecraft/servers.dat", "MultiMC servers.dat")
remove_file(mmc_path + "minecraft/servers.dat_old", "MultiMC servers.dat_old")

# CurseForge to Git directory
remove_dir(packwiz_path + "/config/", "Packwiz configs in Git")
copy_dir(cf_path + "config/", packwiz_path + "/config/", "CurseForge configs", "Git (Packwiz)")
copy_dir(cf_path + "resourcepacks/", packwiz_path + "/resourcepacks/", "CurseForge resource packs", "Git (Packwiz)")

# CurseForge to Git files
# Manifest and json copying moved to "CurseForge to Packwiz.py" to make sure they are always newest
remove_file(packwiz_path + "/servers.dat", "Git servers.dat")
remove_file(packwiz_path + "/servers.dat_old", "Git servers.dat_old")
remove_file(packwiz_path + "/options.txt", "Git options.txt")