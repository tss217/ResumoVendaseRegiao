#list

vendas = [
    {"produto": "Caneca", "quantidade": 3, "preco_unitario": 25.0, "regiao": "Sul"},
    {"produto": "Camiseta", "quantidade": 2, "preco_unitario": 50.0, "regiao": "Sudeste"},
    {"produto": "Caneca", "quantidade": 1, "preco_unitario": 25.0, "regiao": "Sul"},
    {"produto": "Boné", "quantidade": 5, "preco_unitario": 15.0, "regiao": "Nordeste"},
]


#função pra determina vendads por região
def salesForTheRegion(sales):
    region = {i["regiao"]:0 for i in sales}

    for x in sales:
        receita = x["quantidade"]*x["preco_unitario"]
        region[x["regiao"]] = region[x["regiao"]] + receita

    return region

#função para determina a quantidade vendida por produto 
def saleUnity(sales):
    product = {i["produto"]:0 for i in sales}

    for x in sales:
        qtd = x["quantidade"]
        product[x["produto"]] = product[x["produto"]]+qtd
    
    return product


print(salesForTheRegion(vendas))

print(saleUnity(vendas))