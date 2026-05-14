from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import login_required,current_user
from models import db
from models.transaction import Transaction
from utils.predictor import predict_category
from ml.anomly_detector import detect_anomaly

transactions = Blueprint('transactions',__name__)

@transactions.route('/transactions')
@login_required
def view_transactions():
    user_transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    return render_template('transactions.html', transactions=user_transactions)


@transactions.route('/add_transaction',methods=['GET','POST'])
@login_required
def add_transaction():

    is_anomaly = False

    if request.method == 'POST':
        try:
            amount = float(request.form.get('amount', 0))
        except ValueError:
            amount = 0.0

        description = request.form.get('description')
        category = predict_category(description)

        previous_transactions = Transaction.query.filter_by(user_id=current_user.id).all()
        amounts = [t.amount for t in previous_transactions]

        is_anomaly = detect_anomaly(amounts, amount)

        new_transaction = Transaction(
            amount=amount,
            description=description,
            category=category,
            user_id=current_user.id
        )

        db.session.add(new_transaction)
        db.session.commit()

        return redirect(url_for('transactions.view_transactions'))
    return render_template(
            'add_transaction.html',
            anomly=is_anomaly
    )

@transactions.route('/delete/<int:id>')
@login_required
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)

    if transaction.user_id != current_user.id:
        return redirect(url_for('transactions.view_transactions'))
    
    db.session.delete(transaction)
    db.session.commit()

    return redirect(url_for('transactions.view_transactions'))