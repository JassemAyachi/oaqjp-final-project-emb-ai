"""
Emotion Detection Server

This module provides a Flask-based web server to analyze emotions from text
using an external emotion detection package.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def emot_analyzer():
    """
    Analyzes the input text for emotions and returns the formatted response.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again."

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    response_msg = (
        f"For the given statement, the system response is "
        f"anger: {anger}, disgust: {disgust}, fear: {fear}, "
        f"joy: {joy} and sadness: {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return response_msg

@app.route("/")
def render_index_page():
    """
    Renders the default landing page (index.html template).
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
