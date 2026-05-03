# Python OOP + SQLAlchemy + SQL Server

Este projeto demonstra a aplicação de **Programação Orientada a Objetos (OOP)** avançada em pipelines de dados, utilizando o **SQLAlchemy** como ORM para persistência no **SQL Server**.

## Objetivo
O objetivo é gerir uma frota de veículos, garantindo a integridade dos dados e a escalabilidade da arquitetura de base de dados.

## Os 4 Pilares da OOP Aplicados

### 1. Abstração
Utilizamos o `declarative_base()` do SQLAlchemy para abstrair a camada de base de dados. O usuário interage com objetos Python, enquanto o motor (`engine`) traduz essas interações para o dialeto específico do SQL Server (T-SQL).

### 2. Herança (Joined Table Inheritance)
Implementamos a herança de tabelas:
* **Classe Pai (`Veiculo`):** Armazena dados genéricos (marca, modelo).
* **Classe Filha (`CarroEletrico`):** Herda as propriedades do pai e adiciona atributos específicos (capacidade da bateria).
* **Vantagem:** No SQL Server, isto cria duas tabelas relacionadas por chaves estrangeiras, eliminando colunas nulas e redundância.

### 3. Encapsulamento
A lógica de transação é encapsulada em sessões (`session`). Utilizamos o tratamento de exceções (`try/except/rollback`) para garantir que o estado da base de dados permaneça consistente, mesmo em caso de falha na carga.

### 4. Polimorfismo
Através da configuração `polymorphic_on`, o sistema consegue tratar diferentes tipos de veículos sob uma mesma interface, mas instanciando as classes corretas automaticamente no momento da consulta SQL.

##  Tecnologias e Requisitos
* **Python 3.10+**
* **SQLAlchemy:** Mapeamento Objeto-Relacional.
* **pyodbc:** Conector de base de dados.
* **Microsoft SQL Server:** Motor de persistência.
* **Driver ODBC 17:** Necessário para a comunicação entre Python e SQL Server.
