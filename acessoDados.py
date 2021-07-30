import socket

HOST = ''    # '' possibilita acessar qualquer endereco alcancavel da maquina local
PORTA = 6000  # porta onde chegarao as mensagens para essa aplicacao

# cria um socket para comunicacao
sock = socket.socket() # valores default: socket.AF_INET, socket.SOCK_STREAM  

# vincula a interface e porta para comunicacao
sock.bind((HOST, PORTA))

# define o limite maximo de conexoes pendentes e coloca-se em modo de espera por conexao
sock.listen(1) 

# aceita a primeira conexao da fila (chamada pode ser BLOQUEANTE)
novoSock, endereco = sock.accept() # retorna um novo socket e o endereco do par conectado
print ('Conectado com: ', endereco)
print()

msg = novoSock.recv(1024) # argumento indica a qtde maxima de dados
mensagem = str(msg, encoding='utf-8')
print("Mensagem recebida: {}".format(mensagem))

erro = False
text = ""
# Tenta ler o arquivo. Caso não consiga, a exceção disparada coloca a bool 'erro' como True.
try:
	file = open(mensagem, "r")
	for line in file:
		text += line
except:
	erro = True

print("Mandando mensagem de volta para lado ativo!\n")
# envia mensagem de resposta
if not erro:
	novoSock.send(text.encode('utf-8'))
else:
	novoSock.send("Arquivo não encontrado".encode('utf-8'))

# fecha o socket da conexao
novoSock.close() 

# fecha o socket principal
sock.close() 
