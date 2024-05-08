def conta_economia(emails):
    economia_total = 0
    for i in range(1, len(emails)):
        email_atual = emails[i]
        email_anterior = emails[i - 1]
        economia = 0
        for j in range(len(email_atual)):
            if email_atual[j] == email_anterior[j]:
                economia += 1
            else:
                break
        economia_total += economia
    return economia_total

economia = conta_economia(["davi.turing.cp@usp.br",
"diva.turingusp@usp.br",
"diva.estudausp@usp.br",
"renatah.turing@usp.br",
"reginaldo.fake@usp.br"])
print(economia)  