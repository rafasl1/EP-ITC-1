import sys

arquivo_teste = open(sys.argv[1], 'r')
arquivo_saida = open(sys.argv[2], 'w')

index = 0
numero_de_automatos = 0
numero_de_automatos_lidos = 0
automatos = []
primeira_linha = True
index_do_automato_lido = 0
preenchimento_inicial = False
string_de_saida = ''

for linha in arquivo_teste:
	if  preenchimento_inicial and index > automatos[index_do_automato_lido]['numero_de_transicoes'] + 2 + automatos[index_do_automato_lido]['numero_de_cadeias']:
		index = 0;
		index_do_automato_lido += 1
		preenchimento_inicial = False

	if index == 0 and primeira_linha == True:
		numero_de_automatos = int(linha)

		for i in range(int(numero_de_automatos)):
			automatos.append({})
	elif index == 0 and primeira_linha == False:
		parametros = linha.split()
		automatos[index_do_automato_lido]['numero_de_estados'] = int(parametros[0])
		automatos[index_do_automato_lido]['numero_de_simbolos'] = int(parametros[1])
		automatos[index_do_automato_lido]['numero_de_transicoes'] = int(parametros[2])
		automatos[index_do_automato_lido]['index_do_estado_inicial'] = int(parametros[3])
		automatos[index_do_automato_lido]['numero_de_estados_de_aceitacao'] = int(parametros[4])
		automatos[index_do_automato_lido]['transicoes'] = []
		automatos[index_do_automato_lido]['cadeias'] = []

		index += 1
	elif index == 1 and primeira_linha == False:
		automatos[index_do_automato_lido]['estados_de_aceitacao'] = linha.split()
		index += 1
	elif index >= 2 and index <= automatos[index_do_automato_lido]['numero_de_transicoes'] + 1 and primeira_linha == False:
		automatos[index_do_automato_lido]['transicoes'].append(linha.split())
		index += 1
	elif index > automatos[index_do_automato_lido]['numero_de_transicoes'] + 1 and index <= automatos[index_do_automato_lido]['numero_de_transicoes'] + 2 and primeira_linha == False:
		automatos[index_do_automato_lido]['numero_de_cadeias'] = int(linha)
		preenchimento_inicial = True

		index += 1
	elif index > automatos[index_do_automato_lido]['numero_de_transicoes'] + 2 and index <= automatos[index_do_automato_lido]['numero_de_transicoes'] + 2 + automatos[index_do_automato_lido]['numero_de_cadeias'] and primeira_linha == False: 
		automatos[index_do_automato_lido]['cadeias'].append(linha.split())
		index += 1;
	primeira_linha = False


automato_travado = False
cadeia_valida = False

def verificar_cadeira(cadeia, automato, estado_atual):

    if len(cadeia) == 0:
        if str(estado_atual) in automato['estados_de_aceitacao']:
            aux = open('verificacao_automato.txt', 'a')
            aux.write('1 ')
            aux.close()


        else:
            for transicao in automato['transicoes']:
                if int(estado_atual) == int(transicao[0]) and int(transicao[1]) == 0:
                    automato_travado = False
                    cadeia_consumida = cadeia.copy()
                    verificar_cadeira(cadeia_consumida, automato, transicao[2])

        return
    else:
        simbolo_atual = cadeia[0]

        for transicao in automato['transicoes']:

            automato_travado = True

            if int(estado_atual) == int(transicao[0]) and int(simbolo_atual) == int(transicao[1]):
                automato_travado = False
                cadeia_consumida = cadeia.copy()
                cadeia_consumida.pop(0)
                verificar_cadeira(cadeia_consumida, automato, transicao[2])

            if int(estado_atual) == int(transicao[0]) and int(transicao[1]) == 0:
                automato_travado = False
                cadeia_consumida = cadeia.copy()
                verificar_cadeira(cadeia_consumida, automato, transicao[2])


for i in range(numero_de_automatos):
	automato = automatos[i]

	for cadeia in automato['cadeias']:
		verificar_cadeira(cadeia, automato, automato['index_do_estado_inicial'])
		aux = open('verificacao_automato.txt', 'r')

		conteudo = aux.readline()
		aux.close()
		aux = open('verificacao_automato.txt', 'r')

		if not bool(conteudo):
			string_de_saida += '0 '
		for linha in aux:
			vetor = linha.split()
			if('1' in vetor):
				string_de_saida += '1 '
			else :
				string_de_saida += '0 '

		aux.close()
		aux = open('verificacao_automato.txt', 'w')
		aux.write('')
		aux.close()

	string_de_saida += '\n'

arquivo_saida.write(string_de_saida)
arquivo_teste.close()


'''
[
	{
		'numero_de_estados': 2,
		'numero_de_simbolos': 3,
		'numero_de_transicoes': 4,
		'index_do_estado_inicial': 0,
		'numero_de_estados_de_aceitacao': 1,
		'transicoes': [
			['0', '1', '0'],
			['0', '1', '1'],
			['0', '2', '1'],
			['1', '2', '0']
		], 
		'cadeias': [
			['1'], 
			['1', '1'], 
			['1', '1', '1'], 
			['1', '2', '2', '1', '1', '1', '2', '2', '1'], 
			['2', '2', '2', '1'], 
			['2', '1', '2', '2']
		],
		'estados_de_aceitacao': ['0'], 
		'numero_de_cadeias': 6
	},
	{
		'numero_de_estados': 3, 
		'numero_de_simbolos': 3, 
		'numero_de_transicoes': 6, 
		'index_do_estado_inicial': 0, 
		'numero_de_estados_de_aceitacao': 1, 
		'transicoes': [
			['0', '0', '1'], 
			['1', '1', '0'], 
			['0', '1', '2'], 
			['2', '2', '2'], 
			['2', '1', '1'], 
			['2', '2', '1']
		], 
		'cadeias': [
			['0'], 
			['1'], 
			['1', '2', '2', '2', '2', '2', '1'], 
			['1', '1', '1', '2', '1', '1', '1'], 
			['1', '2', '1', '1'], 
			['1', '2', '2', '1', '2', '2'], 
			['2'], 
			['1', '1', '2', '2', '1', '2']
		], 
		'estados_de_aceitacao': ['1'], 
		'numero_de_cadeias': 8
	}
] 
'''