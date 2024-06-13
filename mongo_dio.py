from http import client

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pymongo import MongoClient


Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    saldo = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship('Cliente', back_populates='contas')


engine = create_engine('sqlite:///banco.db')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

# Inserir dados no banco de dados
cliente1 = Cliente(nome='João Silva', idade=30)
cliente2 = Cliente(nome='Maria Souza', idade=25)

conta1 = Conta(tipo='Corrente', saldo=1000.0, cliente=cliente1)
conta2 = Conta(tipo='Poupança', saldo=1500.0, cliente=cliente1)
conta3 = Conta(tipo='Corrente', saldo=2000.0, cliente=cliente2)

session.add_all([cliente1, cliente2, conta1, conta2, conta3])
session.commit()


clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f'Cliente: {cliente.nome}, Idade: {cliente.idade}')
    for conta in cliente.contas:
        print(f'  Conta: {conta.tipo}, Saldo: {conta.saldo}')



db = client['banco']
colecao_clientes = db['clientes']


clientes_mongodb = []
for cliente in clientes:
    cliente_dict = {
        'nome': cliente.nome,
        'idade': cliente.idade,
        'contas': [{'tipo': conta.tipo, 'saldo': conta.saldo} for conta in cliente.contas]
    }
    clientes_mongodb.append(cliente_dict)

colecao_clientes.insert_many(clientes_mongodb)


for cliente in colecao_clientes.find():
    print(f'Cliente: {cliente["nome"]}, Idade: {cliente["idade"]}')
    for conta in cliente['contas']:
        print(f'  Conta: {conta["tipo"]}, Saldo: {conta["saldo"]}')
