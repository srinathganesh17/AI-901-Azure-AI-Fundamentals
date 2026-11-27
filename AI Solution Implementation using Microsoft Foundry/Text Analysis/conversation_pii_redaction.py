from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

key = "<your-api-key>"
endpoint = "https://az901-learningre.cognitiveservices.azure.com/"

# Authenticate the client using your key and endpoint
client = ConversationAnalysisClient(endpoint, AzureKeyCredential(key))

# Example method for detecting PII from conversations
def conversation_pii_example(client):
    conversations = {
        "displayName": "Conversation PII Analysis",
        "analysisInput": {
            "conversations": [
                {
                    "id": "1",
                    "language": "en",
                    "modality": "text",
                    "conversationItems": [
                        {
                            "participantId": "Agent",
                            "id": "1",
                            "text": "$documents"
                        }
                    ]
                }
            ]
        },
        "tasks": [
            {
                "taskName": "ConversationalPIITask",
                "kind": "ConversationalPIITask",
                "parameters": {
                    "redactionSource": "text",
                    "piiCategories": [
                        "All"
                    ]
                }
            }
        ]
    }

    poller = client.begin_conversation_analysis(conversations)
    result = poller.result()
    task_result = result["tasks"]["items"][0]
    conv_result = task_result["results"]["conversations"][0]

    for item in conv_result["conversationItems"]:
        print("Redacted Text: {}".format(item["redactedContent"]["text"]))
        for entity in item["entities"]:
            print("Entity: {}".format(entity["text"]))
            print("\tCategory: {}".format(entity["category"]))
            print("\tConfidence Score: {}".format(entity["confidenceScore"]))
            print("\tOffset: {}".format(entity["offset"]))
            print("\tLength: {}".format(entity["length"]))

conversation_pii_example(client)
