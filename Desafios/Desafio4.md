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
## 🦾 3- Testando permanência dos arquivos 🦾
    Para testar o que aconteceria caso meu container parasse, derrubei ele no próprio Docker Desktop, e com isso, os arquivos sumiram da conexão do Workbench:
![Sétimo print](/Desafios/Prints/4.7.png)
![Oitavo print](/Desafios/Prints/4.8.png)

    Porém, ao executar o compose novamente, todos os arquivos ainda estavam lá:
![Nono print](/Desafios/Prints/4.9.png)

---

