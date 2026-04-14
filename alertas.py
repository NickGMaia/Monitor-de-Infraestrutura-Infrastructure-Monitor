
cpu_alert = 80
memoria_alert = 85
disco_alert = 90

def verificar_alertas(dados):
    alertas = []
    if dados["cpu_percent"] > cpu_alert:

        diferenca = round (dados["cpu_percent"] - cpu_alert, 1)
        mensagem = f"AVISO! Uso alto da CPU em: {diferenca}% acima do recomendado"
        alertas.append(mensagem)
        print(mensagem)

    if dados["memoria_percent"]> memoria_alert:

        diferenca = round (dados["memoria_percent"] - memoria_alert, 1)
        mensagem =f"AVISO! Uso alto da Memoria em: {diferenca}% acima do recomendado"
        alertas.append(mensagem)
        print(mensagem)

    if dados["disco_percent"] > disco_alert:

        diferenca = round (dados["disco_percent"] - disco_alert, 1)
        mensagem =f"AVISO! Uso alto do Disco em: {diferenca}% acima do recomendado"
        alertas.append(mensagem)
        print(mensagem)

    return alertas
