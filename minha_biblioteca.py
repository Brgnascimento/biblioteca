import sqlite3
import pandas as pd
from pathlib import Path


ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / 'biblioteca.sqlite')

cursor = conn.cursor()

cursor.row_factory = sqlite3.Row


livros = pd.read_excel('livros.xlsx')
livros = livros.astype(str)
livros = list(livros.to_records(index=False))


cursor.execute('''
               
               CREATE TABLE IF NOT EXISTS livros (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   ano TEXT NOT NULL,
                   isbn TEXT UNIQUE
                   
                ); ''')





def adicionar(conn, cursor, dados):
    cursor.executemany(
        ''' INSERT INTO livros (titulo, autor, ano, isbn) 
            VALUES (?,?,?,?)''',
            dados,
            )
    conn.commit()
    

def excluir_registro(conn, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM livros WHERE id = ?; ", data)
    conn.commit()
    

adicionar(conn, cursor, livros)


# cursor.execute('DROP TABLE livros') 
