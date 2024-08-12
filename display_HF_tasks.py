import requests
import json
import pprint

# URL to fetch tasks from Hugging Face API
url = "https://huggingface.co/api/tasks"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
else:
    print("Failed to retrieve data")
    data = None

# Function to display tasks in a readable format
def display_tasks(data):
    if data:
        for task, details in data.items():
            print(f"{task}")
            # print(f"  Label: {details.get('label', 'N/A')}")
            print(f"  Summary: {details.get('summary', 'No summary available')}")
            print(f"  YouTube ID: https://youtube.com/watch?v={details.get('youtubeId', 'N/A')}")
            # print(f"  Supported by libraries:")
            # if isinstance(details.get('libraries'), list):
            #     for library in details.get('libraries', []):
            #         if isinstance(library, dict):
            #             print(f"    - Library: {library.get('library_name', 'N/A')}")
            #             print(f"      Description: {library.get('description', 'N/A')}")
            #         else:
            #             print(f"    - Library: {library}")
            # print(f"  Demo: {details.get('demo', 'N/A')}")
            # pprint.pprint(details.get('demo'))


            # if 'datasets' in details:
            #     print("  Datasets:")
            #     for dataset in details['datasets']:
            #         print(f"    - ID: {dataset.get('id', 'N/A')}")
            #         print(f"      Description: {dataset.get('description', 'No description available')}")
            
            # if 'models' in details:
            #     print("  Models:")
            #     for model in details['models']:
            #         print(f"    - ID: {model.get('id', 'N/A')}")
            #         print(f"      Description: {model.get('description', 'No description available')}")

            print()
    else:
        print("No data to display")

# Display the tasks
display_tasks(data)

# save data to file
with open('tasks.json', 'w') as f:
    json.dump(data, f, indent=4)
