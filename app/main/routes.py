from flask import Blueprint, request, render_template
from app.models import Post
from app.my_budget.forms import BudgetForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def index():
    page = request.args.get('page', default=1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About Page')


@main.route("/my_budget")
def my_budget():
    form = BudgetForm()
    return render_template('my_budget.html', form=form)
