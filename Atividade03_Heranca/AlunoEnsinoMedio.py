from Aluno import Aluno

class AlunoEnsinoMedio:
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimirAlunoEnsinoMedio(self):
        print(f"\n--- DADOS ENSINO MÉDIO --- \n -Codigo Aluno(a): {self.codigo} \n -Nome: {self.nome} \n -Matricula: {self.matricula}"
              f"\n -Ano: {self.ano}")