import subprocess

def so():
    """ retorna uma str com o sistema operacional da máquina, é possível alterar
    a função para pegar outras informações, porém atentar-se a  decodificação da saída
    subprocess.check_output('systeminfo')"""
    
    a = str(subprocess.check_output('systeminfo')) # info do sistema em str
    a = a.split(f'Nome do sistema operacional:               ') # separa a informação desejada, no caso sistema operacional
    a = a[1].split(f'\\r\\n')
    
    return a[0]