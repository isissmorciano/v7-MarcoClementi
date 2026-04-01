from app.db import get_db

# TODO: 
def get_all_piatti():
    db = get_db()
    piatti = db.execute("""
        SELECT p.id, p.categoria_id,  p.nome, p.prezzo,  c.nome  
        FROM piatti p 
        JOIN categorie c ON p.categoria_id = c.id 
        ORDER BY p.nome
    """).fetchall()
    return piatti


def get_piatti_by_category(category_id):
    db = get_db()
    piatti = db.execute("""
        SELECT p.id, p.categoria_id, p.nome, p.prezzo, c.nome 
        FROM piatti p 
        JOIN categorie c ON p.categoria_id = c.id 
        WHERE p.categoria_id = ? 
        ORDER BY p.nome,
        (category_id,)
    """).fetchall() #perchè ci aspettiamo più risultati
    return piatti 


def create_piatto(category_id, nome, prezzo):
    "Crea nuovo piatto"
    db = get_db()
    db.execute(
        'INSERT INTO piatti (categoria_id, nome, prezzo) VALUES (?, ?, ?)',
        (category_id, nome, prezzo)
    )
    db.commit()



def get_piatto_by_id(piatto_id): 
    db = get_db()
    piatto = db.execute("""
        SELECT p.id, p.categoria_id, p.nome, p.prezzo, c.nome as categoria_nome 
        FROM piatti p 
        JOIN categorie c ON p.categoria_id = c.id 
        WHERE p.id = ?,
        (piatto_id,)
    """).fetchone()
    return piatto




