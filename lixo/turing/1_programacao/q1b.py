def inverte_email(email):
    meio = len(email) //  2
    
    parte1 = email[:meio]
    parte2 = email[meio:]
    
    parte1_invertida = parte1[::-1]
    parte2_invertida = parte2[::-1]
    
    email_parcialmente_corrigido = parte1_invertida + parte2_invertida
    
    partes = email_parcialmente_corrigido.split('@')
    
    if len(partes) ==   2 and partes[1] == 'usp.br':
        return partes[0] + '@' + partes[1]
    else:
        return "ERRO"
    
def corrige_emails(emails):
    emails_corrigidos = []
    for email in emails:
        email_corrigido = inverte_email(email)
        emails_corrigidos.append(email_corrigido)
    return emails_corrigidos


emails_embaralhados = ["id_atanerrb.psu@av", "t.alalalimacrb.repsu@ppo", ".orbmem_ovonrb.psu@gnirut"]
emails_corrigidos = corrige_emails(emails_embaralhados)
print(emails_corrigidos) 
