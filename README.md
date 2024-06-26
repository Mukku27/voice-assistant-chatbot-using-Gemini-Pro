# Voice Assistant with Google Generative AI

This project is a voice-controlled assistant that uses Streamlit for the web interface, Google's Generative AI for generating responses, and various Python libraries for speech synthesis and recognition. The assistant can listen to user input, process it through a generative AI model, and respond both in text and spoken form. 

## Features

- **Voice Interaction**: Users can speak their requests, and the assistant will respond using synthesized speech.
- **Google Generative AI**: The assistant uses Google's Generative AI to generate responses to user queries.
- **Logging**: All interactions are logged into a text file for future reference.

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the project directory.
    - Add your Google API key to the `.env` file:
      ```
      GOOGLE_API_KEY=your_google_api_key
      ```

## Usage

1. **Run the application**:
    ```bash
    streamlit run app.py
    ```

2. **Interact with the assistant**:
    - Open your web browser and navigate to `http://localhost:8501`.
    - Click the 'Start Listening' button.
    - Speak your request into the microphone.
    - The assistant will process your request, respond with generated text, and speak the response.

## Code Explanation

The application is divided into several key components:

1. **Imports and Initialization**:
    - Import necessary libraries, such as Streamlit, datetime, Google's Generative AI, pyttsx3 for text-to-speech, and speech_recognition for speech-to-text.
    - Load environment variables and configure the Google API key.

2. **Text-to-Speech Setup**:
    - Initialize the pyttsx3 engine for speech synthesis.
    - Set the speaking rate and voice properties.

3. **Google Generative AI Setup**:
    - Configure and initialize the Google Generative AI model.

4. **Helper Functions**:
    - `speak_text(text)`: Uses pyttsx3 to convert text to speech.
    - `append2log(text)`: Logs interaction text to a file with today's date.
    - `process_request(request)`: Processes user requests through the generative model and logs the conversation.

5. **Streamlit Interface**:
    - Set up the Streamlit interface with a title and instructions.
    - Handle user interactions via a button to start listening, use the microphone to capture audio, and process the captured speech.

## Requirements

- Python 3.7 or higher
- Streamlit
- google.generativeai
- python-dotenv
- pyttsx3
- SpeechRecognition

## Notes

- Ensure your microphone is properly configured and accessible by the application.
- The Google API key should have the necessary permissions to use the generative AI services.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to customize and expand the assistant's capabilities as needed!
