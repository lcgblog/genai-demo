import os
import vertexai

from vertexai.generative_models import GenerativeModel
from google.auth import default

class VertexClient:
    def __init__(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key/genaidemo-433009-31673d223052.json'
        os.environ['HTTPS_PROXY'] = ''
        os.environ['HTTP_PROXY'] = ''
        credentials, project = default()
        vertexai.init(project=project, credentials=credentials, location='asia-northeast1')