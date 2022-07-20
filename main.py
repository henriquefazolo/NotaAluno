'''
Ler uma nota de 0 à 10 de um aluno.
Caso o usuário digite um valor inválido, mostrar a mensagem:
"Nota inválida! Digite um valor de 0 à 10!"
'''


class NotaAluno:
    def __init__(self, nota):
        """
        Recebe um valor numero de uma nota

        :param nota: valor da nota do aluno
        """
        self.nota = nota

    def validar_nota(self):
        """
        Valida se a nota esta nos padrões

        :return: Retonar se a nota esta valida ou nao
        """
        if self.nota not in range(0, 11):
            return "Nota inválida! Digite um valor de 0 à 10!"
        else:
            return "Nota válida"


a = NotaAluno(10)
print(a.validar_nota())
