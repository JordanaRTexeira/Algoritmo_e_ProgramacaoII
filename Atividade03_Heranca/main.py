from Aluno            import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao   import AlunoGraduacao

aluno = Aluno(3471 , "Giovane", "7341")
aluno.imprimirAluno()

aluno_2 = AlunoEnsinoMedio(1524 , "Sophia", "4528", "2º")
aluno_2.imprimirAlunoEnsinoMedio()

aluno_3 = AlunoGraduacao(7327 , "Luana", "181710","3º")
aluno_3.imprimirAlunoGraduacao()

