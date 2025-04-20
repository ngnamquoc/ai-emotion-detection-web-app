"""Flask web app for Emotion Detection"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Render the homepage with input form"""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_route():
    """
    Handle GET request with textToAnalyze as query param.
    Returns emotion detection result or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted

if __name__ == "__main__":
    app.run(debug=True)
