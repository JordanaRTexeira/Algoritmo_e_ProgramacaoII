from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

print("---- PESSOA ----")
pessoa = Pessoa(373, "Gabriel", "Av. Otto Niemeyer", "32631142")
pessoa.imprimirNome()
pessoa.__imprimirTelefone()

print("---- PESSOA FÍSICA ----")
pessoaFisica = Fisica(347, "Giovanna", "Av. Borges de Medeiros", 32631145, 86135010032, 22, 65, 1.70)
pessoaFisica.imprimirCPF()
pessoaFisica.__calcularIMC()

print("---- PESSOA JURÍDICA ----")
pessoaJuridica = Juridica(773, "Sophia", "R. José do Patrocínio", 32432720, 86142311074, 3437, 28)
pessoaJuridica.imprimirCNPJ()
pessoaJuridica.__emitirNotaFiscal()