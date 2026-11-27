from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://az901-learningre.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.1-srinath"
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

response = client.responses.create(
    model=deployment_name,
    # instructions="You are an AI assistant that helps people find information.",
    # input="Can you please tell me something about Microsoft Foundry?",
    input=[
        {
            "role": "system",
            "content": "You are an AI assistant that helps people find information."
        },
        {
            "role": "user",
            "content": "Can you please tell me something about Microsoft Foundry?"
        }
    ],
    temperature=0.7,
    max_output_tokens=1000
)

print(f"answer: {response.output[0]}")