# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🐘 0- Compose para Postgre 🐘
No desafio de número 8 utilizei o projeto [awesome-compose, postgresql-pgadmin](postgresql-pgadmin) com o compose para criar uma imagem Nginx.  

---
## 🖊️ 1- Preparativos 🖊️
Para começar, criei o compose:  

![Primeiro print](/Desafios/Prints/8.1.png) 
O importante aqui é observar as portas padrão do Postgre, além das pastas dos volumes. Além disso, diferente do Desafio 3, coloquei as variáveis de ambiente em um `.env` para segurança dos dados.

---
## 🍃 2- Conclusão 🍃
Para o próximo passo, executei o compose no Docker Desktop:  



Ao olharmos os containers, podemos ver todas as imagens:

![Segundo print](/Desafios/Prints/7.2.png)  

E ao colocar o `localhost:3000` no navegador:

![Terceiro print](/Desafios/Prints/7.3.png)

---
