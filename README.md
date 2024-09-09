# Zoho Cliq Audio Summarizer

This extension captures audio from Zoho Cliq meetings and provides a summarized version of the conversation.

## Setup

1. **Backend Setup**
   - Install Python dependencies:
     ```bash
     pip install -r backend/requirements.txt
     ```
   - Create a `.env` file in the `backend/` directory with your AssemblyAI and Gemini API keys:
     ```
     ASSEMBLYAI_API_KEY=your_assemblyai_api_key
     GENAI_API_KEY=your_genai_api_key
     ```

2. **Frontend Setup**
   - Open the `frontend/manifest.json` file and update permissions if necessary.
   - Load the extension into your browser's developer mode.

3. **Running the Backend**
   - Start the Flask server:
     ```bash
     python backend/app.py
     ```

## Usage

- Click the extension icon in Zoho Cliq to open the popup.
- Click "Start Transcription" to transcribe the audio.
- View the summary and ask questions about the transcribed text.
