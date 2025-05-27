# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🐳 0- Olá, Docker! 🐳
Para o segundo desafio, foi proposto levantar um container com imagem nginx, em localhost.

---
## 🖊️ 1- Preparativos 🖊️
O primeiro passo foi criar um volume no docker pelo terminal, utilizando:

![Primeiro print](/Desafios/Prints/2.1.png)  

Cria a mensagem em JavaScript.

![Segundo print](/Desafios/Prints/1.2.png)
>`FROM node:alpine` - Busca uma imagem do NodeJs baseada em Alpine Linux;  
>`COPY . /Primeiro` - Copia tudo presente na minha pasta atual para a pasta "Primeiro" dentro da imagem/container;  
>`WORDKDIR Primeiro` - Indica o diretório de trabalho dentro da imagem/container;  
>`CMD Primeiro.js` - Diz que em toda a execução, o arquivo com a mensagem que criei será executado na inicialização;  

---
## 📦 2- Criando a imagem e o container 📦
Dentro do terminal, fui até a pasta com os arquivos referentes a esse desafio que acabei de mostrar, e então criei a imagem com:  

![Terceiro print](/Desafios/Prints/1.3.png)
>`Docker build -t` - Serve para criar a imagem com uma tag, nesse caso, latest, pois não especifiquei;  
>`meu-echo .` - nomeia a image, e o ponto serve para indicar o diretório atual;  

---
## ⬆️ 3- Rodando ⬆️
Após montar a imagem, para executarmos um container e ver se a mensagem funcionou corretamente, executei:  

![Quarto print](/Desafios/Prints/1.4.png)
>`Docker run` - Roda a imagem em um container;  
>`meu-echo` - Especifica qual imagem estamos referenciando;  

Abaixo podemos ver a mensagem já aparecendo no terminal. Com isso, ao verificar o DockerDesktop, na aba de Containers, já podemos ver o nosso container (com um nome genérico, afinal não especificamos nenhum).  

![Quinto print](/Desafios/Prints/1.5.png)

---
