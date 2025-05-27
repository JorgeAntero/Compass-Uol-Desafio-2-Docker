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
## 📦 2- Testando 📦
    Então executei o compose no meu shell:
![Terceiro print](/Desafios/Prints/4.3.png)

    E dentro do MySQL Workbench, fiz a conexão:
![Quarto print](/Desafios/Prints/4.4.png)
![Quinto print](/Desafios/Prints/4.5.png)

    Após isso fiz um teste criando uma tabela simples:
![Sexto print](/Desafios/Prints/4.6.png)

---
## ⬆️ 3- Rodando ⬆️
    Após montar a imagem, para executarmos um container e ver se a mensagem funcionou corretamente, executei:

>`Docker run` - Roda a imagem em um container;  
>`meu-echo` - Especifica qual imagem estamos referenciando;  

    Abaixo podemos ver a mensagem já aparecendo no terminal. Com isso, ao verificar o DockerDesktop, na aba de Containers, já podemos ver o nosso container (com um nome genérico, afinal não especificamos nenhum).  


---

