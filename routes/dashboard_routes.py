from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.transaction import Transaction
from collections import defaultdict
from ml.expense_predictor import predict_next_month
from models.budget import Budget
from datetime import datetime

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def dashboard_view():

    transactions = Transaction.query.filter_by(user_id=current_user.id).all()

    total_expense = sum(t.amount for t in transactions)

    total_transactions = len(transactions)

    # CATEGORY DATA
    category_data = defaultdict(float)

    for t in transactions:
        category_data[t.category] += t.amount

    categories = list(category_data.keys())
    amounts = list(category_data.values())

    # MONTHLY DATA
    monthly_data = defaultdict(float)

    for t in transactions:
        month = t.date.strftime('%Y-%m')
        monthly_data[month] += t.amount

    months = list(monthly_data.keys())
    monthly_amounts = list(monthly_data.values())

    prediction = predict_next_month(monthly_amounts)

    current_month = datetime.now().strftime('%Y-%m')

    budget = Budget.query.filter_by(
        user_id = current_user.id,
        month = current_month
    ).first()

    budget_amount = budget.amount if budget else 0

    alert = None

    if budget and total_expense > budget_amount:
        alert = '⚠️ You exceeded your monthly budget!'

    food_spending = category_data.get('Food',0)

    suggestion = None

    if food_spending > 0:
        suggestion = 'Reduce Food expenses by 15% to stay within budget.'

    return render_template(
        "dashboard.html",
        total_expense=total_expense,
        total_transactions=total_transactions,
        categories=categories,
        amounts=amounts,
        months=months,
        monthly_amounts=monthly_amounts,
        prediction=prediction,
        budget = budget_amount,
        alert = alert,
        suggestion = suggestion
    )