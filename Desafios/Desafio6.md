# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🐹 0- Otimizando aplicação Go 🐹
A proposta do sexto desafio foi otimizar uma aplicação Go utilizando multi-stage build.

---
## 🖊️ 1- Preparativos 🖊️
Primeiramente, baixei o projeto proposto, que foi o [docker-gs-ping](https://github.com/docker/docker-gs-ping):  

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

