class Config:
    # Ativa o modo Debug
    DEBUG = True
    # Determina a pasta com as gravações brutas.
    RECORDS_PATH = 'records' if not DEBUG else 'test/test_record'
    # Determina a pasta com os arquivos cortados.
    SPLITED_PATH = 'records/splited_audio' if not DEBUG else 'test/test_record/splited'
    # Determina as exenteções de audio permitidas.
    AUDIO_EXTENSIONS = (".mp3", ".mp4", ".mpeg", ".mpga", ".m4a", ".wav", ".webm")
    # Determina o tempo máximo de cada pedaço cortado de audio.
    CHUNK_DURATION = 45
    TRANSCRIPTION = 'transcripted' if not DEBUG else 'test/test_transcription'