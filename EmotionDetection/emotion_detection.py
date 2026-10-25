"""
Emotion Detection Module using IBM Watson NLP Service.
"""

import json      # CORRECTED: Added missing json import
import requests  # Import the requests library to handle HTTP requests


def emotion_detector(text_to_analyse):
    """
    Sends text to the Watson Emotion Predict API and returns a formatted dictionary
    containing individual emotion scores and the dominant emotion.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {
        "grpc-metadata-mm-model-id": (
            "emotion_aggregated-workflow_lang_en_stock"
        )
    }

    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # Check if the API request was successful (Status Code 200)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)

        # CORRECTED: Modified array index extraction to avoid structural out-of-bounds
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Extract specific emotion scores
        anger_score = emotions.get('anger', 0.0)
        disgust_score = emotions.get('disgust', 0.0)
        fear_score = emotions.get('fear', 0.0)
        joy_score = emotions.get('joy', 0.0)
        sadness_score = emotions.get('sadness', 0.0)

        # Create a dictionary dedicated to tracking the isolated emotions
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
        }

        # Logic to find the dominant emotion (key with the maximum value)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Build the required output format
        output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion,
        }
    else:
        # Fallback empty payload for non-200 responses (such as blank input 400 errors)
        output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }

    return output


# Example execution
if __name__ == "__main__":
    RESULT = emotion_detector("I am so happy I am doing this.")
    print(RESULT)



