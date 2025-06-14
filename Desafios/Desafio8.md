# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🐘 0- Compose para Postgre 🐘
No desafio de número 8 utilizei o projeto [awesome-compose, postgresql-pgadmin](postgresql-pgadmin) com o compose para criar uma imagem Nginx.  

---
## 🖊️ 1- Preparativos 🖊️
Para começar, criei o compose:  

![Primeiro print](/Desafios/Prints/8.1.png) 
O importante aqui é observar as portas padrão do Postgre e das pastas dos volumes. Além disso, diferente do Desafio 3, coloquei as variáveis de ambiente em um `.env` para segurança dos dados.

---
## ⬆️ 2- Rodando ⬆️
Para o próximo passo, executei o compose no Docker Desktop:  

![Segundo print](/Desafios/Prints/8.2.png)  


E quando colocamos o endereço escolhido no navegador, já podemos ver o funcionamento:  

![Terceiro print](/Desafios/Prints/8.3.png)

---
## 🛜 3- Testando a conectividade 🛜
O último requisito era de testar a conectividade com o container, para isso, utilizei o usuário padrão criado. Dentro do Postgre, cliquei em "Add New Server", depois em "Connection" adicionei os parâmetros escolhidos:  

![Quarto print](/Desafios/Prints/8.4.png)  

![Quinto print](/Desafios/Prints/8.5.png)  

Quando salvei o novo Server, a seguinte tela apareceu demonstrando sucesso:  

![Sexto print](/Desafios/Prints/8.6.png)  

---
