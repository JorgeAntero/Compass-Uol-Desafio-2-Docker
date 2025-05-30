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
Ao rodar o container, o script imprimiu as informações corretamente como podemos ver ao comparar o horário do meu computador com a saída no terminal:  

![Terceiro print](/Desafios/Prints/13.3.png)

---
## 🛜 3- Testando a conectividade 🛜
O último requisito era de testar a conectividade com o container, para isso, utilizei o usuário padrão criado. Dentro do Postgre, cliquei em "Add New Server", depois em "Connection" adicionei os parâmetros escolhidos:  

![Quarto print](/Desafios/Prints/8.4.png)  

![Quinto print](/Desafios/Prints/8.5.png)  

Quando salvei o novo Server, a seguinte tela apareceu demonstrando sucesso:  

![Sexto print](/Desafios/Prints/8.6.png)  

---
