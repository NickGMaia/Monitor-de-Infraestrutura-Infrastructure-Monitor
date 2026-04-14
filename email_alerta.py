import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import ssl

load_dotenv()

def enviar_email(alertas):

    if not alertas:
        return
    
    smtp_server = "smtp.gmail.com"
    port = 465
    mensagem = '\n'.join(alertas)

    msg = MIMEMultipart()
    msg['From'] = os.getenv('EMAIL_REMETENTE')
    msg['To'] = os.getenv('EMAIL_DESTINATARIO')
    msg['Subject'] = "Alerta de monitoramento"
    
    anexo = MIMEApplication(open('relatorio_monitoramento.xlsx', 'rb').read())
    anexo.add_header('Content-Disposition', 'attachment', filename='relatorio_monitoramento.xlsx')
    msg.attach(MIMEText(mensagem, 'plain'))
    msg.attach(anexo)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(os.getenv('EMAIL_REMETENTE'), os.getenv('EMAIL_SENHA'))
            server.send_message(msg)
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
