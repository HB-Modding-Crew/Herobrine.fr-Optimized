import json
import toml
import os
import zipfile
import sys
from collections import defaultdict
from modrinth import Projects, Versions
from py_markdown_table.markdown_table import markdown_table

""" Modrinth class """

# Modrinth project and version class
class ModrinthProjectAb:
    def __init__(self, id, version_id):
        self.id = id
        try:
            self.project = Projects.ModrinthProject(id)
        except:
            print("ERROR: Modrinth API is not responding, trying again...")
            self.project = Projects.ModrinthProject(id)
        try:
            self.version = Versions.ModrinthVersion(self.project, version_id)
        except:
            print("ERROR: Modrinth API is not responding, trying again...")
            self.version = Versions.ModrinthVersion(self.project, version_id)
        self.slug = self.project.slug
        self.name = self.project.name
        self.desc = self.project.desc
        # Author field should wait that Modrinth API is enhanced
        self.version_id = self.version.version
        self.version_name = self.version.name
        self.version_number = self.version.versionNumber
        
# Modrinth mod class inheriting from ModrinthProject
# Add the url and version url field to the ModrinthProject class: https://modrinth.com/mod/{id} and https://modrinth.com/mod/{slug}/version/{version_number}
class ModrinthMod(ModrinthProjectAb):
    def __init__(self, id, version_id):
        super().__init__(id, version_id)
        self.url = f"https://modrinth.com/mod/{self.id}"
        self.version_url = f"https://modrinth.com/mod/{self.slug}/version/{self.version_number}"
        
""" Memory class """

# ModMemory static class
# Able to load and write in the memory file "modlist/mod_memory.json"
# The json contain a dict of memory
# Each memory is a dict with the mod slug as key and the memory object as value
# The memory object contain the category of the mod, and wether it is optional or not
# The method "apply" is used to create or modify a memory object
class ModMemory:
    
    # memory dict
    memory: dict
    
    # Load the memory file
    def load():
        try:
            with open("modlist/mod_memory.json", "r") as file:
                ModMemory.memory = json.load(file)
        except FileNotFoundError:
            ModMemory.memory = {}
            ModMemory.write()
            
    # Write in the memory file
    def write():
        with open("modlist/mod_memory.json", "w") as file:
            json.dump(ModMemory.memory, file, indent=4)
            
    # Apply a memory to a mod
    def apply(mod, category, optional):
        if mod in ModMemory.memory:
            ModMemory.memory[mod]["category"] = category
            ModMemory.memory[mod]["optional"] = optional
        else:
            ModMemory.memory[mod] = {
                "category": category,
                "optional": optional
            }
        ModMemory.write()
        
    # Get the memory of a mod
    def get(mod):
        if mod in ModMemory.memory:
            return ModMemory.memory[mod]
        else:
            return None
        
    # Remove the memory of a mod
    def remove(mod):
        if mod in ModMemory.memory:
            del ModMemory.memory[mod]
            ModMemory.write()
            
    # Get the memory of a mod, or create it if it doesn't exist
    def get_or_create(mod):
        if mod in ModMemory.memory:
            return ModMemory.memory[mod]
        else:
            ModMemory.memory[mod] = {
                "category": "general",
                "optional": False
            }
            return ModMemory.memory[mod]
        
""" ModEntryDataClass """

# ModEntryDataClass class contain the data for a mod entry in a table
# It can be built in two ways:
#
# First way:
# With a toml file, using the "from_toml" method. The toml file should look like this:
# ```toml
# name = "Amecs"
# 
# [download]
# url = "https://cdn.modrinth.com/data/rcLriA4v/versions/cxa4Xr5x/amecs-1.3.9%2Bmc.1.20-pre2.jar"
# hash-format = "sha512"
# hash = "8794cc3c5cb009064cb25e8214ae6b04084c92766e3c6a9e707fdf505acb04cddfceb5d957dce82315a281db7a7d51d9f68ba886fc7740a4c5bee417b0cea3ca"
# 
# [update]
# [update.modrinth]
# mod-id = "rcLriA4v"
# version = "cxa4Xr5x"
# ```
# A Modrinth object have to be created with the mod-id as project id, and the version as version id
# then the Mod Name, slug, URL, Description, and version number should be set
#
# Second way:
# With a raw mod (.jar file), using the "from_raw" method. The mod should be a .jar file
# The .jar should be opened as a zip file, and the fabric.mod.json file should be read
# and the Mod Name (name field in the .json), slug (id field in the .json), URL (contact.homepage in the .json), Description (description in the .json), and version number (version in the .json) should be set
#
# Finally, the table row data can be built. It should be an object with the following fields:
# Mod, Version, Description
# Each field should contain it's data, but the Mod field should be clickable and link to the mod URL

