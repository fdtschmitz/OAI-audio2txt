from openai import OpenAI
from sources.config import Config
import os
import pickle


class OpenClient:
    def __init__(self) -> None:
        self.client: OpenAI = OpenAI()

    def get_audio_transcription(self, audio_file_path):
        print(f'Starting transcription of file {audio_file_path}')
        # Abre o arquivo de audio
        with open(audio_file_path, 'rb') as audio_file:
            # Faz a request com os parametros escolhidos
            transcription = self.client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="verbose_json"
            )
            print('Audio file transcripted.')
        return transcription

    def transcription_to_file(self, audio_file_path, output_path=Config.TRANSCRIPTION):
        transcription = self.get_audio_transcription(audio_file_path)
        base_name = os.path.basename(audio_file_path)
        output_file = os.path.join(output_path, f"{base_name}_transcripted.pickle")
        with open(output_file, 'wb') as pickle_file:
            pickle.dump(transcription, pickle_file)
        print(f'Transcription saved on {output_file}')



client = OpenClient()