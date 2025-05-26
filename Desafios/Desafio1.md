
# - 🔒 Projeto de Bolsas DevSecOps/AWS,  Compass UOL, abril 2025 🔒 -

## 🐳 0- Olá, Docker! 🐳
    O objetivo do primeiro desafio consiste na criação de uma imagem Alpine com o nome "meu-echo" que imprima "Olá, Docker!" toda vez que executada, e depois executar um container a partir dela.
---
## 🖊️ 1- Preparativos 🖊️
    Antes de ir para o Docker em si, fui ao VS code para criar o arquivo que executará a mensagem, além da Dockerfile.
![Primeiro print](/Desafios/Prints/1.1.png)  

    Cria a mensagem em JavaScript.

![Primeiro print](/Desafios/Prints/1.2.png)
>`cd /` - Para ir até o diretório Root;  
>`mkdir dados` - Para criar a página que o Samba utilizará para comunicar as máquinas;  
>`chmod 777 dados` - Para dar permissões gerais de escrita, leitura e execução da pasta;  
>`vi /etc/samba/smb.conf` - e então configurei conforme a imagem:
