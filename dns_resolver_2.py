import dns.resolver


try:
    arquivo = open('wordlist.txt')
    subdominios = arquivo.read().splitlines()
except:
    print'Arquivo não encontrado!'
    exit()

dominio = 'dominio'
try:
    dominio = raw_input('Digite o nome do domínio:')
except ValueError:
    print 'Nome inválido!'

for subdominio in subdominios:
    try:
        domesub =  subdominio + '.' + dominio
        resultados = dns.resolver.query(domesub,'a')
        for resultado in resultados:
            print domesub,resultado
    except:
         'Alguns sudomínios podem não ter sido encontrados!'
         

            

            
           
    
    
        
        
        
            

