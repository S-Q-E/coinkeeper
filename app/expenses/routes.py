from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.expenses.forms import ExpensesForm
from app.models import Expenses
from app import db

expenses = Blueprint('expenses', __name__)


@expenses.route('/expenses/new')
@login_required
def new_expenses():
    form = ExpensesForm()
    if form.validate_on_submit():
        expense = Expenses(title=form.title.data, value=form.value.data, user=current_user)
        db.session.add(expense)
        db.session.commit()
        flash('Расход добавлен', 'success')
        return redirect(url_for('main.index'))
    return render_template('new_expenses.html', title='Новые расходы',
                           form=form, legend='Новые расходы')


@expenses.route('/expenses/<int:expense_id>/delete')
def delete_expenses(expense_id):
    expense = Expenses.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    flash('Расход удален')
    return redirect(url_for('main.index'))



