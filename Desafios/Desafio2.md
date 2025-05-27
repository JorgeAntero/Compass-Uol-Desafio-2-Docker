# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## ✅ 0- Nginx em volume ✅
Para o segundo desafio, foi proposto levantar um container com imagem nginx, em localhost.

---
## 🖊️ 1- Preparativos 🖊️
O primeiro passo foi criar um volume no docker pelo terminal, utilizando:  

![Primeiro print](/Desafios/Prints/2.1.png)  

Após isso, reutilizei a base do arquivo HTML utilizado no [último desafio da Compass](https://github.com/JorgeAntero/Compass-Uol-Desafio-1-Nginx), fazendo pequenas alterações para se enquadrar no novo projeto.  

---
## ✈️ 2- Passando os arquivos para o volume ✈️
Com o site e o volume prontos, precisei unir os dois, para isso, executei o comando:  

![Segundo print](/Desafios/Prints/2.2.png)
>`Docker run --rm` - Executa o container, removendo-o quando ele parar de ser executado;  
>`-v ${PWD}:/src` - Cria dentro do container, no diretório `/src`, tudo do diretório atual, no nosso caso onde se encontra o `index.html`;  
>`-v arquivos-desafio2:/dest` - Dentro do container, no diretório `/dest`, monta o volume nomeado `arquivos-desafio2`;  
>`busybox` - Imagem leve que utilizaremos para executar o container;  
>`sh -c "cp /src/index.html /dest/"` - Executa como texto no shell o comando entre aspas, que serve para copiar o `index.html` para o `/dest/`;  

---
## 💻 3- Rodando 💻
Agora basta rodar localmente e testar, para isso:  

![Terceiro print](/Desafios/Prints/2.3.png)
>`Docker run -d -p` - Roda o container em segundo plano, na porta `80` do host para a porta `80` do container;  
>`-v arquivos-desafio2:/usr/share/nginx/html` - Monta o arquivos-desafio2 onde o nginx busca os seus arquivos HTML por padrão;  
>`--name NginxTeste nginx` - Nomeia o nosso container e diz a imagem a ser utilizada;  

E então, ao colocar `http://localhost` no navegador:  

![Quinto print](/Desafios/Prints/2.4.png)

---
