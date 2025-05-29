# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🧊 0- Trivy 🧊
Para o desafio de número 11, precisei analisar com a ferramenta [Trivy](https://github.com/aquasecurity/trivy/releases/tag/v0.62.1) as vulnerabilidades de uma imagem python pública.  

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

Podemos ver que temos 3 vulnerabilidades com risco alto, e 1 com nível médio presentes nas bibliotecas pip e setuptools.

---
## 🕵️ 3- Ações para prevenção 🕵️
Ao analisarmos a tabela que nos aponta as vulnerabilidades, vemos que as duas bibliotecas possuem versões que as corrigem, portanto o método mais eficiente de evitar um ataque seria baixando essas atualizações.

---
