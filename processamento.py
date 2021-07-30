import socket

HOST = ''    # '' possibilita acessar qualquer endereco alcancavel da maquina local
PORTA = 5000  # porta onde chegarao as mensagens para essa aplicacao

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

# depois de conectar-se, espera uma mensagem (chamada pode ser BLOQUEANTE))
msg = novoSock.recv(1024) # argumento indica a qtde maxima de dados
mensagem = str(msg, encoding='utf-8')
arquivo = mensagem.split('\n')[0]
palavra = mensagem.split('\n')[1]
print("Mensagem recebida: {}".format(mensagem))
print("Arquivo considerado: {}\nPalavra considerada: {}".format(arquivo, palavra))

# Início do bloco de código que faz a comunicação com acessoDados.py
HOST2 = 'localhost'
PORTA2 = 6000
# cria socket
sock2 = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

# conecta-se com o par passivo
sock2.connect((HOST2, PORTA2))
sock2.send(arquivo.encode('utf-8'))

#espera a resposta do par conectado (chamada pode ser BLOQUEANTE)
msg2 = sock2.recv(1024) # argumento indica a qtde maxima de bytes da mensagem
mensagem2 = str(msg2, encoding='utf-8')

# encerra a conexao
sock2.close() 
# Fim do bloco de código que faz a comunicação com acessoDados.py

if mensagem2 == 'Arquivo não encontrado':
	msg = "Erro ao ler arquivo: arquivo não foi encontrado."
	print(msg)
else:
	print("\nMensagem recebida: {}\n".format(mensagem2))
	msg = str(mensagem2.count(palavra))

print("Mandando mensagem de volta para lado ativo!\n")
# envia mensagem de resposta
novoSock.send(msg.encode('utf-8'))

# fecha o socket da conexao
novoSock.close() 

# fecha o socket principal
sock.close() 
