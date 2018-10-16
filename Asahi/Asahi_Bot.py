import random

print('Asahi: Olá, prazer em te conhecer, meu nome é Asahi, estou aqui para te auxiliar com qualquer medicamento!\n'
      'Asahi: Você pode visualizar a lista de comandos ao digitar "Lista"')

while True:
    ConvInicial = str(input('Você: '))
    if ConvInicial == 'Lista':
        Lista = ['♟♟♟ (1) Iniciar Consulta ♟♟♟', '• Não estou me sentindo bem', '• Preciso de ajuda',
                 '• Estou com dor', '• Não estou passando bem', '♟♟♟ (2) Opções ♟♟♟',
                 '• Estou com dor de cabeça', '• Estou com enxaqueca', '• Estou com dor de garganta',
                 '• Estou com dor abdominal']
        for var in Lista:
            print(var)
    elif ConvInicial == 'Não estou passando bem' or ConvInicial == 'Não estou me sentindo bem' \
            or ConvInicial == 'Estou com dor' or ConvInicial == 'Preciso de ajuda':
        print('Asahi: O que você está sentindo?')
        RespDor = input('Você: ')
        if RespDor == 'Estou com dor de cabeça' or RespDor == 'Dor de cabeça' or RespDor == 'Minha cabeça dói':
            Randomizar = ['Neosaldina', 'Dorflex', 'Advil', 'Tylenol', 'Aspirina', 'Naldecon']
            Randomizar = random.choice(Randomizar)
            print('Asahi: Você pode usar um {} para aliviar sua dor!'.format(Randomizar))
        elif RespDor == 'Estou com enxaqueca':
            Randomizar = ['Paracetamol', 'Ibuprofeno', 'Aspirina']
            Randomizar = random.choice(Randomizar)
            print('Asahi: Você pode usar um {} para aliviar sua enxaqueca!'.format(Randomizar))
        elif RespDor == 'Estou com dor de garganta':
            Randomizar = ['Paracetamol', 'Dipirona', 'Ibuprofeno', 'Diclofenaco', 'Nimesulida', 'Piroxicam',
                          'Celecoxibe']
            Randomizar = random.choice(Randomizar)
            print('Asahi: Você pode usar um {} para aliviar sua dor de garganta!'.format(Randomizar))
        elif RespDor == 'Estou com dor abdominal':
            Randomizar = ['Cimetidina', 'Digeplus', 'Dimeticona', 'Domperidona', 'Dipirona', 'Dimezin']
            Randomizar = random.choice(Randomizar)
            print('Asahi: Você pode usar um {} para aliviar sua dor abdominal!'.format(Randomizar))
            break
    else:
        NaoEntendi = ['Asahi: Não entendi, poderia ser mais claro?',
                      'Asahi: Comando inválido, em caso de dúvidas digite "Lista"',
                      'Asahi: Se essa for sua primeira vez, digite "Lista" para mais informações!',
                      'Asahi: Tente: "Lista" para visualizar todos os comandos!',
                      'Asahi: Precisa de ajuda? Tente escrever "Lista" para mais informações!']
        NaoEntendi = random.choice(NaoEntendi)
        print(NaoEntendi)
