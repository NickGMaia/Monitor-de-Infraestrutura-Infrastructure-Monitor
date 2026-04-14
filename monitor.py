import psutil
import socket
from datetime import datetime
from alertas import verificar_alertas
from banco import criar_banco, salvar_leitura
from relatorio import gerar_relatorio
from email_alerta import enviar_email
import schedule
import time

def coletar_dados():
    dados = {
        "horario": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memoria_percent": psutil.virtual_memory().percent,
        "memoria_usada_gb": round(psutil.virtual_memory().used / (1024**3), 2),
        "disco_percent": psutil.disk_usage("/").percent,
        "disco_livre_gb": round(psutil.disk_usage("/").free / (1024**3), 2),
        "nome_maquina": socket.gethostname(),  
        "ip_local": socket.gethostbyname(socket.gethostname())
        
    }
    
    return dados



def exibir_dados(dados):
    print("=" * 40)
    print(f" Nome do Host: {dados['nome_maquina']}")
    print(f" IP Local: {dados['ip_local']}")
    print(f" Monitor de Sistema — {dados['horario']}")
    print("=" * 40)
    print(f"  CPU:     {dados['cpu_percent']}%")
    print(f"  Memória: {dados['memoria_percent']}% ({dados['memoria_usada_gb']} GB usados)")
    print(f"  Disco:   {dados['disco_percent']}% ({dados['disco_livre_gb']} GB livres)")
    print("=" * 40)

def executar():
        dados = coletar_dados()
        exibir_dados(dados)
        salvar_leitura(dados)
        gerar_relatorio()
        alertas = verificar_alertas(dados)
        enviar_email(alertas)
    

if __name__ == "__main__":
    criar_banco()
    executar()
    schedule.every(30).minutes.do(executar)

    while True:
        schedule.run_pending()
        time.sleep(1)    