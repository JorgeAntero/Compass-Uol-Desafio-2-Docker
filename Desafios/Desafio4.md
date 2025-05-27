# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🐬 0- MySQL no Docker 🐬
    Para o quarto desafio, precisei desenvolver um método de executar o banco de dados MySQL no Docker.

---
## 🖊️ 1- Preparativos 🖊️
    Primeiro de tudo, criei um volume no DockerDesktop para armazenar os dados.
![Primeiro print](/Desafios/Prints/4.1.png)  

    Após isso, criei um compose para estruturar todo meu serviço:
![Segundo print](/Desafios/Prints/4.2.png)
>`desafio-4:` - Toda essa parte serve para criar o meu serviço do banco. Por exemplo, `image: mysql:8.4` define a imagem que nosso container se baseará;  
>`environment:` - Define as variáveis de ambiente padrões usadas para o MySQL;  
>`ports:` - Indica a porta padrão do MySQL;  
>`volumes:` - Monta a pasta local do volume que criamos dentro do container;

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

