from pydub import AudioSegment
from sources.config import Config
import os


def split_audio(input_file,
                output_folder=Config.SPLITED_PATH,
                chunk_duration_minutes=Config.CHUNK_DURATION,
                channels=1):
    # Carrega o arquivo de audio
    audio = AudioSegment.from_file(input_file)

    # Calcula o tamanho da parte em milisegundos
    chunk_size_ms = chunk_duration_minutes * 60 * 1000

    # Inicializa as variáveis para divisão
    current_part = 1
    total_parts = len(audio) // chunk_size_ms + 1
    
    # Cria a base do nome do arquivo
    base_name = os.path.basename(input_file)

    # Itera sobre os pedaços de audio
    for i in range(0, len(audio), chunk_size_ms):
        # Pega o pedaço atual
        chunk = audio[i:i+chunk_size_ms]

        # Cria o nome do arquivo de saída
        output_file = os.path.join(output_folder, f"{base_name}_part_{current_part}.mp3")

        # Exporta o pedaço para o arquivo de saída com o número especificado de canais
        chunk.export(output_file, format="mp3", parameters=["-ac", str(channels)])

        print(f"Part {current_part}/{total_parts} saved to {output_file}")

        # Incrementa o contador de partes
        current_part += 1

def file_iterator(folder_path=Config.RECORDS_PATH, accepted_extensions=Config.AUDIO_EXTENSIONS):
    if not os.path.exists(folder_path):
        print("Pasta não encontrada")
        return

    # Verifica os arquivos contidos na pasta
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # Confirma se é um arquivo (e não uma subpasta)
        if os.path.isfile(file_path):
            # Confirma se a extensão é aceita
            if file_path.endswith(tuple(accepted_extensions)):
                # Verifica o tamanho do arquivo
                file_size = os.path.getsize(file_path)
                # Caso seja maior que 24MB (24 * 1024 * 1024 bytes)
                if file_size > 24 * 1024 * 1024:
                    # Chama a função para dividir o arquivo
                    split_audio(file_path)
