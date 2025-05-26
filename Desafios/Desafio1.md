
# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🐳 0- Olá, Docker! 🐳
    O objetivo do primeiro desafio consiste na criação de uma imagem Alpine com o nome "meu-echo" que imprima "Olá, Docker!" toda vez que executada, e depois executar um container a partir dela.
---
## 🖊️ 1- Preparativos 🖊️
    Antes de ir para o Docker em si, fui ao VS code para criar o arquivo que executará a mensagem, além da Dockerfile.
![Primeiro print](/Desafios/Prints/1.1.png)  

    Cria a mensagem em JavaScript.

![Primeiro print](/Desafios/Prints/1.2.png)
>`FROM node:alpine` - Busca uma imagem do NodeJs baseada em Alpine Linux;  
>`COPY . /Primeiro` - Copia tudo presente na minha pasta atual para a pasta "Primeiro" dentro da imagem/container;  
>`WORDKDIR Primeiro` - Indica o diretório de trabalho dentro da imagem/container;  
>`CMD Primeiro.js` - Diz que em toda a execução, o arquivo com a mensagem que criei será executado na inicialização;

---
## 📦 2- Criando a imagem e o container 📦
