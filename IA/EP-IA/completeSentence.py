import math
from UpperClasses import Problem, LanguageModel

class CompleteSentence(Problem, LanguageModel):
    def __init__(self, texto, n, frase_inicial):
        """
        Função de inicialização do modelo, não a modifique.
        """
        Problem.__init__(self)
        LanguageModel.__init__(self, texto, n)
        self.frase_inicial = frase_inicial

    """
    Daqui para cima são funções relacionadas com preparar o modelo.
    Daqui para baixo são funções relacionadas com a busca.
    """ 
    def initialState(self):
        """
        Retorna uma tupla contendo N marcadores de sentença.
        """
        words = self.frase_inicial.split()

        if len(words) < self.N:
            words = ['<s>'] * (self.N - len(words)) + words

        return tuple(words[-self.N:])

    
    def isGoal(self, estado):
        """
        Testa se estado é um final de frase.
        """
        return estado[-1] == '</s>'

    def actions(self, estado):
        """
        Retorna a lista de ações aplicáveis a estado.
        """
        context = estado[-(self.N - 1):]

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
        Retorna o estado resultante de aplicar acao em estado.
        """
        return estado[1:] + (acao,)

    def cost(self, estado1, acao, estado2):
        """
        Retorna o -log da probabilidade de ir de estado1 para estado2 aplicando acao.
        """
        contexto = estado2[:-1] 
        return -math.log(self.n_grams[contexto + (acao,)] / self.n_grams_smaller[contexto])

