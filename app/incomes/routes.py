from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.incomes.forms import IncomesForm
from app.models import Incomes
from app import db

expenses = Blueprint('expenses', __name__)


@expenses.route('/expenses/new')
@login_required
def new_incomes():
    form = IncomesForm()
    if form.validate_on_submit():
        income = Incomes(title=form.title.data, value=form.value.data, user=current_user)
        db.session.add(income)
        db.session.commit()
        flash('Доход добавлен', 'success')
        return redirect(url_for('main.index'))
    return render_template('new_incomes.html', title='Новые доходы',
                           form=form, legend='Новые доходы')


@expenses.route('/expenses/<int:income_id>/delete')
def delete_incomes(income_id):
    income = Incomes.query.get_or_404(income_id)
    db.session.delete(income)
    db.session.commit()
    flash('Доход удален')
    return redirect(url_for('main.index'))



