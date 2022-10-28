from model.aluno import Aluno
from model.cidade import Cidade
from model.endereco import Endereco
from model.funcionario import Funcionario
from model.gestorApp import GestorApp
from model.instituicaoDeEnsino import InstituicaoDeEnsino
from model.motorista import Motorista
from model.passageiro import Passageiro
from model.pessoa import Pessoa
from model.prefeito import Prefeito
from model.prefeitura import Prefeitura
from model.rota import Rota
from model.uf import Uf
from model.veiculo import Veiculo

aluno = Aluno("Gleidson", "12-12-2012","gleidson@gmail.com","8888-8888","IFPB","TSI","202223")
print(aluno)
cidade = Cidade("Guarabira")
endereco = Endereco("59220-000","13","Quadra 2","Posto Sao Jose","Rua X Bairro Y")
funcionario = Funcionario("Pedro","20-12-1990","pedro@gmail.com","0000-0000","PrefGBA","AuxADM")
gestorapp = GestorApp("Ricardo","12-12-1960","ricardo@gmail.com","7777-7777")
instituicaodeensino = InstituicaoDeEnsino("IFPB","Rua x bairro Y","1234-5678")
motorista = Motorista("Erick","30-02-2000","erick@gmail.com","1111-1111","PrefSolanea","Condutor","sol-gba")
passageiro = Passageiro("Gleidson", "12-12-2012","gleidson@gmail.com","8888-8888","IFPB","TSI","202223", "Bananeiras","Guarabira")
prefeito = Prefeito("Joao","10-10-2010","joao@gmail.com","5555-5555")
prefeitura = Prefeitura("Laura","prefeituragba@gmail.com","4444-4444")
rota = Rota("Guarabira","20","Onibus","Gleidson","12:30","13:10")
uf = Uf("Paraiba","PB")
veiculo = Veiculo("Solanea","20","Onibus","ABC-2345")