import sqlite3

def save_data():
    conn = sqlite3.connect('UsuarioData.db')
    cursor = conn.cursor()

    cursor.execute("""  
            """)