import requests

url_passo1 = "https://url.com/passo1"
response_passo1 = requests.get(url_passo1)

if response_passo1.status_code == 200:
    print("Passo 1 concluído com sucesso!")
    print("Resposta:", response_passo1.json())
else:
    print(f"Erro no Passo 1. Código de status: {response_passo1.status_code}")
    print("Detalhes:", response_passo1.text)
    exit()

print("\n" + "-" * 50 + "\n")

url_passo2 = "https://url.com/passo2"
data_passo2 = {
    "cpf": "cpf_inserido"
}
response_passo2 = requests.post(url_passo2, json=data_passo2)

if response_passo2.status_code in [200, 201]:
    print("Passo 2 concluído com sucesso!")
    print("Resposta:", response_passo2.json())
else:
    print(f"Erro no Passo 2. Código de status: {response_passo2.status_code}")
    print("Detalhes:", response_passo2.text)
    exit()

print("\n" + "-" * 50 + "\n")

url_passo3 = "https://url.com/passo3"
data_passo3 = {
    "cpf": "cpf_inserido",
    "respostaQuestaoObjetiva": "30"
}
response_passo3 = requests.post(url_passo3, json=data_passo3)

if response_passo3.status_code in [200, 201]:
    print("Passo 3 concluído com sucesso!")
    resposta_passo3 = response_passo3.json()
    print("Resposta:", resposta_passo3)
else:
    print(f"Erro no Passo 3. Código de status: {response_passo3.status_code}")
    print("Detalhes:", response_passo3.text)
    exit()

print("\n" + "-" * 50 + "\n")

url_passo4 = "https://url.com/passo4"
token = "token_inserido"
cpf = "cpf_inserido"

params = {
    "cpf": cpf,
    "token": token
}

response_passo4 = requests.get(url_passo4, params=params)

if response_passo4.status_code in [200, 201]:
    print("Passo 4 concluído com sucesso!")
    print("Resposta:", response_passo4.json())
else:
    print(f"Erro no Passo 4. Código de status: {response_passo4.status_code}")
    print("Detalhes:", response_passo4.text)

print("\n" + "-" * 50 + "\n")