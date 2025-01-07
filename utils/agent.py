from openai import OpenAI
client = OpenAI()

def create_author(name, instructions, vector_store_id):
    author = client.beta.assistants.create(
        instructions= instructions,
        name=name,
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
        model="gpt-4o"
    )
    return author

def modify_author_instructions(author_id, instructions):
    author = client.beta.assistants.update(
        author_id,
        instructions=instructions
    )
    return author

def create_vector_store(name):
    vector_store = client.beta.vector_stores.create(
        name=name,

    )
    return vector_store

def retrieve_author(author_id):
    author = client.beta.assistants.retrieve(author_id)
    return author   

def retrieve_vector_store(vector_store_id):
    vector_store = client.beta.vector_stores.retrieve(vector_store_id)
    return vector_store

def upload_file(file_path):
    file = client.files.create(file=open(file_path, 'rb'), purpose="assistants")
    return file

def list_files():
    files = client.files.list()
    return files

def retrieve_file(file_id):
    file = client.files.retrieve(file_id)
    return file

def add_file_to_vector_store(vector_store_id, file_id):
    vector_store = client.beta.vector_stores.retrieve(vector_store_id)
    client.beta.vector_stores.files.create(
        vector_store_id=vector_store_id,
        file_id=file_id) 
    return vector_store

def create_thread():
    thread = client.beta.threads.create()
    return thread

def retrieve_thread(thread_id):
    thread = client.beta.threads.retrieve(thread_id)
    return thread

def create_message(prompt, thread_id):
    thread_message = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=prompt,
    )
    return thread_message

def retrieve_messages(thread_id):
    thread_messages = client.beta.threads.messages.list(thread_id)
    return thread_messages

def delete_messages(thread_id):
    thread_messages = client.beta.threads.messages.list(thread_id)
    for m in thread_messages:
        client.beta.threads.messages.delete(m.id, thread_id=thread_id)
    thread_messages = client.beta.threads.messages.list(thread_id)
    return thread_messages
