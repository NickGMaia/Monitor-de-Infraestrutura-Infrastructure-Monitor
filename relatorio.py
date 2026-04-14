import sqlite3
import pandas as pd



def buscar_dados():
    conn = sqlite3.connect("monitor.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM maquinas')
    historico_de_uso = cursor.fetchall()
    nomes_coluna = [coluna[0] for coluna in cursor.description]
    conn.close()
    return historico_de_uso, nomes_coluna

def gerar_relatorio():
    dados, colunas = buscar_dados()
    df = pd.DataFrame(dados,columns=colunas)
    df.to_excel('relatorio_monitoramento.xlsx',index=False)
    df.to_csv('dados.csv',index=False)