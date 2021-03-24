from Aluno import Aluno

class AlunoGraduacao:
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimirAlunoGraduacao(self):
        print(f"\n--- DADOS GRADUAÇÃO --- \n -Codigo Aluno(a): {self.codigo} \n -Nome: {self.nome} \n -Matricula: {self.matricula}"
              f"\n -Semestre: {self.semestre}")