# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🧊 0- Trivy 🧊
Para o desafio de número 11, precisei analisar com a ferramenta [Trivy](https://github.com/aquasecurity/trivy/releases/tag/v0.62.1) as vulnerabilidades de uma imagem python pública.  

---
## 🖊️ 1- Preparativos 🖊️
Ao pesquisar o site oficial do Trivy, descobri como se baixava a imagem pelo próprio Docker, e então executei o comando no Docker Desktop:  

![Primeiro print](/Desafios/Prints/11.1.png) 

E então buildei a imagem:  

![Segundo print](/Desafios/Prints/9.2.png)  

---
## ✅ 2- Rodando ✅
Por fim, rodei o container na porta 8080 para a 80 dele:

![Terceiro print](/Desafios/Prints/9.3.png)

O que me retornou o site corretamente:

![Quarto print](/Desafios/Prints/9.4.png)

---
