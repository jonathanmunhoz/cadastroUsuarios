import mysql.connector

dados_conexao = (
    "Driver={SQL Server};"
    "Server=localhost;"
    "Database=db_usuario;"
)

con = mysql.connector.connect(host='localhost',database='db_usuario',user='root',password='root')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)

import csv

with open('dadosUsuarios.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for linha in arquivo_csv:
        print(linha)

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

    elif letra in "Rr": senha = senha + "#"
    elif letra in "Ss": senha = senha + "%"
    elif letra in "Mm": senha = senha + "$"
    else: senha = senha + letra
print('Seu usuário é: ', usuario)
print('Sua senha é: ', senha)

import smtplib
import email.message

def enviar_email():
    corpo_email = '<p>Usuário: ' + usuario + '</p> <p>Senha: ' + senha + '</p>'

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

print('Realize seu Login!')

login = input('Login: ')
senhaLogin = input('Senha: ')
while senhaLogin not in senha:
    senhaLogin = input('Dados inválidos. Por favor, informe sua senha: ')
print('Dados corretos! Por favor, cadastre uma nova senha em seu primeiro login!'.format(senhaLogin))

novaSenha = input('Nova senha: ')
email = input("Digite seu E-mail: ")

alterar_dados = "UPDATE tb_usuario SET senha = '" + novaSenha + "' WHERE email = '" + email + "';";

cursor.execute(alterar_dados)
con.commit()