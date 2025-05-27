# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## ✅ 0- Objetivo ✅
A proposta do terceiro desafio é criar um container com a imagem Ubuntu no docker, e dentro dele, navegar pelos arquivos e então instalar o pacote Curl.

---
## 💿 1- Criando a imagem 💿
![Primeiro print](/Desafios/Prints/3.1.png)  

Para criar o container com a imagem:
>`Docker create -it` - Cria um container interativo;  
>`--name Ubuntu-Desafio` - Apenas nomeia o Container;  
>`ubuntu bash` - Fala a imagem a ser utilizada, e o comando que será executado quando executar;

Depois, para iniciar o terminal:
>`Docker start -i Ubuntu-Desafio` - Starta, interativamente, o nosso container;

---
## 📂 2- Navegando 📂
Executei alguns comandos básicos de navegação para teste, e então atualizei o sistema e baixei o Curl:  

![Segundo print](/Desafios/Prints/3.2.png)  
![Terceiro print](/Desafios/Prints/3.3.png)

---
## 🛜 3- Curl funcional 🛜

Para verificar se o Curl estava no sistema, executei o seguinte comando:  

![Quarto print](/Desafios/Prints/3.4.png)

Como apareceu a lista de comandos, temos a instalação como sucesso!

---
