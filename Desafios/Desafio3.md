# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## ✅ 0- Objetivo ✅
    A proposta do terceiro desafio é criar um container com a imagem Ubuntu no docker, e dentro dele, navegar pelos arquivos e então instalar o pacote Curl.
---
## 💿 1- Criando a imagem 💿
![Primeiro print](/Desafios/Prints/3.1.png)  

>`Docker create -it` - Cria um container interativo;  
>`--name Ubuntu-Desafio` - Apenas nomeia o Container;  
>`ubuntu bash` - Fala a imagem a ser utilizada, e o comando que será executado quando executar;  

![Segundo print](/Desafios/Prints/1.2.png)

---
## 📦 2- Criando a imagem e o container 📦
    Dentro do terminal, fui até a pasta com os arquivos referentes a esse desafio que acabei de mostrar, e então criei a imagem com:
![Terceiro print](/Desafios/Prints/1.3.png)
>`Docker build -t` - Serve para criar a imagem com uma tag, nesse caso, latest, pois não especifiquei;  
>`meu-echo .` - nomeia a image, e o ponto serve para indicar o diretório atual;  

---
## ⬆️ 2- Rodando ⬆️
    Após montar a imagem, para executarmos um container e ver se a mensagem funcionou corretamente, executei:
![Quarto print](/Desafios/Prints/1.4.png)
>`Docker run` - Roda a imagem em um container;  
>`meu-echo` - Especifica qual imagem estamos referenciando;  

    Abaixo podemos ver a mensagem já aparecendo no terminal. Com isso, ao verificar o DockerDesktop, na aba de Containers, já podemos ver o nosso container (com um nome genérico, afinal não especificamos nenhum).  
![Quinto print](/Desafios/Prints/1.5.png)

---
