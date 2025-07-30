Este é um simples **scanner de rede** desenvolvido em Python utilizando a biblioteca `nmap` (python-nmap). O script realiza varreduras em uma faixa de IPs fornecida, identifica hosts ativos, portas abertas e os serviços em execução e exporta os resultados para o tipo de arquivo escolhido.

---

# Funcionalidades

- Varredura TCP (SYN scan) com Nmap
- Detecção de portas abertas e serviços
- Exportação dos resultados para um arquivo `relatorio.csv`
- Suporte a faixas de IP (ex: `192.168.0.0/24`)

---

# Requisitos

- Python 3.6+
- [Nmap](https://nmap.org/) instalado no sistema
- Bibliotecas Python:
  - `pandas`
  - `python-nmap`

# Como usar?
 Em sua CLI copie e cole este comando:
 python scanner.py 192.168.0.0

# Saída
Após a execução, será gerado um arquivo chamado relatorio.csv no diretório atual, contendo as seguintes colunas:
- IP: Endereço IP do host
- Status: Estado do host (ex: up)
- Porta: Porta aberta detectada
- Protocolo: Tipo de protocolo (ex: tcp)
- Serviço: Nome do serviço identificado (ex: http)
