import google.generativeai as genai
from database import get_column_names, get_rows

PROMPT = 'Context: This data has been collected by a service technician to pass on to a service engineer. Each tuple is a row. List contains column names. Generate summary and insights. Data: '
MODEL = 'gemini-pro'
colnames= get_column_names()
data=get_rows()
PROMPT+= str(colnames) +str(data)

print('** GenAI text: %r model & prompt %r\n' % (MODEL, PROMPT))

genai.configure(api_key='your api key') #replace with API Key
model = genai.GenerativeModel(MODEL)
response = model.generate_content(PROMPT)
if response:
    print(response.text)
else:
    print("failed to generate")