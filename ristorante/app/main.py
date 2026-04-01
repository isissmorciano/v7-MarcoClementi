from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import categoria_repository, piatto_repository

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    categories = categoria_repository.get_all_categories()
    return render_template("index.html", categories=categories)


@bp.route("/categoria/:categoria_id")
def categoria_detail(categoria_id):
    category = categoria_repository.get_category_by_id(categoria_id)
    if category is None:
        abort(404)
    piatti = piatto_repository.get_piatti_by_category(categoria_id)
    return render_template("categoria_detail.html", category=category, piatti=piatti)



@bp.route("/crea_categoria", methods=["GET", "POST"])
def crea_categoria():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        if not nome:
            flash("Nome categoria obbligatorio")
        else:
            categoria_repository.create_category(nome)
            flash(f"Categoria '{nome}' creata con successo")
            return redirect(url_for("main.index"))
    
    return render_template("crea_categoria.html")

@bp.route("/crea_piatto", methods=["GET", "POST"])
def crea_piatto():
    categories = categoria_repository.get_all_categories()
    if request.method == "POST":
        return None



    

