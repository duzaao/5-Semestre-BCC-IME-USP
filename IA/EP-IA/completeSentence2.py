import math
from UpperClasses import Problem, LanguageModel

class CompleteSentence2(Problem, LanguageModel):
    def __init__(self, texto, n, frase_inicial):
        """
        Função de inicialização do modelo, não a modifique.
        """
        LanguageModel.__init__(self, texto, n)
        self.frase_inicial = frase_inicial
    """
    Daqui para cima são funções relacionadas com preparar o modelo.
    Daqui para baixo são funções relacionadas com a busca.
    """ 

    def initialState(self):
        """
        Retorna uma tupla de tuplas contendo N marcadores de sentença e o tamanho das sentenças a principio  iguais  a 0.
        """
        words = self.frase_inicial.split()
        x = 0

        if len(words) < self.N:
            words = ['<s>'] * (self.N - len(words)) + words

        return (tuple(words[-self.N:]), x)

    
    def isGoal(self, estado):
        """
        Testa se estado é um final de frase.
        """
        return estado[0][-1] == '</s>'

    def actions(self, estado):
        """
        Retorna a lista de ações aplicáveis a estado.
        """
        context = estado[0][-(self.N - 1):]

        valid_actions = []
        new_ngram2 = context + ('</s>',)

        if new_ngram2 in self.n_grams:
            valid_actions.append('</s>')

        for word in self.vocabulary:
            new_ngram = context + (word,)

            if new_ngram in self.n_grams:
                valid_actions.append(word)

        return valid_actions

    
    def result(self, estado, acao):
        """
        Retorna o estado resultante de aplicar acao em estado e incrementa o numero x a cada vez.
        """
        estado, x = estado 
         
        return (estado[1:] + (acao,), x + 1)

    def cost(self, estado1, acao, estado2):
        """
        Retorna o -log da probabilidade de ir de estado1 para estado2 aplicando acao.
        """
        contexto = estado2[0][:-1] 
        return ( -math.log(self.n_grams[contexto + (acao,)] / self.n_grams_smaller[contexto]) / estado2[1] )
