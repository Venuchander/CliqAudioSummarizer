document.getElementById('start').addEventListener('click', async () => {
    const response = await fetch('http://localhost:5000/transcribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ audio_url: 'YOUR_AUDIO_URL_HERE' }) // Replace with actual audio URL
    });
    const result = await response.json();
    document.getElementById('transcript').value = result.text;

    // Automatically summarize the transcribed text
    const summaryResponse = await fetch('http://localhost:5000/summarize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: result.text })
    });
    const summaryResult = await summaryResponse.json();
    document.getElementById('summary').value = summaryResult.summary;
});

document.getElementById('askQuestion').addEventListener('click', async () => {
    const transcript = document.getElementById('transcript').value;
    const question = document.getElementById('question').value;

    const answerResponse = await fetch('http://localhost:5000/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: transcript, question: question })
    });
    const answerResult = await answerResponse.json();
    document.getElementById('answer').value = answerResult.answer;
});
