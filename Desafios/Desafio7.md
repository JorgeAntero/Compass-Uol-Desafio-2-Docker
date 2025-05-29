# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🚧 0- Juntando back e front de uma aplicação 🚧
Para o sétimo desafio, foi proposto que utilizasse-mos o docker compose para executar o projeto [awesome-compose, react-express-mongodb](https://github.com/docker/awesome-compose/tree/master/react-express-mongodb).  

---
## 🖊️ 1- Preparativos 🖊️
O primeiro passo foi criar um compose que juntasse os serviços necessários. O meu ficou da seguinte forma:  

(Para melhor visualização, [clique aqui!](https://github.com/JorgeAntero/Compass-Uol-Desafio-2-Docker/blob/main/Desafios/Arquivos%20utilizados/Desafio%207/docker-compose.yaml))  

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

---
## 🍃 2- Conclusão 🍃
Para o próximo passo, executei o compose no Docker Desktop:  

![Primeiro print](/Desafios/Prints/7.1.png) 

Ao olharmos os containers, podemos ver todas as imagens:

![Segundo print](/Desafios/Prints/7.2.png)  

E ao colocar o `localhost:3000` no navegador:

![Terceiro print](/Desafios/Prints/7.3.png)

---
