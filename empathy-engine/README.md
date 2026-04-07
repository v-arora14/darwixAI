 Empathy Engine: Emotion-Based Text-to-Speech
Project Description
The Empathy Engine is an AI-based system that converts text into speech with emotional expression. Unlike traditional text-to-speech systems, this project analyzes the sentiment of the input text and dynamically adjusts voice properties such as speed and volume to produce more human-like audio.

Working
	1. The user inputs a text string.
	2. The system analyzes the sentiment using TextBlob.
	3. The text is classified into:
	   - Positive (Happy)
	   - Negative (Sad)
	   - Neutral
	4. Based on the detected emotion, voice parameters are adjusted:
	   - Rate (speed of speech)
	   - Volume (loudness)
	5. The modified speech is generated as an audio file.

Installation & Setup

	Step 1: Clone the Repository
	Step 2: Install Dependencies
	   -pip install -r requirements.txt
	   -python -m textblob.download_corpora
	Step 3: Run the Application
	   - Enter any text when prompted.
       	   - The system will:
	   - Detect emotion
	   - Generate an audio file (`output.wav`)
	design choice
	   - Used **TextBlob** for sentiment analysis.
	   - Polarity score determines emotion:
	   - > 0.2 → Happy
	   - < -0.2 → Sad
	   - Otherwise → Neutral
For future inhancements I can build a web interface and use advance emotional models(BERT) and realistic API's
