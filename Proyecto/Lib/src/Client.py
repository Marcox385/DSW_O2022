# IS727272 - Proyecto - 
import requests, os
import Parser, Recorder, json

if __name__ == '__main__':
    parser_helper = Parser.SimpleEnv()
    dotenv_file = parser_helper.begin_parse(parser_helper.ParseType.ENV, r'..\..\.env')
    API_KEY = dotenv_file['API_KEY']
    API = dotenv_file['API']

    recorder_helper = Recorder.AudioRecorder('send_file')
    recorder_proxy = Recorder.RecorderProxy(recorder_helper)
    recorder_proxy.record(duration = 5.0)

    api_data = {
        'api_token': API_KEY,
        'return': 'spotify'
    }

    files = {
        'file': open(recorder_helper.get_output_path(), 'rb')
    }

    result = requests.post(API, data = api_data, files = files).json()['result']

    if (result):
        print(f'\n--- CANCIÓN ENCONTRADA ---\nTítulo: {result["title"]}\nArtista: {result["artist"]}\nLinks: {result["song_link"]}')
    else:
        print('CANCIÓN NO ENCONTRADA, VUELVE A INTENTAR...')