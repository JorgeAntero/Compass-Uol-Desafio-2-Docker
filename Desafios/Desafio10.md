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

A imagem abaixo demonstra o sucesso:

![Terceiro print](/Desafios/Prints/10.3.png)  

![Quarto print](/Desafios/Prints/12.4.png)  
>Aqui a única diferença é que, para deixar a imagem mais enxuta, utilizei a versão Slim dela.

---
## 🛡️ 3- Resultado 🛡️
Após montarmos a imagem, podemos veer que seu tamanho diminuiu consideravelmente, e as únicas vulnerabilidades presentes são as do Debian:  

![Quinto print](/Desafios/Prints/12.5.png)  

![Sexto print](/Desafios/Prints/12.6.png)

---

