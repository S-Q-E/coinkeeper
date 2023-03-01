from flask import Blueprint, flash, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.models import Transaction
from app import db
from .forms import BudgetForm

budget = Blueprint('budget', __name__)


@budget.route("/my_budget", methods=['GET', 'POST'])
@login_required
def my_budget():
    transactions = Transaction.query.all()
    form = BudgetForm()
    return render_template('my_budget.html', form=form, transactions=transactions)


@budget.route('/add-transaction', methods=['POST'])
def add_transaction():
    transaction_type = request.form['transaction_type']
    title = request.form['title']
    value = request.form['value']
    if transaction_type == 'expenses':
        expense = Expenses(type=transaction_type, title=title, value=value, user=current_user)
        db.session.add(expense)
        db.session.commit()
        flash('Расход добавлен', 'success')
    elif transaction_type == 'incomes':
        income = Incomes(type=transaction_type,title=title, value=value, user=current_user)
        db.session.add(income)
        db.session.commit()
        flash('Доход добавлен', 'success')
    return redirect(url_for('budget.my_budget'))



@budget.route('/my_budget/expenses/<int:expense_id>/delete')
def delete_expenses(expense_id):
    expense = Expenses.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    flash('Расход удален')
    return redirect(url_for('main.index'))


@budget.route('/my_budget/expenses/<int:income_id>/delete')
def delete_incomes(income_id):
    income = Incomes.query.get_or_404(income_id)
    db.session.delete(income)
    db.session.commit()
    flash('Доход удален')
    return redirect(url_for('budget.my_budget'))
