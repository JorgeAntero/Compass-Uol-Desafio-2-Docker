# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## ⚡ 0- Corrigindo vulnerabilidades ⚡
No penultimo desafio, precisei corrigir arquivos com diversas vulnerabilidades. Todos os arquivos, corrigidos e não corrigidos disponíveis ![aqui!](https://github.com/JorgeAntero/Compass-Uol-Desafio-2-Docker/tree/main/Desafios/Arquivos%20utilizados/Desafio%2012) 

---
## 🖊️ 1- Preparativos 🖊️
Ao pesquisar o site oficial do Trivy, descobri como se baixava a imagem pelo próprio Docker, e então executei o comando no Docker Desktop:  

![Primeiro print](/Desafios/Prints/11.1.png)  

---
## 🔍 2- Análise 🔎
E então executei o comando
`docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image --no-progress python:3.9`
>`-v /var/run/docker.sock:/var/run/docker.sock` - Serve para fazer com que o Trivy rode como se estivesse nativamente, enxergando assim o Docker do host;  
>`aquasec/trivy image` - Indica a imagem a ser utilizada, e chama o comando `image` do Trivy;  
>`--no-progress python:3.9` - Deixa a saída mais limpa, e indica a imagem a ser analisada;  

E a saída foi:

![Segundo print](/Desafios/Prints/11.2.png)  

Podemos ver que temos 3 vulnerabilidades com risco alto presente na biblioteca setuptools. Para ver o que cada uma afeta, cliquei no link da própria tabela:  
A primeira basicamente consome ciclos excessivos da CPU;  
A segunda tem em sua construção um elemento que pode causar um mau funcionamento do código;  
A terceira possui em sua construção um elemento que pode causar uma certa confusão de diretórios;  

---
## 🕵️ 3- Ações para prevenção 🕵️
Ao analisarmos a tabela que nos aponta as vulnerabilidades, vemos que a biblioteca possui versões que as corrigem, portanto uma das soluções possíveis seria atualizar a versão dela.

---
