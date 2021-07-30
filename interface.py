import socket

HOST = 'localhost' # maquina onde esta o par passivo
PORTA = 5000        # porta que o par passivo esta escutando

# cria socket
sock = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

# conecta-se com o par passivo
sock.connect((HOST, PORTA))

while True:
	arq = input('Insira o nome do arquivo:\n')
	if len(arq):
		break
	else:
		print("Tente novamente!")
if '.' not in arq:
	arq = arq + '.txt'

while True:
	palavra = input("Insira palavra a ser procurada:\n")
	if len(palavra):
		break
	else:
		print("Tente novamente!")

mensagem = arq + '\n' + palavra

sock.send(mensagem.encode('utf-8'))

#espera a resposta do par conectado (chamada pode ser BLOQUEANTE)
msg = sock.recv(1024) # argumento indica a qtde maxima de bytes da mensagem
mensagem = str(msg, encoding='utf-8')

try:
	mensagem = int(mensagem)
	print('Ocorrências da palavra "{}": {}'.format(palavra, str(mensagem)))
except:
	print("Erro ao ler arquivo: arquivo não foi encontrado.")

# encerra a conexao
sock.close() 