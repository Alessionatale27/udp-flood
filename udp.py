import socket
import random

def generate_random_bytes(size):
    return bytes(random.getrandbits(8) for _ in range(size))

def send_udp_packets(ip, porta, numero_pacchetti):
    packet_size = 1024  
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        for i in range(numero_pacchetti):
            packet = generate_random_bytes(packet_size)
            udp_socket.sendto(packet, (ip, porta))
            print(f"Pacchetto {i + 1} inviato a {ip}:{porta}")

def main():
    ip = input("Inserisci l'indirizzo IP del destinatario: ")
    porta = int(input("Inserisci la porta del destinatario: "))
    numero_pacchetti = int(input("Inserisci il numero di pacchetti da inviare: "))

    send_udp_packets(ip, porta, numero_pacchetti)

if __name__ == "__main__":
    main()
