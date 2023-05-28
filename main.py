import os
import inquirer
folder_path = '/root/main/Subtitles/Better Call Saul'

# List all files in the folder
seasons = os.listdir(folder_path)
# Prompt to select a folder
questions = [
    inquirer.List('folder',
                  message='Select a folder:',
                  choices=seasons,
              ),
]

answer = inquirer.prompt(questions)
selected_folder = answer['folder']

# Print the selected folder
subtitles = os.listdir(f"{folder_path}/{selected_folder}")

relationships = {}

for name in subtitles:
    common_part = name[0:4]  # Extract the common part of the name
    
    if common_part not in relationships:
        relationships[common_part] = []
    
    relationships[common_part].append(name)

# Print the relationships
for key, value in relationships.items():
    print(value)
