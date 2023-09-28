import socket

def scan_port(host, port):
    try:
        # Cria um objeto socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define um timeout curto para a conexão
        sock.settimeout(1)
        # Tenta se conectar à porta especificada
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"A porta {port} está aberta.")
        else:
            print(f"A porta {port} está fechada.")
        sock.close()
    except KeyboardInterrupt:
        print("Varredura interrompida.")
    except socket.error:
        print("Não foi possível se conectar ao host.")

def main():
    host = input("Digite o endereço IP ou nome de domínio: ")
    for port in range(1, 1025):  # Varre as portas de 1 a 1024
        scan_port(host, port)

if __name__ == "__main__":
    main()