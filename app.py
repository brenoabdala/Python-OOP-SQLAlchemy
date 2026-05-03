from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import urllib

# 1. Configuração da Conexão SQL Server (Ajuste os dados abaixo)
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SEU_SERVIDOR;"
    "DATABASE=NOME_DO_BANCO;"
    "UID=USUARIO;"
    "PWD=SENHA"
)
connection_string = f"mssql+pyodbc:///?odbc_connect={params}"

# Criando o Engine
engine = create_engine(connection_string, echo=True) # echo=True mostra o SQL no terminal
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# 2. Definição das Classes (Modelos)
class Veiculo(Base):
    __tablename__ = 'frota_veiculos'

    id = Column(Integer, primary_key=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    tipo = Column(String(20)) 

    # Configuração de Polimorfismo
    __mapper_args__ = {
        'polymorphic_identity': 'combustao',
        'polymorphic_on': tipo
    }

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class CarroEletrico(Veiculo):
    __tablename__ = 'frota_eletricos'
    
    # FK para a tabela pai (Herança de Tabela Unida)
    id = Column(Integer, ForeignKey('frota_veiculos.id'), primary_key=True)
    capacidade_bateria = Column(Float)

    __mapper_args__ = {
        'polymorphic_identity': 'eletrico',
    }

    def __init__(self, marca, modelo, capacidade_bateria):
        super().__init__(marca, modelo) # super() chamando o construtor do pai
        self.capacidade_bateria = capacidade_bateria

# 3. CONDIÇÃO: Criar tabelas se não existirem
# O metadata.create_all checa automaticamente a existência antes de criar
print("Checando/Criando tabelas no SQL Server...")
Base.metadata.create_all(engine)

# 4. Inserção de Dados (Exemplo)
try:
    carro_1 = Veiculo(marca="Volkswagen", modelo="Golf")
    carro_2 = CarroEletrico(marca="Tesla", modelo="Model S", capacidade_bateria=100.0)

    session.add_all([carro_1, carro_2])
    session.commit()
    print("Dados inseridos com sucesso!")
except Exception as e:
    session.rollback()
    print(f"Erro ao inserir: {e}")
finally:
    session.close()
