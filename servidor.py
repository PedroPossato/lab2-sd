import socket

HOST = ''    # '' possibilita acessar qualquer endereco alcancavel da maquina local
PORTA = 5000  # porta onde chegarao as mensagens para essa aplicacao

# cria um socket para comunicacao
sock = socket.socket() # valores default: socket.AF_INET, socket.SOCK_STREAM  

# vincula a interface e porta para comunicacao
sock.bind((HOST, PORTA))

# define o limite maximo de conexoes pendentes e coloca-se em modo de espera por conexao
sock.listen(1) 

# Confirma a necessidade de uma nova conexão
novaConexao = True

while True:
	if novaConexao:
		# aceita a primeira conexao da fila (chamada pode ser BLOQUEANTE)
		novoSock, endereco = sock.accept() # retorna um novo socket e o endereco do par conectado
		print ('Conectado com: ', endereco)
		print()
		novaConexao = False # mostra que não é necessária outra conexão no momento

	# depois de conectar-se, espera uma mensagem (chamada pode ser BLOQUEANTE))
	msg = novoSock.recv(1024) # argumento indica a qtde maxima de dados
	mensagem = str(msg, encoding='utf-8')

	# separa a mensagem em arquivo e palavra. Caso não consiga achar a palavra, significa que o comando fim foi executado, logo deve-se encerrar o socket atual
	arquivo = mensagem.split('\n')[0]
	try:
		palavra = mensagem.split('\n')[1]
	except:
		novoSock.close()
		novaConexao = True
		continue
	
	print("Mensagem recebida: {}".format(mensagem))
	print("Arquivo considerado: {}\nPalavra considerada: {}".format(arquivo, palavra))

	erro = False
	text = ""
	# Tenta ler o arquivo. Caso não consiga, a exceção disparada coloca a bool 'erro' como True.
	try:
		file = open(arquivo, "r")
		for line in file:
			text += line
	except:
		print("Erro ao ler arquivo")
		erro = True

	print("Mandando mensagem de volta para lado ativo!\n")
	
	# Retorna uma mensagem de erro em caso de erro, ou o número de ocorrências da palavra, em caso de êxito.
	if erro:
		novoSock.send("Erro ao ler arquivo: arquivo não foi encontrado.".encode("utf-8"))
	else:
		novoSock.send(str(text.count(palavra)).encode("utf-8"))