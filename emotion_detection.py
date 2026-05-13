import requests
import json

def emotion_detector(text_to_analyze):
    # Watson NLP Emotion Predict endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Required headers
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Input JSON payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send POST request
    response = requests.post(url, headers=headers, json=payload)

    # Convert response to JSON
    result = response.json()

    # Return the 'text' attribute from the response
    return result.get("text", None)


if __name__ == "__main__":
    sample_text = "I am feeling very happy today!"
    print(emotion_detector(sample_text))
