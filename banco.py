import sqlite3

def criar_banco():
    conn = sqlite3.connect("monitor.db")
    cursor = conn.cursor()
    comando_sql = """
    CREATE TABLE IF NOT EXISTS maquinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        nome TEXT NOT NULL,
        horario REAL NOT NULL,
        cpu_usada REAL NOT NULL,
        memoria_livre REAL NOT NULL,
        memoria_usada_gb REAL NOT NULL,
        disco_usado REAL NOT NULL,
        disco_livre_gb REAL NOT NULL
        
    )
    """
    cursor.execute(comando_sql)
    conn.commit()
    conn.close()
    

def salvar_leitura(dados):
    conn = sqlite3.connect("monitor.db")
    cursor = conn.cursor()
    comando_sql = "INSERT INTO maquinas (ip, nome, horario, cpu_usada, memoria_livre, memoria_usada_gb, disco_usado, disco_livre_gb) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

    valores = (
        dados['ip_local'],
        dados['nome_maquina'],
        dados['horario'],
        dados['cpu_percent'],
        dados['memoria_percent'],
        dados['memoria_usada_gb'],
        dados['disco_percent'],
        dados['disco_livre_gb'],
    )
    cursor.execute(comando_sql, valores)
    conn.commit()
    conn.close()