class ModEntryDataClass:
    
    # Constructor
    def __init__(self, data):
        self.name = data["name"]
        self.slug = data["slug"]
        self.url = data["url"]
        self.desc = data["desc"]
        self.version_number = data["version_number"]
        # Log generation of an entry
        print(f"Generated entry for {self.name} {self.version_number}", flush=True)
    
    # Build the data from a toml file
    @staticmethod
    def from_toml(toml_file):
        # Log generation of an entry from a toml file
        print(f"Generating entry from toml file: {toml_file}", flush=True)
        with open(toml_file, "r") as file:
            toml_data = toml.load(file)
        # Log pulling modrinth data
        print("Pulling modrinth data", flush=True)
        mod = ModrinthMod(toml_data["update"]["modrinth"]["mod-id"], toml_data["update"]["modrinth"]["version"])
        # Log data retrieved
        print("Data retrieved from modrinth", flush=True)
        data: dict = dict()
        data["name"] = toml_data["name"]
        data["slug"] = mod.slug
        data["url"] = mod.url
        data["desc"] = mod.desc
        data["version_number"] = mod.version_number
        return ModEntryDataClass(data)
    
    # Build the data from a raw mod
    @staticmethod
    def from_raw(raw):
        with zipfile.ZipFile(raw, "r") as zip:
            with zip.open("fabric.mod.json", "r") as file:
                json_data = json.load(file)
                data: dict = dict()
                data["name"] = json_data["name"]
                data["slug"] = json_data["id"]
                data["url"] = json_data["contact"]["homepage"]
                data["desc"] = json_data["description"]
                data["version_number"] = json_data["version"]
                return ModEntryDataClass(data)
            
    def get_table_row_data(self):
        return {
            "Mod": f'<a href="{self.url}">{self.name}</a>',
            "Version": self.version_number,
            "Description": self.desc
        }
        
""" Make modlist """

# The function generate entry list parse each file of a folder and generate a list of ModEntryDataClass
# If the file is a toml file, it will use the "from_toml" method of ModEntryDataClass
# If the file is a raw mod (.jar), it will use the "from_raw" method of ModEntryDataClass
# Else it will ignore the file
def generate_entry_list(folder):
    # Log begin of generation
    print(f"Generating entry list from {folder}", flush=True)
    entry_list = []
    for file in os.listdir(folder):
        if file.endswith(".toml"):
            entry_list.append(ModEntryDataClass.from_toml(os.path.join(folder, file)))
        elif file.endswith(".jar"):
            entry_list.append(ModEntryDataClass.from_raw(os.path.join(folder, file)))
    return entry_list

# The function should init a empty dict
# Then iterate over entry list
# For each entry, if the category is not a key in the dict, add it as a key with a list containing the entry as value
# Else, append the entry to the list of the category
def generate_category_dict(entry_list):
    categories = dict()
    for entry in entry_list:
        memory = ModMemory.get_or_create(entry.slug)
        if memory["category"] not in categories.keys():
            categories[memory["category"]] = [entry]
        else:
            categories[memory["category"]].append(entry)
    return categories

# The function should iterate over the categories dict
# It should init a table dictionary, with one table per category
# Each table should contain the entries of the category
# A table is created with markdown_table and entry.get_table_row_data()
def generate_tables(categories):
    tables = defaultdict(lambda: "...")
    for category in categories.keys():
        # Get list of category entries data
        datas = []
        for entry in categories[category]:
            datas.append(entry.get_table_row_data())
        # Create table
        tables[category] = markdown_table(datas).set_params(quote=False, row_sep = 'markdown').get_markdown()
    return tables

# The function should read 'modlist/MODLIST.md' and use the content as a template
# With format, it should replace the {category} with the table of the category
# Then it should write the result in 'MODLIST.md' at the root of the project
def write_modlist(tables):
    with open("modlist/MODLIST.md", "r") as file:
        template = file.read()
    formatted = template.format_map(tables)
    with open("MODLIST.md", "w") as file:
        file.write(formatted)
        
# The function should read 'modlist/OPTIONALS.md' and use the content as a template
# With format, it should replace the {optionals} with the table of optionals mods
# It do it by iterating over the entry list and checking if the entry is optional
# If it is, add the row data to the optionals list
# Then generate the table with markdown_table and write it in 'OPTIONALS.md' at the root of the project
def write_optionals(entry_list):
    with open("modlist/OPTIONALS.md", "r") as file:
        template = file.read()
    optionals = []
    for entry in entry_list:
        memory = ModMemory.get_or_create(entry.slug)
        if memory["optional"]:
            optionals.append(entry.get_table_row_data())
    if len(optionals) == 0:
        table = "No optional mods"
    else:
        table = markdown_table(optionals).set_params(quote=False, row_sep = 'markdown').get_markdown()
    formatted = template.format(optionals=table)
    with open("OPTIONALS.md", "w") as file:
        file.write(formatted)

def run():
    mod_folder_path = " ".join(sys.argv[1:])
    mod_folder_path = mod_folder_path.removeprefix("'")
    mod_folder_path = mod_folder_path.removesuffix("'")
    ModMemory.load()
    entry_list = generate_entry_list(mod_folder_path)
    categories = generate_category_dict(entry_list)
    tables = generate_tables(categories)
    write_modlist(tables)
    write_optionals(entry_list)
    ModMemory.write()
    
if __name__ == "__main__":
    run()
    