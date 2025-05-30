# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## ⚡ 0- Corrigindo vulnerabilidades ⚡
No penultimo desafio, precisei corrigir arquivos com diversas vulnerabilidades. Todos os arquivos, corrigidos e não corrigidos disponíveis [aqui!](https://github.com/JorgeAntero/Compass-Uol-Desafio-2-Docker/tree/main/Desafios/Arquivos%20utilizados/Desafio%2012) 

---
## ⛔ 1- Vulnerável ⛔
O primeiro passo foi ver quanto o arquivo vulnerável pesa, e quais são suas vulnerabilidades. Pra isso, utilizei o Trivy:

![Primeiro print](/Desafios/Prints/12.1.png)  

![Segundo print](/Desafios/Prints/12.2.png)  

---
## 🪛 2- Modificações 🪛
Então fiz as alterações necessárias nos arquivos:  
![Terceiro print](/Desafios/Prints/12.3.png)  
>Todas acima servem para que esses serviços sejam atualizados para a versão mais recente compatível com o Python 3.9.  

![Quarto print](/Desafios/Prints/12.4.png)  
>Aqui a única diferença é que, para deixar a imagem mais enxuta, utilizei a versão Slim dela.

---
## 🛡️ 3- Resultado 🛡️
Após montarmos a imagem, podemos ver que seu tamanho diminuiu consideravelmente, e as únicas vulnerabilidades presentes são as do Debian:  

![Quinto print](/Desafios/Prints/12.5.png)  

![Sexto print](/Desafios/Prints/12.6.png)

---
## 🫚 4- Corrigindo usuário 🫚
Para melhor segurança, devemos rodar o container com um usuário não-root, pra isso, alterei o Dockerfile:

![Sétimo print](/Desafios/Prints/12.7.png)  
>Linha 2 - `RUN adduser --system --group --no-create-home --disabled-login jorge` - Cria o grupo e usuário jorge no sistema, de forma que não precise de login;  
>Linha 4 - `RUN chown -R jorge:jorge /app` - Garante que meu usuário tenha acesso à pasta app;  

Com isso, ao verificar o usuário:  

![Oitavo print](/Desafios/Prints/12.8.png)

---

