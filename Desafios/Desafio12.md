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

![Quarto print](/Desafios/Prints/12.4.png)  

---
## 🕵️ 3- Ações para prevenção 🕵️
Ao analisarmos a tabela que nos aponta as vulnerabilidades, vemos que a biblioteca possui versões que as corrigem, portanto uma das soluções possíveis seria atualizar a versão dela.

---
