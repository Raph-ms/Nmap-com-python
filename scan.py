import pandas as pd
import nmap
import sys

def scan_rede(ip_range):
    scanner = nmap.PortScanner()
    print("Escaneando rede:", ip_range)
    scanner.scan(hosts = ip_range, arguments="-sS T4")


    resultados = []
 
    for host in scanner.all_hosts():
     status = scanner[host].state()
     for proto in scanner[host].all_protocols():
         portas = scanner[host][proto].keys()
         for porta in portas:
              servico = scanner[host][proto][porta]['name']
              resultados.append({
                    'IP': host,
                    'Status': status,
                    'Porta': porta,
                    'Protocolo': proto,
                    'Serviço': servico
                })

    return resultados

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <IP/Faixa de IP>")
        sys.exit(1)

    ip_range = sys.argv[1]
    dados = scan_rede(ip_range)

    if dados:
        df = pd.DataFrame(dados)
        df.to_csv("relatorio.txt", index=False)
        print("\nRelatório salvo como relatorio.csv")
    else:
        print("Nenhum host ativo encontrado.")
