from lore_generation import global_lore_generation
from lore_generation import starting_region_lore_generation
import os
import pytest

def test_generate_lore():
    lore = global_lore_generation.generate_global_lore()
    print(lore)
    assert(len(lore)>1000)
    races_text = global_lore_generation.extract_races_text(lore)
    assert(len(lore)>500)
    races= global_lore_generation.extract_races(races_text)
    assert(len(races) > 0)
    print(races)


def test_lore_generation_from_file():
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    lore_file = "{}/../test_data/world_lore.txt".format(BASE_DIR)
    lore_txt = ""
    with open(lore_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            lore_txt += line
    print(lore_txt) 
    assert(len(lore_txt)>1000)

    races_file = "{}/../test_data/races_lore.txt".format(BASE_DIR)
    races_txt = ""
    with open(races_file, 'r') as f:
        races_lines = f.readlines()
        for line in races_lines:
            races_txt += line
    print(races_txt)
    assert(len(races_txt)>500)
    #returns a list of tuples (name,description)
    races= global_lore_generation.extract_races(races_txt)
    assert(len(races) > 0)
    print(races)

    starting_region_file = "{}/../test_data/starting_region_lore.txt".format(BASE_DIR)
    starting_region_txt = ""
    with open(starting_region_file, 'r') as f:
        region_lines = f.readlines()
        for line in region_lines:
            starting_region_txt += line
    print(starting_region_txt)




