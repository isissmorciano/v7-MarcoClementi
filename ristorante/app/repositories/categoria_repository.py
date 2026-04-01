from app.db import get_db


# TODO: Implementa le funzioni richieste dall'esercizio 1 e 2
def get_all_categories():
    db = get_db()
    categories = db.execute(
        "SELECT id, nome FROM categorie ORDER BY nome"
    ).fetchall()
    return categories



def create_category(nome):
    db = get_db()
    db.execute(
        "INSERT INTO categorie (nome) VALUES(?,?,?)",
        (nome,)
    )
    db.commit()



def get_category_by_id(category_id):
    db = get_db()
    category = db.execute(
        "SELECT id, nome FROM categorie WHERE id = ?",
        (category_id,)
    ).fetchone()
    return category

