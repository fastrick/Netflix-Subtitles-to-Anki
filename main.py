import os
import inquirer
from lib.createRelation import relation_between_files, relation_between_texts 
from lib.getText import get_text_from_xml
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

relational_files = relation_between_files(subtitles)

for rel in relational_files:
    sub0 = relational_files[rel][0]
    sub1 = relational_files[rel][1]
    #print(f"Comparing {sub0} with {sub1}")
    eng = get_text_from_xml(f"{folder_path}/{selected_folder}/{relational_files[rel][0]}")
    pt = get_text_from_xml(f"{folder_path}/{selected_folder}/{relational_files[rel][1]}")
    rela = relation_between_texts(eng, pt)
    if len(rela) < 30:
        print(f"N texts: {len(rela)} {sub0} and {sub1} are not the same")
        print(rela)
    #subtitle = get_text_from_xml(f"{folder_path}/{selected_folder}/{relational_files[rel][1]}")
    #print(subtitle)