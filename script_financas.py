from financas.models import Transacao
from django.contrib.auth.models import User
from datetime import date

u = User.objects.get(id=1)

dados = [
    ("Salário", "R", 3500, "2025-01-05", "Trabalho"),
    ("Aluguel", "D", 1200, "2025-01-07", "Moradia"),
    ("Internet", "D", 120, "2025-01-10", "Serviços"),
    ("Água", "D", 75, "2025-01-11", "Serviços"),
    ("Luz", "D", 180, "2025-01-12", "Serviços"),
    ("Mercado", "D", 430, "2025-01-15", "Supermercado"),
    ("Venda de Notebook", "R", 2000, "2025-01-16", "Vendas"),
    ("Cinema", "D", 45, "2025-01-17", "Lazer"),
    ("Jantar", "D", 120, "2025-01-18", "Alimentação"),
    ("Gasolina", "D", 230, "2025-01-20", "Transporte"),
    ("Freelance Website", "R", 1600, "2025-01-22", "Freelance"),
    ("Remédio", "D", 60, "2025-01-23", "Saúde"),
    ("Academia", "D", 89, "2025-01-24", "Esportes"),
    ("Padaria", "D", 26, "2025-01-25", "Alimentação"),
    ("Café da manhã", "D", 18, "2025-01-26", "Alimentação"),
    ("Pagamento Cliente X", "R", 950, "2025-01-27", "Freelance"),
    ("Conserto Celular", "D", 280, "2025-01-28", "Manutenção"),
    ("Venda de bicicleta", "R", 750, "2025-01-29", "Vendas"),
    ("Presente de aniversário", "D", 110, "2025-01-30", "Presentes"),
    ("Aplicativo de streaming", "D", 32, "2025-02-02", "Assinaturas"),
    ("Salário", "R", 3500, "2025-02-05", "Trabalho"),
    ("Aluguel", "D", 1200, "2025-02-07", "Moradia"),
    ("Supermercado", "D", 410, "2025-02-10", "Supermercado"),
    ("Almoço", "D", 37, "2025-02-11", "Alimentação"),
    ("Combustível", "D", 250, "2025-02-12", "Transporte"),
    ("Freelance App", "R", 1200, "2025-02-13", "Freelance"),
    ("Luz", "D", 190, "2025-02-14", "Serviços"),
    ("Internet", "D", 120, "2025-02-15", "Serviços"),
    ("Farmácia", "D", 70, "2025-02-16", "Saúde"),
    ("Academia", "D", 89, "2025-02-17", "Esportes"),
    ("Padaria", "D", 24, "2025-02-18", "Alimentação"),
    ("Venda de livros", "R", 160, "2025-02-19", "Vendas"),
    ("Parcela Notebook", "D", 250, "2025-02-20", "Parcelamentos"),
    ("Cinema", "D", 42, "2025-02-21", "Lazer"),
    ("Pagamento Cliente Y", "R", 850, "2025-02-22", "Freelance"),
    ("Presentes", "D", 180, "2025-02-23", "Presentes"),
    ("Doces", "D", 12, "2025-02-24", "Alimentação"),
    ("Streaming", "D", 32, "2025-02-25", "Assinaturas"),
    ("Salário", "R", 3500, "2025-03-05", "Trabalho"),
    ("Aluguel", "D", 1200, "2025-03-07", "Moradia"),
    ("Mercado", "D", 390, "2025-03-08", "Supermercado"),
    ("Gasolina", "D", 220, "2025-03-09", "Transporte"),
    ("Venda de TV", "R", 1250, "2025-03-10", "Vendas"),
    ("Conserto carro", "D", 480, "2025-03-11", "Manutenção"),
    ("Almoço", "D", 35, "2025-03-12", "Alimentação"),
    ("Freelance Design", "R", 1350, "2025-03-13", "Freelance"),
    ("Academia", "D", 89, "2025-03-14", "Esportes"),
    ("Internet", "D", 120, "2025-03-15", "Serviços"),
]

for d in dados:
    Transacao.objects.create(
        descricao=d[0],
        tipo=d[1],
        valor=d[2],
        data=d[3],
        categoria=d[4],
        usuario=u
    )
