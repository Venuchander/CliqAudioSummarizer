import unittest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from backend import app  

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  
        self.app.testing = True

    def test_transcribe_audio(self):
        response = self.app.post('/transcribe', json={'audio_url': 'https://storage.googleapis.com/aai-web-samples/news.mp4'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('text', response.json)

    def test_summarize_text(self):
        response = self.app.post('/summarize', json={'text': 'Sample text to summarize.'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('summary', response.json)

    def test_ask_question(self):
        response = self.app.post('/ask', json={'text': 'Sample text for question answering.', 'question': 'What is this?'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('answer', response.json)

if __name__ == '__main__':
    unittest.main()
