import requests

api_key = "API_KEY"
endpoint = "https://api.openai.com/v1/completions"

prompt = "o que é uma api?"
model = "text-davinci-003"

data = {
    "prompt": prompt,
    "model": model,
    "max_tokens": 100,
    "temperature" : 0
}

response = requests.post(endpoint, json=data, headers={
    "Content-Type": "application/json",
    "Authorization" : f"Bearer {api_key}"

})

print(response.json())