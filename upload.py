#colocar esse arquivo fora da pasta do repositório e preencher o githubToken e o committer
# Import the requests module for send a PUT request
import requests
# Import the base64 module for encoding a file to base64
import base64
import json
from datetime import datetime

githubToken=''#Personal Token Github
githubAPIURL = "https://api.github.com/repos/CaioViktor/Test_Upload/contents/data.json" #URI para o arquivo que será atualizado
r = requests.get(githubAPIURL)#pega informações do arquivo no git
sha = r.json()['sha'] #pega sha do arquivo para atualização

data = {'data':str(datetime.now())}
jsonfile=json.dumps(data)
with open("Test_Upload/data.json","w") as file:
    file.write(jsonfile)#grava data atual no arquivo local
with open("Test_Upload/data.json","rb") as file:
    encodedData = base64.b64encode(file.read())#lê o arquivo local e converte para binario 64
    headers = {
        "Authorization": f'''Bearer {githubToken}''',
        "Content-type": "application/vnd.github+json"
    }
    data = {
        "message": "Upload data", # Put your commit message here.
        "committer":{"name":"","email":""},#colocar no nome do user do git e o email do git
        'sha':sha,
        "content": encodedData.decode("utf-8")#arquivo codificado a ser enviado
    }

    r = requests.put(githubAPIURL, headers=headers, json=data) #faz o post do arquivo
    print(r.text) # Printing the response
