import subprocess
import json

def query_local_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "openchat", prompt],
        stdout=subprocess.PIPE,
        text=True
    )
    return result.stdout.strip()

def parse_query(user_input):
    system_prompt = (
        "Extract query intent and details in this JSON format:\n"
        "{\n"
        "  \"intent\": \"product_search | flight_search | price_compare\",\n"
        "  \"platforms\": [\"Amazon\", \"Flipkart\", \"Skyscanner\"],\n"
        "  \"category\": \"smartphone or flight or product\",\n"
        "  \"filters\": {\"price_limit\": 30000, \"from\": \"Delhi\", \"to\": \"Dubai\"}\n"
        "}\n"
        "Query: " + user_input
    )
    response = query_local_llm(system_prompt)
    try:
        json_data = json.loads(response)
    except json.JSONDecodeError:
        print("⚠️ Could not parse JSON from model. Response:", response)
        return {}
    return json_data
