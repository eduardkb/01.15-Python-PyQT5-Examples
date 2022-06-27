import re

def fValidaCPF(sCPF):
    sCPF = str(sCPF)

    sCPF = re.sub(r'[^0-9]', '', sCPF)
    if not sCPF or len(sCPF) != 11:
        return False
    novo_cpf = sCPF[:-2]
    reverso = 10                        # Contador reverso
    total = 0                           # O total das multiplicações

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # evita que CPF seja uma sequencia
    sequencia = novo_cpf == str(novo_cpf[0]) * len(sCPF)

    if sCPF == novo_cpf and not sequencia:
        return True
    else:
        return False

def fFormataCPF(sCPF):
    if len(sCPF) == 11:
        cpfFormatado = '{}.{}.{}-{}'.format(sCPF[:3], sCPF[3:6], sCPF[6:9], sCPF[9:])
        return cpfFormatado
    else:
        return sCPF

