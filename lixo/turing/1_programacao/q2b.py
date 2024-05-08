
def dfs_correcoes(qtd_estados, transicoes, estado_atual, estado_final, max_prof, profundidade=0, sequence=None):
    if sequence is None:
        sequence = [estado_atual]
    
    if profundidade > max_prof:
        #print(f"Profundidade máxima atingida para o estado {estado_atual}")
        return 0
    x = 0
    
    if profundidade > 0 and estado_atual == estado_final:
        #print(f"Encontrou uma correção para o estado {estado_atual} de profundidade {profundidade}")
        x = x +1 
        #print(sequence) # Print the sequence leading to the current lacuna
        if profundidade < max_prof:
            for estado_intermediario in range(1, qtd_estados + 1):
                if transicoes.get((estado_atual, estado_intermediario), 0) == 1:
                    x += dfs_correcoes(qtd_estados, transicoes, estado_intermediario, estado_final, max_prof, profundidade + 1, sequence + [estado_intermediario])
        #print(x)
        return x


    for estado_intermediario in range(1, qtd_estados + 1):
        if transicoes.get((estado_atual, estado_intermediario), 0) == 1:
            x += dfs_correcoes(qtd_estados, transicoes, estado_intermediario, estado_final, max_prof, profundidade + 1, sequence + [estado_intermediario])
    #print(x)
    return x


def conta_correcoes(qtd_estados, transicoes, episodio, max_prof):
    max_prof = max_prof+1
    correcoes_possiveis = 0
    resposta = 0
    x = 0
    
    for i in range(len(episodio) - 1):
        estado_atual = episodio[i]
        estado_final = episodio[i + 1]
        
        if transicoes.get((estado_atual, estado_final), 0) == 0:
            #print(f"Lacuna encontrada de {estado_atual} para {estado_final}")
            correcoes_possiveis = dfs_correcoes(qtd_estados, transicoes, estado_atual, estado_final, max_prof)
            if(correcoes_possiveis != 0):
                if(resposta == 0):
                    resposta = 1
                resposta *= correcoes_possiveis
            else:
                return 0
            


    
    if resposta == 0:
        return -1  # Não há lacunas no episodio
    else:
        return resposta

# Exemplo de uso:
print(conta_correcoes(4,
{(1, 1): 0, (1, 2): 0, (1, 3): 1, (1, 4): 1,
(2, 1): 1, (2, 2): 0, (2, 3): 1, (2, 4): 0,
(3, 1): 0, (3, 2): 1, (3, 3): 0, (3, 4): 1,
(4, 1): 1, (4, 2): 1, (4, 3): 1, (4, 4): 1},
[3, 1, 3, 2, 2, 4], 3))


