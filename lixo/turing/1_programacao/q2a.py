def verifica_ordem_crescente(episodios):
    ultimo_tempo = -1
    x = 1
    for episodio in episodios:
        if x != episodio[0]:
            x = episodio[0]
            ultimo_tempo = -1
        if episodio[1] <= ultimo_tempo:
            return False
        ultimo_tempo = episodio[1]
    return True

def organiza_listas(qtd_projetos, episodios, min_passos):
    ans = ""
    somas = [0] * qtd_projetos  
    resposta = [[] for _ in range(qtd_projetos)]  
    episodios_ordenados = sorted(episodios, key=lambda x: x[0])
    if(verifica_ordem_crescente(episodios_ordenados)):
        ans = "sim"
    else:
        ans = "nao"
        return ans,resposta 
    
    for episodio in episodios_ordenados:
        id_projeto, _, passos = episodio
        somas[id_projeto - 1] += passos
    
    for i, soma in enumerate(somas):
        if soma >= min_passos:
            resposta[i] = [episodio for episodio in episodios_ordenados if episodio[0] == i + 1]
        else:
            resposta[i] = []

    if all(not sublist for sublist in resposta):
        ans = "nao"
    #print(somas)
    return ans, resposta

# Exemplo de uso:
resultado = organiza_listas(3, [[1, 1, 10],
[1, 2, 20],
[2, 5, 30],
[3, 10, 50],
[3, 12, 100],
[1, 8, 60], [2, 6, 100],
[1, 25, 100],
[3, 15, 100],
[1, 30, 80]], 250)

print(resultado)
