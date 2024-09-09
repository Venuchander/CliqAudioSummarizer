from flask import Flask, request, jsonify
import assemblyai as aai
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()


aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    audio_url = request.json.get('audio_url')
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_url)
    text = transcript.text
    return jsonify({"text": text})

@app.route('/summarize', methods=['POST'])
def summarize_text():
    text = request.json.get('text')
    model = genai.GenerativeModel('gemini-pro')
    summary_prompt = f"Summarize the following text: {text}"
    summary = model.generate_content(summary_prompt).text
    return jsonify({"summary": summary})

@app.route('/ask', methods=['POST'])
def ask_question():
    text = request.json.get('text')
    question = request.json.get('question')
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Answer the following question based on the text: '{text}'. Question: {question}"
    answer = model.generate_content(prompt).text
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(port=5000)
