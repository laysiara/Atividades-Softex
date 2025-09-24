import random
import math
import requests


numero= random.randint(1,50)

print(f"O numero escolhido foi {numero}")

x=math.sin(90)

print(f"Seno de 90 é {x:.2f}")

resposta=requests.get("https://httpbin.org/get")
print("Status Code:", resposta.status_code)
print("Conteúdo:", resposta.text[:100])


