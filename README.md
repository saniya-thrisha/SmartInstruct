SmartInstruct is a voice-enabled inspection platform. Using Gemini API, questions are extracted from inspection templates and stored in a database. Responses to these questions 
are captured and stored. Certain keywords such as 'bad condition' or 'okay condition' prompt additional investigation. Based on the information stored in the database,
a comprehensive report is generated to be passed on to the service engineer. The inspection can also happen in Hindi.

Python frameworks: speech_recognition and pyaudio (for voice input), 
pyttsx3 (for voice output), psycopg2 (for database connectivity)  
APIs: Gemini API, GoogleTranslate API 
Database used: PostgreSQL

This project was built as a part of the Caterpillar Hackathon 2024.
