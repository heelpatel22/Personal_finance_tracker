from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.transaction import Transaction
from collections import defaultdict

insight = Blueprint('insight',__name__)

@insight.route('/insights')
@login_required
def insights():

    transactions = Transaction.query.filter_by(user_id=current_user.id).all()

    category_data = defaultdict(float)
    monthly_data = defaultdict(float)

    for t in transactions:
        category_data[t.category] += t.amount
        monthly_data[t.date.strftime('%Y-%m')] += t.amount

    if category_data:
        top_category = max(category_data, key=category_data.get)
    else:
        top_category = None

    insights = []

    if top_category:
        insights.append(f'Your highest spending category is {top_category}')

    sorted_months = sorted(monthly_data.keys())
    if len(sorted_months) >= 2:
        current_month = sorted_months[-1]
        previous_month = sorted_months[-2]
        if monthly_data[current_month] > monthly_data[previous_month]:
            insights.append('You spent more this month than last month.')
        elif monthly_data[current_month] < monthly_data[previous_month]:
            insights.append('Great job! You spent less this month than last month.')

    return render_template(
        'insights.html',
        insights = insights
    )