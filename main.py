import mysql.connector

con = mysql.connector.connect(host='localhost',database='db_usuario',user='root',password='root')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor = con.cursor(buffered=True)
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)
    print("_______________________________________________________")

import csv

with open('dadosUsuarios.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for linha in arquivo_csv:
        print(linha)

print("_______________________________________________________")

nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
print("_______________________________________________________")

usuario = input('Digite seu usuário: ')
chave = input('Digite a base da sua senha: ')

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "a"
    elif letra in "Bb": senha = senha + "2"
    elif letra in "Cc": senha = senha + "3"
    elif letra in "Dd": senha = senha + "d"
    elif letra in "Ee": senha = senha + "5"
    elif letra in "Ff": senha = senha + "6"
    elif letra in "Gg": senha = senha + "G"
    elif letra in "Hh": senha = senha + "8"
    elif letra in "Ii": senha = senha + "I"
    elif letra in "Jj": senha = senha + "10"
    elif letra in "Kk": senha = senha + "11"
    elif letra in "Ll": senha = senha + "L"
    elif letra in "Nn": senha = senha + "n"
    elif letra in "Oo": senha = senha + "0"
    elif letra in "Pp": senha = senha + "14"
    elif letra in "Qq": senha = senha + "15"
    elif letra in "Tt": senha = senha + "T"
    elif letra in "Uu": senha = senha + "19"
    elif letra in "Vv": senha = senha + "20"
    elif letra in "Ww": senha = senha + "W"
    elif letra in "Xx": senha = senha + "22"
    elif letra in "Yy": senha = senha + "y"
    elif letra in "Zz": senha = senha + "24"

    elif letra in "1": senha = senha + "i"
    elif letra in "2": senha = senha + "II"
    elif letra in "3": senha = senha + "III"
    elif letra in "4": senha = senha + "04"
    elif letra in "5": senha = senha + "05"
    elif letra in "6": senha = senha + "06"

    elif letra in "Rr": senha = senha + "#"
    elif letra in "Ss": senha = senha + "%"
    elif letra in "Mm": senha = senha + "$"
    else: senha = senha + letra

print('_______________________________________________________')
print('Seu usuário é: ', usuario)
print('Sua senha é: ', senha)
print('_______________________________________________________')

import smtplib
import email.message

def enviar_email():
    corpo_email = 'Nome: ' + nome + '<br>Usuario: ' + usuario + '<br>Senha: ' + senha

    msg = email.message.Message()
    msg['Subject'] = "Teste"
    msg['From'] = 'usuariotestepython@gmail.com'
    msg['To'] = input('Digite seu E-mail para receber a senha: ')
    password = 'testando123'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
enviar_email()

print('_______________________________________________________')
print('Realize seu Login!')

login = input('Login: ')
while login not in usuario:
    login = input('Dados inválidos. Por favor, informe seu usuario: ')
senhaLogin = input('Senha: ')
while senhaLogin not in senha:
    senhaLogin = input('Dados inválidos. Por favor, informe sua senha: ')
print('Dados corretos! Por favor, cadastre uma nova senha em seu primeiro login!'.format(senhaLogin))

print("_______________________________________________________")

novaSenha = input('Nova senha: ')
email = input("Confirme seu E-mail: ")

#alterar_dados = "UPDATE tb_usuario SET senha = '" + novaSenha + "' WHERE email = '" + email + "';";
alterar_dados = "INSERT INTO tb_usuario (nome, sobrenome, usuario, email, codigo, senha) VALUES ('" + nome + "', '" + sobrenome + "','" + usuario + "','" + email + "', '" + senha + "', '" + novaSenha + "')";

cursor.execute(alterar_dados)
con.commit()

opcao = "0"

while opcao !="4":
    print("Opções para continuar:")
    print("1) Alterar senha")
    print("2) Esqueci minha senha")
    print("3) Deletar usuario")

    opcoes = input("Insira o número da opção desejada: ")

    for numero in opcoes:
        if numero in "1":
            novaSenha = input("Alterar senha: ")

            emailConfirma = input("Confirme seu email: ")
            while emailConfirma not in email:
                emailConfirma = input('Dados inválidos. Por favor, informe seu email: ')

            alterar_dados_senha = "UPDATE tb_usuario SET senha = '" + novaSenha + "' WHERE email = '" + email + "';";
            cursor.execute(alterar_dados_senha)
            con.commit()
            print("Senha alterada!")
            print("_______________________________________________________")

        elif numero in "2":
            lembrarSenha = input("Confirme seu email para receber a senha: ")
            while lembrarSenha not in email:
                lembrarSenha = input('Dados inválidos. Por favor, informe seu email: ')

            lembrar_senha = "SELECT senha FROM tb_usuario WHERE email = '" + email + "';";
            cursor.execute(lembrar_senha)
            print("Sua senha: ", novaSenha)
            print("_______________________________________________________")

        elif numero in "3":
            deletaUsuario = input("Confirme seu email para deletar: ")
            while deletaUsuario not in email:
                deletaUsuario = input('Dados inválidos. Por favor, informe seu email: ')

            deleta_usuario = "DELETE FROM tb_usuario WHERE email = '" + email + "';";
            cursor.execute(deleta_usuario)
            con.commit()
            print("Usuario deletado!")
            print("_______________________________________________________")
