#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep as esperar
import os
import filecmp
import requests

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

roxo = "\033[1;35m"
roxo_claro = "\033[1;95m"
resetar = "\033[0;0m"
branco = "\033[0;37m"

def logo():
    logo.texto = """ __          ___            _____ ______ _   _ 
 \ \        / (_)          / ____|  ____| \ | |
  \ \  /\  / / _ ___ _ __ | |  __| |__  |  \| |
   \ \/  \/ / | / __| '_ \| | |_ |  __| | . ` |
    \  /\  /  | \__ \ |_) | |__| | |____| |\  |
     \/  \/   |_|___/ .__/ \_____|______|_| \_|
                    | |                        
                    |_|                        """

logo()
logo = logo.texto

def start():
    limpar()
    print(roxo+logo)
    print(branco)
    


limpar()
input("Código totalmente aberto, caso modifique deixe livre para todos\nAss: WispSSH")

def vless():
    try:
        start()
        print("Qual vai ser o nome do link?")
        nome = input('> ')
        start()
        print("Qual link ira utilizar para gerar?")
        vless_link = input('> ')
        start()
        print("Qual proxy deseja utilizar?")
        print("""
1 - 104.16.18.94 (vivo e tim)
2 - cdn.jsdelivr.net (claro)
3 - mobilidade.cloud.caixa.gov.br (universal)
4 - Defina sua proxy
        """)
        proxy = input('> ')
        if proxy == "1":
            proxy = '104.16.18.94'
        elif proxy == "2":
            proxy = 'cdn.jsdelivr.net'
        elif proxy == "3":
            proxy = 'mobilidade.cloud.caixa.gov.br'
        elif proxy == "4":
            start()
            print('Defina sua proxy modificada')
            proxy = input('> ')
        else:
            print('Opção não encontrada')
            return vless()

        uuid = vless_link.split('//')[1].split('@')[0]
        porta = vless_link.split(':')[2].split('?')[0].split('/')[0]
        caminho = vless_link.split('path=')[1].split('#')[0].split('&security')[0]
        server = vless_link.split('@')[1].split(':')[0]



        link = (f'vless://{uuid}@{proxy}:{porta}?path={caminho}&security=tls&encryption=none&host={server}&type=ws&sni={server}#{nome}')
        
        start()

        print(f"""
NOME : {nome}
UUID : {uuid}
SERVER : {server}
PROXY : {proxy}
PORTA : {porta}
CAMINHO : {caminho}

Link Gerado

{link}
        """)
    except:
        print('Ocorreu algum erro')
        esperar(3)
        return menu()

def atualizar():
    url = 'https://raw.githubusercontent.com/WispSSH/WispSSH-V2RAY-GEN/main/wispssh-gen.py'
    r = requests.get(url, allow_redirects=True).content
    open('wispssh-gen.py', 'wb').write(r)

def menu():
    limpar()
    url = 'https://raw.githubusercontent.com/WispSSH/WispSSH-V2RAY-GEN/main/wispssh-gen.py'
    r = requests.get(url, allow_redirects=True).content
    open('atualizar.py', 'wb').write(r)
    status = filecmp.cmp('atualizar.py', 'wispssh-gen.py')
    os.remove('atualizar.py')
    if status == True:
        status = ('Atualizado ✅')
    elif status == False:
        status = ('Desatualizado ❌')
    start()
    
    print(f"""
Qual modo deseja gerar o link?

Status : {status}
1 - Vless
2 - Vmess
3 - Trojan
4 - Atualizar
    """)
    menu_escolha = input('> ')
    if menu_escolha == "1":
        vless()
    elif menu_escolha == "2":
        print('Ainda não está disponível')
    elif menu_escolha == "3":
        print('Ainda não está disponível')
    elif menu_escolha == "4":
        atualizar()
    else:
        print('Opção Inexistente')
        return menu()

menu()
