import json
import os
import utils.agent as agent

#Tests assume that the Assistant and vector store below have been setup and 
#the file list uploaded.
#Also that the thread is running
vector_store_id = "vs_3P44d1OPCLJPumcl7Yc8kVIa"
assistant_id = "asst_rLhqNkUB77vU3Pfavd3HeChr"
thread_id = "thread_nvJfWjlC7RFFuUNiUZDTY45G"


         
def test_write_events():
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    #Load the intro text
    intro = "{}/../test_data/events/intro.txt".format(BASE_DIR)
    intro_txt = ""
    with open(intro, 'r') as f:
        lines = f.readlines()
        for line in lines:
            intro_txt += line

    #Load the region json and extract name of first region
    start_region_file = "{}/../test_data/starting_region_lore.txt".format(BASE_DIR)
    region_lore_txt = ""
    with open(start_region_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            region_lore_txt += line
    region_lore_json = json.loads(region_lore_txt)
    assert region_lore_json is not None
    
    
    #Load all the events json and count number of events per region

    #Give the assistant the intro and tell to generate event 1 + a scene to link to event 2

    #Based on event_1 + link  generate event_2 + link
    #repeat for N events

    pass