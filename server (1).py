import socket
tcp_port = 23
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind(('10.0.0.54',tcp_port))
s.listen(5)

while True:
	conn,adr = s.accept()
	conn.send(bytes("  _    _      _ _        __          __        _     _ \n | |  | |    | | |       \ \        / /       | |   | |\n | |__| | ___| | | ___    \ \  /\  / /__  _ __| | __| |\n |  __  |/ _ \ | |/ _ \    \ \/  \/ / _ \| '__| |/ _` |\n | |  | |  __/ | | (_) |    \  /\  / (_) | |  | | (_| |\n |_|  |_|\___|_|_|\___/      \/  \/ \___/|_|  |_|\__,_|","ascii"))
	conn.close()