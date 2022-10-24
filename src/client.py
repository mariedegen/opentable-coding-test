import json

import requests

if __name__ == "__main__":
    headers = {'Content-type': 'application/json'}

    result1 = requests.get("http://127.0.0.1:5000/embeddings", "sentence=the+quick+brown+fox")
    print(f"Q1: Status Code {result1.status_code}. Response:")
    print(json.dumps(result1.json()))

    with open('data/payload_2.json', 'r') as f:
        payload_2 = json.load(f)

    result2 = requests.post("http://127.0.0.1:5000/embeddings/bulk", json=payload_2, headers=headers)
    print(f"Q2: Status Code {result2.status_code}. Response:")
    print(json.dumps(result2.json()))

    with open('data/payload_3.json', 'r') as f:
        payload_3 = json.load(f)

    result3 = requests.post("http://127.0.0.1:5000/embeddings/similarity", json=payload_3, headers=headers)
    print(f"Q3: Status Code {result3.status_code}. Response:")
    print(json.dumps(result3.json()))
