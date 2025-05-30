# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🐍 0- Script Python e Push pro Hub 🐍
No último desafio precisei criar um Dockerfile que copiasse, com uma imagem Python:3.11-slim, um script em python que imprimisse a data e horas atuais. ([Script nesta página](https://github.com/JorgeAntero/Compass-Uol-Desafio-2-Docker/blob/main/Desafios/Arquivos%20utilizados/Desafio%2013/app.py))

---
## 🖊️ 1- Preparativos 🖊️
Para começar, criei o Dockerfile:  

![Primeiro print](/Desafios/Prints/13.1.png)  

Depois buildei a imagem:  

![Segundo print](/Desafios/Prints/13.2.png) 

---
## ⬆️ 2- Rodando ⬆️
Ao rodar o container, o script imprimiu as informações corretamente, como podemos ver ao comparar o horário do meu computador com a saída no terminal:  

![Terceiro print](/Desafios/Prints/13.3.png)

---
## 👽 3- Extra 👽
Como um extra, foi pedido que eu upasse o [Desafio 1](https://github.com/JorgeAntero/Compass-Uol-Desafio-2-Docker/blob/main/Desafios/Desafio1.md) no DockerHub, pra isso fiz os seguintes passos:

buildei a imagem:  

![Quarto print](/Desafios/Prints/13.4.png)  

Depois fiz o push para o Hub:

![Quinto print](/Desafios/Prints/13.5.png)  

Ao acessar o meu perfil no site, vemos que está tudo certo:

![Sexto print](/Desafios/Prints/13.6.png)  

---
