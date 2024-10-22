import requests
import Constants

Exludeurl = Constants.Exludeurlsapi
headers =  Constants.ExcludeurlHeader
payload = {}
def CpalGetExURL():
    response = requests.request("GET", Exludeurl, headers = headers, data = payload)
    print("-----response", response.text)
    return response.text
# x = CpalGetExURL()
# print("response iss--------", x)



# def CpalGetExURL():
#     requests.get()

# # Define the API endpoint and your API key
# api_endpoint = "https://api.copilotstudio.com/v1/prompts"
# api_key = "your_api_key_here"

# # Define the prompt data
# prompt_data = {
#     "title": "Sample Prompt",
#     "description": "This is a sample prompt for Copilot Studio.",
#     "content": "Write a Python script to add prompts to Copilot Studio."
# }

# # Set up the headers with your API key
# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# # Make the POST request to add the prompt
# response = requests.post(api_endpoint, json=prompt_data, headers=headers)

# # Check the response status
# if response.status_code == 201:
#     print("Prompt added successfully!")
# else:
#     print(f"Failed to add prompt. Status code: {response.status_code}")
#     print(response.json())
