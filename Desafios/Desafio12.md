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
Após montarmos a imagem, podemos veer que seu tamanho diminuiu consideravelmente, e as únicas vulnerabilidades presentes são as do Debian:  

![Quinto print](/Desafios/Prints/12.5.png)  

![Sexto print](/Desafios/Prints/12.6.png)

---
