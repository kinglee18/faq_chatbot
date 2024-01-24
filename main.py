from flask import Flask, render_template, request
from dialogue_manager import *
 
 
    
app = Flask(__name__)
use_model_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
dataset_path = 'dataset.pkl'
dialogue_manager = DialogueManager(use_model_url, dataset_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(dialogue_manager.generate_answer(userText))
 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
