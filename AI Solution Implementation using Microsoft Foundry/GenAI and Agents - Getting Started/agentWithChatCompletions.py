# Before running the sample:
#    pip install "azure-ai-projects>=2.1.0"

# Import the Azure authentication and Foundry project SDK classes used below.
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Define the Foundry project endpoint and the agent to invoke.
endpoint = "https://az901-learningre.services.ai.azure.com/api/projects/az901-mf-learning-proj"
agent_name = "srinath-chat-agent"
# Define the message sent to the agent on this run.
user_message = "Hi srinath-chat-agent"

# Create and automatically close the Azure credential and project client contexts.
with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint,
        credential=credential,
        allow_preview=True,
    ) as project_client,
):
    # Get the OpenAI-compatible client configured for the selected Foundry agent.
    openai_client = project_client.get_openai_client(agent_name=agent_name)

    # Create a conversation so this Responses API request is associated with chat state.
    # Preview agents require a conversation for every turn.
    conversation = openai_client.conversations.create()

    # Send the user message and generate the agent's response in this conversation.
    response = openai_client.responses.create(
        conversation=conversation.id,
        input=[{"role": "user", "content": user_message}],
        extra_body={
            "agent_reference": {"agent_name": agent_name, "type": "agent_reference"}
        }
    )

    # Print the combined text output returned by the agent.
    print(f"Response output: {response.output_text}")