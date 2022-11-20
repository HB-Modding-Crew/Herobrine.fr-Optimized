import os, shutil, re, zipfile

mmc_path = "/mnt/e/mmc-stable-win32/MultiMC/instances/Herobrine.fr-Optimized/"
git_path = "/mnt/e/Bureau/Progs/Perso/HB-Modding-Crew/Modpackwork/Herobrine.fr-Optimized/"
output_path = "/mnt/e/Bureau/Progs/Perso/HB-Modding-Crew/Modpackwork/Herobrine.fr-Optimized/"

# Functions

def copy_file(from_path, to_path, from_desc, to_desc):
    if os.path.isfile(from_path):
        shutil.copy2(from_path, to_path)
        print("Copied " + from_desc + " to " + to_desc)
    else:
        print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

def copy_to_archive(from_path, to_path, archive_path):

    files = []

    with zipfile.ZipFile(archive_path) as archive:
        for zipinfo in archive.infolist():
            if zipinfo.filename != to_path:
                files.append((zipinfo.filename, archive.read(zipinfo.filename)))

    with zipfile.ZipFile(archive_path, "w") as archive:
        for filename, content in files:
            archive.writestr(filename, content)
        archive.write(from_path, to_path)

# MultiMC to Git

version = "1.0.2"
pattern = re.compile(r"\d+\.\d+\.\d+-?\w*\.?\d*")

with open(mmc_path + "instance.cfg") as file:
    if match := pattern.search(file.read()):
        version = match.group()

with open(git_path + "MultiMC/Herobrine.fr-Optimized x.y.z/instance.cfg", "r+") as file:
    data = pattern.sub(version, file.read())
    file.seek(0); file.truncate(); file.write(data)

copy_to_archive(git_path + "MultiMC/Herobrine.fr-Optimized x.y.z/instance.cfg", f"Herobrine.fr - Optimized/instance.cfg", output_path + f"Herobrine.fr-Optimized-mmc-{version}.zip")
copy_file(mmc_path + "mmc-pack.json", git_path + "MultiMC/Herobrine.fr-Optimized x.y.z/mmc-pack.json", "MultiMC mmc-pack.json", "Git")
copy_file(mmc_path + "pack.png", git_path + "MultiMC/Herobrine.fr-Optimized x.y.z/pack.png", "MultiMC pack.png", "Git")