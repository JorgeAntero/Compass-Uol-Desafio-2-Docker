# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🦠 0- Servidor Node sem Root 🦠
A proposta do desafio 10 foi de rodar uma aplicação com um servidor Node simples, com um usuário não-root.

---
## 🖊️ 1- Preparativos 🖊️
Para isso, criei um servidor que retorna apenas uma mensagem de "Sucesso" ([Código dele nesta página](https://github.com/JorgeAntero/Compass-Uol-Desafio-2-Docker/tree/main/Desafios/Arquivos%20utilizados/Desafio%2010))

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
Após montarmos a imagem, podemos veer que seu tamanho diminuiu consideravelmente, e as únicas vulnerabilidades presentes são as do Debian:  

![Quinto print](/Desafios/Prints/12.5.png)  

![Sexto print](/Desafios/Prints/12.6.png)

---

