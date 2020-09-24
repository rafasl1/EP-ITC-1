import sys

arquivo = open('ArqTeste.txt', 'r')
index = 0
numero_de_automatos = 0
numero_de_automatos_lidos = 0
automatos = []
primeira_linha = True
index_do_automato_lido = 0
preenchimento_inicial = False

for linha in arquivo:
	if  preenchimento_inicial and index > automatos[index_do_automato_lido]['numero_de_transicoes'] + 2 + automatos[index_do_automato_lido]['numero_de_cadeias']:
		index = 0;
		index_do_automato_lido += 1
		preenchimento_inicial = False

	if index == 0 and primeira_linha == True:
		numero_de_automatos = linha

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


print(automatos)
arquivo.close()

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