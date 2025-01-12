from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

def create_author(name, instructions, vector_store_id):
    """
    Create a new author with the given instructions and vector store ID.
    """
    try:
        author = client.beta.assistants.create(
            instructions=instructions,
            name=name,
            tools=[{"type": "file_search"}],
            tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
            model="gpt-4o"
        )
        return author
    except Exception as e:
        print(f"Error in create_author: {e}")
        return None

def modify_author_instructions(author_id, instructions):
    """
    Modify the instructions for an existing author.
    """
    try:
        author = client.beta.assistants.update(
            author_id,
            instructions=instructions
        )
        return author
    except Exception as e:
        print(f"Error in modify_author_instructions: {e}")
        return None

def create_vector_store(name):
    """
    Create a new vector store with the given name.
    """
    try:
        vector_store = client.beta.vector_stores.create(
            name=name,
        )
        return vector_store
    except Exception as e:
        print(f"Error in create_vector_store: {e}")
        return None

def retrieve_author(author_id):
    """
    Retrieve an existing author by ID.
    """
    try:
        author = client.beta.assistants.retrieve(author_id)
        return author
    except Exception as e:
        print(f"Error in retrieve_author: {e}")
        return None

def retrieve_vector_store(vector_store_id):
    """
    Retrieve an existing vector store by ID.
    """
    try:
        vector_store = client.beta.vector_stores.retrieve(vector_store_id)
        return vector_store
    except Exception as e:
        print(f"Error in retrieve_vector_store: {e}")
        return None

def upload_file(file_path):
    """
    Upload a file to the OpenAI API.
    """
    try:
        file = client.files.create(file=open(file_path, 'rb'), purpose="assistants")
        return file
    except Exception as e:
        print(f"Error in upload_file: {e}")
        return None

def list_files():
    """
    List all files uploaded to the OpenAI API.
    """
    try:
        files = client.files.list()
        return files
    except Exception as e:
        print(f"Error in list_files: {e}")
        return None

def retrieve_file(file_id):
    """
    Retrieve a specific file by ID from the OpenAI API.
    """
    try:
        file = client.files.retrieve(file_id)
        return file
    except Exception as e:
        print(f"Error in retrieve_file: {e}")
        return None

def add_file_to_vector_store(vector_store_id, file_id):
    """
    Add a file to a vector store.
    """
    try:
        vector_store = client.beta.vector_stores.retrieve(vector_store_id)
        client.beta.vector_stores.files.create(
            vector_store_id=vector_store_id,
            file_id=file_id
        )
        return vector_store
    except Exception as e:
        print(f"Error in add_file_to_vector_store: {e}")
        return None

def create_thread():
    """
    Create a new thread.
    """
    try:
        thread = client.beta.threads.create()
        return thread
    except Exception as e:
        print(f"Error in create_thread: {e}")
        return None

def retrieve_thread(thread_id):
    """
    Retrieve an existing thread by ID.
    """
    try:
        thread = client.beta.threads.retrieve(thread_id)
        return thread
    except Exception as e:
        print(f"Error in retrieve_thread: {e}")
        return None

def create_message(prompt, thread_id):
    """
    Create a new message on an existing thread.
    """
    try:
        thread_message = client.beta.threads.messages.create(
            thread_id,
            role="user",
            content=prompt,
        )
        return thread_message
    except Exception as e:
        print(f"Error in create_message: {e}")
        return None

def retrieve_messages(thread_id):
    """
    Retrieve all messages from a thread.
    """
    try:
        thread_messages = client.beta.threads.messages.list(thread_id)
        return thread_messages
    except Exception as e:
        print(f"Error in retrieve_messages: {e}")
        return None

def delete_messages(thread_id):
    """
    Delete all messages from a thread.
    """
    try:
        thread_messages = client.beta.threads.messages.list(thread_id)
        for m in thread_messages:
            client.beta.threads.messages.delete(m.id, thread_id=thread_id)
        thread_messages = client.beta.threads.messages.list(thread_id)
        return thread_messages
    except Exception as e:
        print(f"Error in delete_messages: {e}")
        return None

def start_run(thread_id, assistant_id):
    """
    Start a run on a thread with a specific assistant.
    """
    try:
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread_id,
            assistant_id=assistant_id,
        )
        print("Run completed with status: " + run.status)
        output = None
        if run.status == "completed":
            messages = client.beta.threads.messages.list(thread_id=thread_id)
            # Last message will be the first
            if len(messages.data) > 0:
                output = messages.data[0].content[0].text.value
        return output
    except Exception as e:
        print(f"Error in start_run: {e}")
        return None
