import os
import vertexai


from vertexai.generative_models import GenerativeModel
from google.auth import default

class VertexGenAI:
    def __init__(self):
        credentials, project = default()
        vertexai.init(project=project, credentials=credentials, location='asia-northeast1')
        self.model = GenerativeModel('gemini-1.5-flash-001')

    def generate_text(self, prompt):
        return self.model.generate_content(prompt)

if __name__ == "__main__":
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key/genaidemo-433009-31673d223052.json'
    os.environ['HTTPS_PROXY'] = ''
    os.environ['HTTP_PROXY'] = ''
    gen_ai = VertexGenAI()
    resp = gen_ai.generate_text("Provide interesting trivia")
    print(resp)
