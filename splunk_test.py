import requests
import json

# Define your Splunk HEC endpoint URL and token
splunk_hec_url = "https://YOUR_SPLUNK_HEC_URL"
splunk_hec_token = "YOUR_HEC_TOKEN"

# Define the event (message) you want to send
event_data = {
    "event": "Your message content"
}

# Convert the event data to JSON format
payload = json.dumps(event_data)

# Set the headers with authorization and content-type
headers = {
    "Authorization": f"Splunk {splunk_hec_token}",
    "Content-Type": "application/json"
}

# Send the POST request to Splunk HEC endpoint
response = requests.post(splunk_hec_url, headers=headers, data=payload, verify=False)

# Check the response
if response.status_code == 200:
    print("Message sent successfully to Splunk.")
else:
    print(f"Failed to send message. Status code: {response.status_code}")
    print(response.text)
