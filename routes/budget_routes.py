from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db
from models.budget import Budget
from datetime import datetime

budget = Blueprint('budget',__name__)

@budget.route('/set_budget', methods=['GET','POST'])
@login_required
def set_budget():

    if request.method == 'POST':
        try:
            amount = float(request.form.get('amount', 0))
        except ValueError:
            amount = 0.0
        month = datetime.now().strftime('%Y-%m')

        existing = Budget.query.filter_by(
            user_id = current_user.id,
            month = month
        ).first()

        if existing:
            existing.amount = amount
        else:
            new_budget = Budget(
                amount = amount,
                month = month,
                user_id = current_user.id
            )
            db.session.add(new_budget)
        
        db.session.commit()

        return redirect(url_for('dashboard.dashboard_view'))
    
    return render_template('set_budget.html')