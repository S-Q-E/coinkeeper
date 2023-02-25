from flask import Blueprint, request, render_template
from app.models import Expenses, Incomes, Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def index():
    page = request.args.get('page', default=1, type=int)
    expenses = Expenses.query.order_by(Expenses.date_posted.desc()).paginate(page=page, per_page=5)
    incomes = Incomes.query.order_by(Incomes.date_posted.desc()).paginate(page=page, per_page=5)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', incomes=incomes, expenses=expenses, posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About Page')