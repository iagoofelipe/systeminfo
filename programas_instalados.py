import subprocess, webbrowser, pyautogui as ag

def todos_instalados():
    try:
        Data = subprocess.check_output(['winget', 'list']).decode("UTF-8") 
        linhas = Data.split("\r\n") #gera uma lista utilizando "\r\n" como separador
        todos_instalados = []

        for i in linhas:
            if i != linhas[0] and i != linhas[1]: #ignora duas primeiras linhas (título e ---)
                if '   ' in i: #pega a primeira parte da linha (nome do programa)
                    c = i.split('   ')[0]
                
                    if '…' in c: #pega a primeira parte da linha, caso seja grande e esteja abreviado
                        c = c.split('…')[0]
                
                if '(x' in c:
                    c = c.split(" (x",1)[0]
                    
                
                todos_instalados.append(c)
    except:
        webbrowser.open('https://www.microsoft.com/store/productId/9NBLGGH4NNS1')
        ag.alert('Verifique se o winget está disponível em sua máquina!')
        
        

            
    return todos_instalados

ag.alert(todos_instalados())