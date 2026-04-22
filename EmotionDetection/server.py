from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionAnalyzer")
def sent_analyzer():
    """
    Analyzes the sentiment of the input text and returns the result.
    """
    # Get the text from the UI
    text_to_analyze = request.args.get('textToAnalyze')

    # Run the detector
    response = emotion_detector(text_to_analyze)

    # If input is blank (Task 7 requirement)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the string for the UI
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)