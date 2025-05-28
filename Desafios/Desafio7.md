# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🚧 0- Juntando back e front de uma aplicação 🚧
Para o sétimo desafio, foi proposto que utilizasse-mos o docker compose para executar o projeto [awesome-compose, react-express-mongodb](https://github.com/docker/awesome-compose/tree/master/react-express-mongodb).  

---
## 🖊️ 1- Preparativos 🖊️
O primeiro passo foi criar um compose que juntasse os serviços necessários. O meu ficou da seguinte forma: 
(Para melhor visualização, [clique aqui!](https://github.com/JorgeAntero/Compass-Uol-Desafio-2-Docker/blob/main/Desafios/Arquivos%20utilizados/docker-compose-Des7.yaml))
      version: '3.9'
    
    services:
      back: #Configura o serviço do Backend;
        build:
          context: backend #Encontra o Dockerfile do backend nessa pasta;
          target: development #Usa esse estágio de building;
    
        expose:
          - 3000 #Preferi deixar como no projeto original. Serve para expor para outros containers a porta 3000;
    
        volumes:
          - ./backend:/usr/src/app #Copia a pasta backend para o diretório do container;
          - /usr/src/app/node_modules #Deixei como no original. Basicamente garante que o node_modules não seja sobreposto, evitando crashes;
          
        restart: unless-stopped #Serve para que o serviço esteja sempre de pé, a não ser que seja eu que derrube;
    
        networks:
          - backefront #Cria uma rede de comunicação entre os serviços do Back e do Front;
          - backedb #Cria uma rede de comunicação entre os serviços do Back e do BD;
    
        depends_on:
          - bd #Impede que o serviço seja iniciado sem que o BD esteja de pé primero;
    
      front: #Configura o serviço do Frontend
        build:
          context: frontend #Encontra o Dockerfile do frontend nessa pasta;
          target: development 
    
        ports:
          - 3000:3000 #Expõe as portas 3000 do container para a 3000 do host;
    
        volumes:
          - ./frontend:/usr/src/app #Copia a pasta frontend para o diretório do container;
          - /usr/src/app/node_modules 
    
        restart: unless-stopped
    
        networks:
          - backefront
    
        depends_on:
          - back #Impede que o serviço seja iniciado sem que o Back esteja de pé primero;
    
      bd: #Configura o serviço do Banco de Dados
        image: mongo:8.0 #Constrói o container com base na imagem do mongo;
    
        expose:
          - 27017 #Porta padrão do mongo visível para outros containers;
    
        volumes:
          - mongo:/data/db #Faz um volume para permanencia de dados do banco;
          
        restart: unless-stopped
    
        networks:
          - backedb
    
    networks: #Estabelece as Redes internas
      backefront:
      backedb:
    
    volumes:
      mongo:     



![Primeiro print](/Desafios/Prints/6.1.png)  

Após isso, apaguei o arquivo `Dockerfile.multistage` para fazer o meu próprio, editando o `Dockerfile`. Com isso, editei tirando os comentários:  

![Segundo print](/Desafios/Prints/6.2.png)  

Ao executar a imagem, observei o tamanho dela:  

![Terceiro print](/Desafios/Prints/6.3.png)

---
## 🤖 2- Otimizando 🤖
Então montei o multistage:  

![Quarto print](/Desafios/Prints/6.4.png)  
>Linha 1 - `FROM golang:1.19 AS builder` - Cria a imagem e indica ela como builder;  
>Linha 8 - `FROM alpine:latest` - Cria uma imagem com alpine, que é extreamente leve, para o container final;
>`WORKDIR /root/` - O diretório de trabalho será o root;
>`COPY --from=builder /app/docker-gs-ping .` - Copia do builder o binário, que está em `app` para `root`;
>`EXPOSE 8080` - Informa a porta a ser usada;
>`CMD [ "/docker-gs-ping" ]` - Executa o binário criado ao rodar o container;

---
## 😉 3- Resultado 😉
Em seguida buildei a imagem:  

![Quinto print](/Desafios/Prints/6.5.png)  

E a imagem ficou com o seguinte tamanho:

![Quinto print](/Desafios/Prints/6.6.png)  

---

