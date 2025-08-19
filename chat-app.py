import os
from dotenv import load_dotenv

# Add references
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        project_endpoint = os.getenv("PROJECT_ENDPOINT")
        model_deployment =  os.getenv("MODEL_DEPLOYMENT")
        api_key = os.getenv("API_KEY")

        # Get a chat client
        client = ChatCompletionsClient(
            endpoint=project_endpoint, 
            credential=AzureKeyCredential(api_key)
        )

        # Initialize prompt with system message
        prompt = [
            {"role": "system", "content": "You are a Sales AI assistant that helps customers buy makeup, shoes, clothes and electronics."}
        ] 

        # Loop until the user types 'quit'
        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
            
             # Add user message to conversation
            prompt.append({"role": "user", "content": input_text})

            # Get a chat completion
            response = client.complete(
                model=model_deployment,
                messages=prompt
            )

            # Extract assistant message
            completion = response.choices[0].message["content"]
            print("Assistant:", completion)
            
            # Append assistant's reply for multi-turn context
            prompt.append({"role": "assistant", "content": completion})

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()
