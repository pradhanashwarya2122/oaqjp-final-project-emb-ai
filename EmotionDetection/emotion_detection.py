"""
This module provides a function to perform sentiment analysis using
the Watson NLP Library.
"""
import json
import requests

def emotion_detector(text_to_analyse):
    """
    Analyze the sentiment of the given text using Watson NLP Library.

    Args:
        text_to_analyse (str): The text to analyze.

    Returns:
        dict: The sentiment analysis result containing label and score.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers, timeout=10)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotion_result = formatted_response['emotionPredictions'][0]['emotion']
        anger = emotion_result['anger']
        disgust = emotion_result['disgust']
        fear = emotion_result['fear']
        joy = emotion_result['joy']
        sadness = emotion_result['sadness']
        dominant_emotion = max(emotion_result, key=emotion_result.get)
        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion
        }
        
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion
        }
    return {"dominant_emotion": None}
