import os
import utils.agent as agent
import openai

# TTD file not meant to be run in entirety.
# Instructions for the creative writer agent
instructions = ("You are a creative writer generating beautiful, well written fantasy stories. "
                "You will be given JSON files containing the story's plot, characters, events and setting. "
                "You will create sections of the story for a given range of events in the JSON file. "
                "You will try and keep the content consistent throughout the story by analysis the previous events. ")

# IDs for vector store, assistant, and test file
vector_store_id = "vs_3P44d1OPCLJPumcl7Yc8kVIa"
assistant_id = "asst_rLhqNkUB77vU3Pfavd3HeChr"
file_for_test = "file-KpqbmL6XU1hxz7FjiLS9Hc"

# List of files to be used in tests
files_list = ["../test_data/characters/conversations.txt",
              "../test_data/characters/enemy.txt", 
              "../test_data/characters/party.txt",  
              "../test_data/events/all_events.txt",
              "../test_data/starting_region_lore.txt", 
              "../test_data/world_lore.txt",           
              ]

# Thread ID for testing purposes
thread_id = "thread_nvJfWjlC7RFFuUNiUZDTY45G"

def test_create_vector_store():
    '''
    Create a new vector store.
    '''
    vector_store_id = agent.create_vector_store("Fantasy story vector store").id
    assert vector_store_id is not None
    print(vector_store_id)

def test_create_author():
    '''
    Create a new author with the given instructions.
    '''
    author = agent.create_author("Fantasy story author", instructions, vector_store_id)
    assert author is not None
    print(author.id)

def test_retrieve_author():
    '''
    Retrieve an existing author by ID.
    '''
    author = agent.retrieve_author(assistant_id)
    assert author is not None
    print(author.id)

def test_retrieve_vector_store():
    '''
    Retrieve an existing vector store by ID.
    '''
    vector_store = agent.retrieve_vector_store(vector_store_id)
    assert vector_store is not None
    print(vector_store.id)

def test_modify_author_instructions():
    '''
    Modify the instructions for an existing author.
    '''
    author = agent.modify_author_instructions(assistant_id, instructions)
    assert author is not None
    print(author.id)

def test_upload_file():
    '''
    Upload a file to the agent.
    '''
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    txt_file = f"{BASE_DIR}/../test_data/characters/conversations.txt"
    file = agent.upload_file(txt_file)
    assert file is not None
    print(file.id)

def test_list_files():
    '''
    List all files using the agent.
    '''
    files = agent.list_files()
    assert files is not None
    print(files.data)  

def test_retrieve_file():
    '''
    Retrieve a specific file using the agent.
    '''
    file = agent.retrieve_file(file_for_test)
    assert file is not None
    print(file.filename) 

def test_add_file_to_vector_store():
    '''
    Add a file to the vector store.
    '''
    file = agent.retrieve_file(file_for_test)
    assert file is not None

    vector_store = agent.retrieve_vector_store(vector_store_id)
    assert vector_store is not None

    agent.add_file_to_vector_store(vector_store_id, file_for_test)

def test_add_all_files():
    '''
    Adds all the files to the API and then adds them to the vector store.
    '''
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    uploaded_file_id_list = []
    for f in files_list:
        file = None
        full_path = f"{BASE_DIR}/{f}"
        file = agent.upload_file(full_path)
        assert file is not None
        uploaded_file_id_list.append(file.id)
    for f in uploaded_file_id_list:
        agent.add_file_to_vector_store(vector_store_id, f)

def test_create_thread():
    '''
    Create a new thread.
    '''
    thread = agent.create_thread()
    assert thread is not None
    print(thread.id)

def test_retrieve_thread():
    '''
    Retrieve an existing thread by ID.
    '''
    thread = agent.retrieve_thread(thread_id)
    assert thread is not None
    print(thread.id)

def test_create_message_on_thread():
    '''
    Create a new message on an existing thread.
    '''
    message = agent.create_message("Write an intro paragraph to the story", thread_id)
    assert message is not None

def test_retrieve_messages():
    '''
    Retrieve all messages from a thread.
    '''
    messages = agent.retrieve_messages(thread_id)
    assert messages is not None
    for m in messages.data:
        print(m.content)

def test_delete_messages():
    '''
    Delete all messages from a thread.
    '''
    response = agent.delete_messages(thread_id)
    assert response is not None
    messages = agent.retrieve_messages(thread_id)
    assert messages is not None
    assert len(messages.data) == 0

def test_run_message():
    '''
    Create a new message and run it.
    '''
    message = agent.create_message("Write an intro paragraph to the story", thread_id)
    assert message is not None
    response = agent.start_run(thread_id, assistant_id)
    assert response is not None
    print(response)
