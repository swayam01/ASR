import time
from datetime import datetime
from os import listdir, path
import requests
from sys import argv, exit
from json import dumps

TIME_SPAN = 69
start_time = datetime.now()
file_dict = {}
SPEECH_TEXT_URL = 'http://192.168.1.3:8000/speech2text'
SUMMARIZE_URL = 'http://192.168.1.3:8080/summarize/'
folder  = argv[1]
while True:
    if (datetime.now() - start_time).seconds > TIME_SPAN:

        resp = requests.post(url=SUMMARIZE_URL, json={'text': open(folder + '/' + folder + '.txt').read()})
        with open(folder + '/' + '{}final_summarize.json'.format(folder), 'w') as fout:
            fout.write(dumps(resp.json()))
        exit(0)
    for file in listdir(folder):
        if file not in file_dict:
            file_dict[file] = False
        if file_dict[file]:
            continue
        fileaddress = path.join(folder, file)
        file_send = {
            'file': (file, open(fileaddress, 'rb'), 'text/xml'),
            'Content-Disposition': 'form-data; name="file"; filename="' + file + '"',
            'Content-Type': 'text/xml'
        }            
        r1 = requests.post(SPEECH_TEXT_URL, files=file_send)
        file_dict[file] = True
        with open(folder + '/' + folder + '.txt', 'a+') as f:
            f.write(r1.text)
            f.write('\n')
        print('File text', r1.text)

print('Got Final Output')
