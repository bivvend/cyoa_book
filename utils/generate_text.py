import openai
import json
import os

# Writing guidelines for the AI
writing_guidelines = ("You are a creative writer generating detailed game lore. "
                      "You will be asked to return JSON structure sometimes, if so "
                      "ALWAYS use  double quotes \"\" around strings, never single \'\' " 
                      )


# Initialize the OpenAI client
client = openai.OpenAI(
    # Retrieve the OpenAI API key from an environment variable
    #api_key=os.getenv("OPENAI_API_KEY")
)

def generate_text(prompt, max_tokens=5000, temperature=0.7, model_in = "gpt-4o-mini"):
    """
    Generic function to generate text using OpenAI's ChatGPT API.
    
    Parameters:
    - prompt (str): The prompt to send to the API.
    - max_tokens (int): The maximum number of tokens to generate.
    - temperature (float): The sampling temperature to use.
    
    Returns:
    - str: The generated text from the API.
    """
    try:
        # Create a completion request to the OpenAI API
        completion = client.chat.completions.create(
            model=model_in,  # Specify the model to use
            store=False,  # Store the completion for future reference
            max_tokens=max_tokens,  # Set the maximum number of tokens to generate
            temperature=temperature,  # Set the sampling temperature
            messages=[
                {"role": "user", "content": f"{writing_guidelines}\n\n. {prompt}"}
            ]  # Include the writing guidelines and prompt in the message
        )

        # Return the generated text from the completion
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error in generate_text: {e}")
        return None

def critique_text(prompt, max_tokens=5000, temperature=1.1, model_in = "gpt-4o-mini"):
    """
    Generic function to comment on structures using OpenAI's ChatGPT API.
    
    Parameters:
    - prompt (str): The prompt to send to the API.
    - max_tokens (int): The maximum number of tokens to generate.
    - temperature (float): The sampling temperature to use.
    
    Returns:
    - str: The generated text from the API.
    """
    try:
        if model_in == "o1-mini":
            completion = client.chat.completions.create(
                model=model_in,  # Specify the model to use
                store=False,  # Store the completion for future reference
                max_completion_tokens=max_tokens,  # Set the maximum number of tokens to generate
                messages=[
                    {"role": "user", "content": f"{prompt}"}
                ]  # Include the writing guidelines and prompt in the message
            )
        else:

            # Create a completion request to the OpenAI API
            completion = client.chat.completions.create(
                model=model_in,  # Specify the model to use
                store=False,  # Store the completion for future reference
                max_tokens=max_tokens,  # Set the maximum number of tokens to generate
                temperature=temperature,  # Set the sampling temperature
                messages=[
                    {"role": "user", "content": f"{prompt}"}
                ]  # Include the writing guidelines and prompt in the message
            )
        
        # Return the generated text from the completion
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error in generate_text: {e}")
        return None