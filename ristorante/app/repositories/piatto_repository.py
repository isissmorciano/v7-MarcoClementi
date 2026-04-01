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
    db = get.db()
    db.execute("""
        SELECT p.id, p.categoria.id, p.nome, p.prezzo, c.nome 
        FROM piatti p
        JOIN user u ON p.author_id = u.id
        WHERE p.id = ?
    """)
    # fetchone() perché ci aspettiamo un solo risultato
    post = db.execute(query, (post_id,)).fetchone()
    if post:
        post_dict = dict(post)
        post_dict['created'] = datetime.fromisoformat(post_dict['created'])
        return post_dict
    return post





