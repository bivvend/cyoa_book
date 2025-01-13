import os
import json
import pytest
import utils.agent as agent

# Tests assume that the Assistant and vector store below have been setup and 
# the file list uploaded.
# Also that the thread is running

@pytest.fixture
def vector_store_id():
    return "vs_3P44d1OPCLJPumcl7Yc8kVIa"

@pytest.fixture
def assistant_id():
    return "asst_rLhqNkUB77vU3Pfavd3HeChr"

@pytest.fixture
def thread_id():
    return "thread_nvJfWjlC7RFFuUNiUZDTY45G"

@pytest.fixture
def load_intro_text():
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    intro = "{}/../test_data/events/intro.txt".format(BASE_DIR)
    intro_txt = ""
    with open(intro, 'r') as f:
        lines = f.readlines()
        for line in lines:
            intro_txt += line
    return intro_txt

@pytest.fixture
def load_events():
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    events = "{}/../test_data/events/all_events.txt".format(BASE_DIR)
    events_txt = ""
    with open(events, 'r') as f:
        lines = f.readlines()
        for line in lines:
            events_txt += line
    events_json =json.loads(events_txt)
    assert events_json is not None
    return events_json

@pytest.fixture
def load_region_lore():
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    start_region_file = "{}/../test_data/starting_region_lore.txt".format(BASE_DIR)
    region_lore_txt = ""
    with open(start_region_file, 'r') as f:
        lore_lines = f.readlines()
        for line in lore_lines:
            region_lore_txt += line
    region_lore_json = json.loads(region_lore_txt)
    assert region_lore_json is not None
    return region_lore_json

def test_write_events(load_intro_text, load_region_lore, load_events, assistant_id, thread_id, vector_store_id):
    intro_txt = load_intro_text
    region_lore_json = load_region_lore

    areas = region_lore_json["starting_area"]["notable_locations"]
    print(f"Number of areas = {len(areas)}")

    all_events_json = load_events
    
    
    # Load all the events json and count number of events per region
    for area in areas:
        print(area["name"])
        print(f"Number of events in {area["name"]} = {len(all_events_json[area["name"]]["events"])}")
    # Give the assistant the intro and tell to generate event 1 + a scene to link to event 2
    writing_guide_line_1 = (
        "The previous scene in the story is given below: \n\n"
        f"{intro_txt} \n\n"

        "Write a scene for the next event in the series described by the JSON below: \n\n"
        f"{all_events_json[areas[0]["name"]]["events"][0]} \n\n"
        "You must not add anything other than what is described in the event JSON. "
        "In the description link the scene with the previous scene. "                 

    )

    writing_guide_line_2 = (
        f"Where possible add a converstion from \"conversations.txt\" during the event. \n"
        f"The description should not be too dramatic and does not need to end with a heroic line of what may come next.  It is a description in the middle of a story."
        f"Only include utf-8 characters in the response. \n"
    )

    print(f"Generating link from intro and {areas[0]["name"]} {all_events_json[areas[0]["name"]]["events"][0]["id"]} ")
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))

    message = agent.create_message(writing_guide_line_1 + writing_guide_line_2, thread_id)
    assert message is not None
    response = agent.start_run(thread_id, assistant_id)
    assert response is not None
    print(response)

    agent.delete_messages(thread_id)

    
    file_path = f"{BASE_DIR}/../test_data/story_chunks/area_1_{all_events_json[areas[0]["name"]]["events"][0]["id"]}.txt"
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(response)
    area_count = 0
    for area in areas[0:1]:
        event_count = 0
        
        for event in  all_events_json[areas[0]["name"]]["events"]:
            if area_count == 1 and event_count ==1: #Skip link to intro
                pass
            else:
                file_path = f"{BASE_DIR}/../test_data/story_chunks/area_{area_count+1}_event_{event_count+1}.txt"
                print(file_path)

                print(f"Writing event {event_count+1}...")

                writing_guide_line_1 = (
                    "The previous scene in the story is given below: \n\n"
                    f"{response} \n\n"

                    "Write a scene for the next event in the series described by the JSON below: \n\n"
                    f"{all_events_json[area["name"]]["events"][event_count]} \n\n"
                    "You must not add anything other than what is described in the event JSON. "
                    "In the description link the scene with the previous scene. "                 

                )

                writing_guide_line_2 = (
                    f"Where possible add a converstion from \"conversations.txt\" during the event. \n"
                    f"The description should not be too dramatic and does not need to end with a heroic line of what may come next.  It is a description in the middle of a story."
                    f"Only include utf-8 characters in the response. \n"
                )

                print(writing_guide_line_1 + "\n" + writing_guide_line_2)

                message = agent.create_message(writing_guide_line_1 + "\n" + writing_guide_line_2, thread_id)
                assert message is not None
                response = agent.start_run(thread_id, assistant_id)
                assert response is not None
                #print(response)

                with open(file_path, 'w', encoding="utf-8") as f:
                    f.write(response)

                agent.delete_messages(thread_id)

            event_count += 1
        area_count += 1 
