# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🦠 0- Servidor Node sem Root 🦠
A proposta do desafio 10 foi de rodar uma aplicação com um servidor Node simples, com um usuário não-root.

---
## 🖊️ 1- Preparativos 🖊️
Para isso, criei um servidor que retorna apenas uma mensagem de "Sucesso" ([Códigos dele nesta página](https://github.com/JorgeAntero/Compass-Uol-Desafio-2-Docker/tree/main/Desafios/Arquivos%20utilizados/Desafio%2010)) e configurei o Dockerfile da seguinte forma:

![Primeiro print](/Desafios/Prints/10.1.png)  
>`RUN adduser -S Jorge` - Cria o usuário Jorge no sistema;
>`USER Jorge` - Serve para trocar para o usuário Jorge;
>`CMD ["node", "index.js"]` - Roda o servidor;

![Segundo print](/Desafios/Prints/12.2.png)  

---
## 🌀 2- Rodando 🌀
Então buildei a imagem e rodei o container nas portas 3000 do host e do Docker:  

![Segundo print](/Desafios/Prints/10.2.png)  

A imagem abaixo demonstra que tudo deu certo:

![Terceiro print](/Desafios/Prints/10.3.png)  

---
## 👤 3- Verificação de usuário 👤
Por último, executei o comando `docker exec *nome do container* whoami` para verificar se o usuário estava correto:  

![Quarto print](/Desafios/Prints/10.4.png)  

Sucesso!

---

