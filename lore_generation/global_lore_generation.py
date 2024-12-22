from utils import generate_text
import os

#Delimiters used to extract the races from the text
race_delimiter = "&&"
name_surround = "**"

#Define details of how to generate the world
start_prompt = "Write global lore for a fantasy world. The world is not called Eldoria!It should be loosely based on Tolkien with the main races being essentially humanoid. Include detailed descriptions of the races and include their home area nd a decription of it."
race_prompt = f"From the following lore text for a fantasy world, extract the major races. Return the name of the race and a description of them in a list. Use {race_delimiter} as a list delimiter.  Surround each race name with ** e.g. **Dwarves**." 

def generate_global_lore(save=True):
    """
    Generates global lore for the game world from the given prompt.
    Is suggested that the prompt defines that a set of races should be generated.
    """
    response = generate_text.generate_text(start_prompt)
    if save:
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        txt_file = "{}/../test_data/world_lore.txt".format(BASE_DIR)

        with open(txt_file, 'w') as f:
            f.write(response)

    return response

def extract_races_text(lore_text, save=True):    
    '''
    Based on the given global lore text use comprehension to extract the races
    '''

    prompt = f"{race_prompt}\n\n. {lore_text}"

    response = generate_text.generate_text(prompt)
    if save:
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        txt_file = "{}/../test_data/races_lore.txt".format(BASE_DIR)

        with open(txt_file, 'w') as f:
            f.write(response)

    return response

def extract_races(races_text):
    '''
    Returns races from given text based on the defined global delimiters
    '''
    races = []
    split_1 = races_text.split(race_delimiter)
    for race in split_1:
        split_2 = race.strip().split(name_surround)
        if len(split_2)>2:
            name = split_2[1].strip()
            description = split_2[2].strip()
            print(f"Race: {name} found with description {description}")
            races.append((name, description))
        else:
            raise Exception("Not enough races generated")  
    return races

