# NLP Emotion Detection Web App

## Overview
This project is a web application for detecting emotions in text using Natural Language Processing (NLP). It provides a user-friendly interface where users can input text and receive an analysis of the emotions present, including the dominant emotion.

## Features
- Detects emotions such as joy, anger, sadness, fear, and disgust.
- Provides a web-based interface for user interaction.
- Uses Flask for the backend and a pre-trained NLP model for emotion detection.
- Includes unit tests to ensure the accuracy of emotion detection.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Emotion Detection**: Pre-trained NLP model via IBM Watson API
- **Testing**: Python's unittest module
- **HTTP Requests**: Python's requests library

## Prerequisites
- Python 3.8 or higher
- Flask
- Requests library

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/ngnamquoc/ai-emotion-detection-web-app.git
   cd ai-emotion-detection-web-app
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   flask --app server --debug run
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000` to access the web app.

## Usage
1. Enter the text you want to analyze in the input field on the homepage.
2. Click the "Run Sentiment Analysis" button.
3. View the detected emotions and the dominant emotion in the results section.

![Demo picture](/static/images/6b_deployment_test.png "Demo picture")

## Testing
Run the unit tests to verify the functionality:
```bash
python -m unittest test_emotion_detection.py
```

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- IBM Developer Skills Network for providing the pre-trained emotion detection model.
- Flask and Bootstrap for enabling rapid web development.
