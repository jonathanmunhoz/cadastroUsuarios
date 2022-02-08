Projeto:
Este é um projeto que é capaz de ler um arquivo CSV, que dentro deste arquivo contém nome, sobrenome e email de usuários.
Além disto, o projeto realiza a criação de contas e senhas, onde a primeira senha gerada é uma random, que é enviada por e-mail
juntamente com seu nome de usuário, sendo necessário fazer a troca da senha logo em seu primeiro acesso.
No banco de dados, toda senha cadastrada é salva de acordo com o e-mail que foi cadastrado.
_______________________________________________________________________________________________________________________________
Tecnologias utilizadas:
Python - Linguagem de Programação

MySQL Server - Banco de dados

Mysql.connector - Biblioteca para integração do Banco de Dados

Csv - Biblioteca para importar um arquivo CSV

Smtplib - Biblioteca para importar um endereço de e-mail

Email.message - Biblioteca para integrar um endereço de e-mail
_______________________________________________________________________________________________________________________________
Requisitos:
Ter instalado uma versão recente do Python (Durante o desenvolvimento foi utilizado a versão PyCharm 2021 3.2)

Criar um arquivo CSV no endereço padrão de projetos Python, com um arquivo CSV que contenha as informações: nome, sobrenome e email.

Criar um banco de dados com as informações necessárias, ou utilizar o IP de um computador que esteja configurado corretamente.
_______________________________________________________________________________________________________________________________
Desenvolvimento do Projeto:
De início, é utilizado uma varíavel para realizar a conexão com o banco de dados, onde todos os dados sobre o Database e a Tabela estão inseridos.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/Df4ZK2Gd/img1.png" alt="img1"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Em seguida, começamos deixando um script para o usuário identificar se a conexão com o banco de dados foi bem-sucedida.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/KvXYGdrX/img2.png" alt="img2"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Após a integração e validação com o Banco de Dados, vamos fazer a leitura do arquivo CSV.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/m2Qgt88P/img3.png" alt="img3"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Depois da leitura do arquivo CSV, começamos com a primeira inserção de dados por parte do usuário, onde irá inserir seu usuário e senha.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/DwnysLMB/img4.png" alt="img4"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Método utilizado para gerar uma senha random:

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/YSypJVqs/img5.png" alt="img5"/></a><br/><br/>
____________________________________________________________________________________________________________________________
Em seguida, o programa irá exibir o usuário e senha random gerada.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/3x1rZWM7/img6.png" alt="img6"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Depois, reservamos uma função para fazer o login de um e-mail, e enviar uma mensagem para o usuário do login e senha cadastrados.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/yYzV40ss/img7.png" alt="img7"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
E uma mensagem de alerta para o usuário.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/6QQWbwwZ/img8.png" alt="img8"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Nesta parte, é utilizado o While para fazer uma validação de senha, para garantir que o usuário não irá conseguir entrar utilizando qualquer senha.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/dQfVCkrC/img9.png" alt="img9"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Para finalizar, o usuário deve inserir sua nova senha, que será enviada para nossa base de dados. E o email, será utilizado para destinar para qual ID no banco será enviado a atualização da senha.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/GtvdTmPW/img10.png" alt="img10"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Comando que realiza a atualização da senha, dependendo do email que for usado:

<a href='https://postimg.cc/xkYxm0v5' target='_blank'><img src='https://i.postimg.cc/BvPddbtr/img11.png' border='0' alt='img11'/></a>
_______________________________________________________________________________________________________________________________
E para execução do comando no SQL com Python, feito a execução da classe alterar_dados, e um commit das informações enviadas.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/SsBmKM9L/img12.png" alt="img12"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
A partir desta etapa, foi colocado um laço de repetição, para um tipo de "menu" no final.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/y846fMfY/img13.png" alt="img13"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Nesta opção, se o usuário digiitar "1", ele poderá alterar sua senha em nosso banco de dados. Foi utilizado o comando Update.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/fRcz18F7/img14.png" alt="img14"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Na opção "2" ele conseguirá deletar seu cadastro de nosso banco de dados, utilizando o comando do SQL Delete.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/pdk2LpPp/img15.png" alt="img15"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Opção "3" é possível que o usuário recupere sua senha, caso a tenha esquecido, usando o comando Select em nosso banco.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/4ddX7s3w/img16.png" alt="img16"/></a><br/><br/>
_______________________________________________________________________________________________________________________________
Opção "4" simplesmente finaliza o programa.

<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/q7pJr8VP/img17.png" alt="img17"/></a><br/><br/>
