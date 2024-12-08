def calculate_equation(inputs):
    I = inputs["amperagem"]
    V = inputs["tensao"]
    n = inputs["n"]
    velocidadeSoldagem = inputs["velocidadeSoldagem"]
    Tp = inputs["tp"]
    To = inputs["to"]
    p = inputs["densidade"]
    Cp = inputs["calorEspecifico"]
    t = inputs["espessuraChapa"]
    Tm = inputs["temperaturaFusao"]

    Ht = (I * V * n * 60) / velocidadeSoldagem
    resulUm = 1 / (Tp - To)
    resulDois = (4.13 * ((p * Cp) / 1_000_000_000) * t) / Ht
    resulTres = 1 / (Tm - To)
    resultadoAdams = (resulUm - resulTres) / resulDois

    temperatura_distancia = [
        (i, round(1 / (((4.13 * ((p * Cp) / 1_000_000_000) * t * i) / Ht) + resulTres) + To))
        for i in range(int(inputs["distancia"]) + 1)
    ]

    temperatura_tempo = [
        ((60 / velocidadeSoldagem) * ciclo[0], ciclo[1]) for ciclo in temperatura_distancia
    ]

    return {
        f"Valor de Y em {Tp}° é:": f"{round(resultadoAdams, 2)} mm",
        "Heat Input (Ht)": f"{Ht} J/mm",
        "data_distancia": temperatura_distancia,
        "data_tempo": temperatura_tempo,
    }
