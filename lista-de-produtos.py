produtos = []
produto1 = {
    "Produto": "arroz",
    "preço": 12.00
}
produto2 = {
    "Produto": "feijão",
    "preço": 8.50
}
produtos.append(produto1)
produtos.append(produto2)
for produto in produtos:
    print(f"produto:{produto['Produto']} | Preço: R$ {produto['preço']:.2f}")