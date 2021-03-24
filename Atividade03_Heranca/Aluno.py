class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo    = codigo
        self.nome      = nome
        self.matricula = matricula


    def imprimirAluno(self):
        print(f"--- DADOS ALUNO --- \n -Codigo Aluno(a): {self.codigo} \n -Nome Aluno(a): {self.nome} \n -Matricula: {self.matricula}")