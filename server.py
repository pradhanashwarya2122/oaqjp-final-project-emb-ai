''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    stored_text = emotion_detector(text_to_analyze)
    if stored_text['dominant_emotion'] is not None:
        anger = stored_text['anger']
        disgust = stored_text['disgust']
        fear = stored_text['fear']
        joy = stored_text['joy']
        sadness = stored_text['sadness']
        dominant_emotion = stored_text['dominant_emotion']
        return f"For the given statement, the system response is "\
            f"'anger': {anger}, 'disgust': {disgust}, "\
            f"'fear': {fear}, 'joy': {joy} and "\
            f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
