import os
import inquirer
from lib.createRelation import relation_between_files, relation_between_texts 
from lib.getText import get_text_from_xml
from lib.gen_anki import generate_anki_deck

folder_path = '/root/main/Subtitles/'

# List all files in the folder
serie = os.listdir(folder_path)
# Prompt to select a folder
questions = [
    inquirer.List('folder',
                  message='Select a Serie:',
                  choices=serie,
              ),
]

selected_serie = inquirer.prompt(questions)['folder']


season = os.listdir(f"{folder_path}/{selected_serie}")
# Prompt to select a folder
questions = [
    inquirer.List('folder',
                  message='Select a Season:',
                  choices=season,
              ),
]

selected_season = inquirer.prompt(questions)['folder']

# Print the selected folder
path_season = f"{folder_path}/{selected_serie}/{selected_season}"
subtitles = os.listdir(path_season)

relational_files = relation_between_files(subtitles)

for rel in relational_files:
    eng = get_text_from_xml(f"{path_season}/{relational_files[rel][0]}")
    pt = get_text_from_xml(f"{path_season}/{relational_files[rel][1]}")
    rela = relation_between_texts(eng, pt)
    generate_anki_deck(rela, selected_season, rel)