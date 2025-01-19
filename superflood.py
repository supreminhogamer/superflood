import requests
import time
import os


os.system("title 🌊SUPER FLOOD🌊")


print("""
------------------------------🌊SUPER FLOOD🌊--------------------------------
     _____  _    _ _____   ______ _____    ______ _      ____   ____    _____  
    / ____|| |  | |  __ \ |  ____|  __ \  |  ____| |    / __ \ / __ \  |  __ \ 
   | (___  | |  | | |__) || |__  | |__) | | |__  | |   | |  | | |  | | | |  | |
    \___ \ | |  | |  ___/ |  __| |  _  /  |  __| | |   | |  | | |  | | | |  | |
    ____) || |__| | |     | |____| | \ \  | |    | |___| |__| | |__| | | |__| |
   |_____/  \____/|_|     |______|_|  \_\ |_|    |______\____/ \____/  |_____/ 

Por @supreminho_gamer no Discord - Versão 1.0

--------------------------------CARREGANDO------------------------------------
""")

time.sleep(4)

azi = """
                                          
            ,d                            
            88                            
,adPPYba, MM88MMM ,adPPYba,  8b,dPPYba,   
I8[    ""   88   a8"     "8a 88P'    "8a  
 `"Y8ba,    88   8b       d8 88       d8  
aa    ]8I   88,  "8a,   ,a8" 88b,   ,a8"  
`"YbbdP"'   "Y888 `"YbbdP"'  88`YbbdP"'   
                             88           
                             88   

Aviso: Esse foi um projeto criado pela diversão, por favor não use para o mal!                             
"""
print(azi)



# Pede o Token de autenticação do discord:
Tokeninp = input("Insira seu token do discord aqui: ")
token = (Tokeninp)

# Pede o ID do canal:
channelinp = input("Insira o ID do canal aqui: ")
channel_id = (channelinp)

# Pede a mensagem a ser enviada:
messageinp = input("Insira a mensagem aqui: ")
message = (messageinp)

# A quantidade de vezes que vai ser repetido a ação: :skull:
counter = 10000000000000000
start_time = time.time()

# Os tempos de sleep para cada variavel:
default_sleep = 0.1
backoff_sleep = 3
backoff_duration = 30

# Aqui começa o timer e coloca as informações do request:
while time.time() - start_time < counter:

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Authorization': token
    }

    json_data = {
    'content': message
    }

    
    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
    if response.status_code == 200: # Detecta um envio bem-sucedido
        print(f"A mensagem '{message}' foi enviada")

    if response.status_code == 400: # Informações errada do ID de canal
          print("[400] Verifique as informações do ID de canal e tente novamente")
          exit("Bad Request")

    if response.status_code == 404: # Conexão de internet
         print("[404] Verifique a conexão de internet e tente novamente")
         exit("Bad Request")

    if response.status_code == 401: # Token incorreto
         print("[401] Verifique as informações de Token e tente novamente")
         exit("Bad Request")

    if response.status_code == 403: # Sem permissão para enviar mensagem no canal
         print("[403] Você não tem permissão para enviar mensagens nesse canal, por favor tente novamente mais tarde")
         exit("Sem permissão")
        
    if response.status_code == 429:  # Detecta "Too Many Requests"
        print("Você foi limitado de mandar mensagens, entrando em modo de espera...")
        backoff_end_time = time.time() + backoff_duration

        while time.time() < backoff_end_time:
            time.sleep(backoff_sleep)
            response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
            
            if response.status_code == 200: # Mensagem enviada com sucesso durante o modo de espera
              print(f"Mensagem enviada durante o modo de espera: '{message}' ")
            else:
                 print(f"Mensagem não conseguiu ser enviada durante o modo de espera...")
     
else:
        time.sleep(default_sleep)  # Retorna ao tempo de espera padrão

