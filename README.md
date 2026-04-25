# Personal Finance Tracker

A comprehensive personal finance management web application built with Flask. This project helps users track their income, expenses, and budgets while leveraging machine learning to provide intelligent insights, expense predictions, and anomaly detection.

## Features

- **User Authentication:** Secure signup and login system using Flask-Login and bcrypt.
- **Dashboard:** An interactive dashboard providing a summary of your finances, including charts and visualizations.
- **Transaction Management:** Easily add, edit, view, and categorize your income and expenses.
- **Budgeting:** Set and manage budgets to keep your spending in check.
- **AI-Powered Insights:** 
  - **Expense Prediction:** Uses machine learning to forecast future spending patterns.
  - **Anomaly Detection:** Automatically identifies unusual spending behavior to alert the user.

## Tech Stack

### Backend
- **Python 3**
- **Flask:** Core web framework.
- **Flask-SQLAlchemy:** ORM for database interactions.
- **Flask-Login:** User session management.
- **Flask-Bcrypt:** Password hashing.
- **SQLite:** Lightweight relational database.

### Machine Learning & Data Processing
- **Pandas & NumPy:** Data manipulation and analysis.
- **Scikit-learn:** Building predictive models and anomaly detection.
- **Matplotlib:** Generating static charts and visualizations.

### Frontend
- **HTML/CSS/JS**
- **Jinja2:** Flask's templating engine for dynamic HTML rendering.

## Project Structure

```
personal_finance_tracker/
│
├── app.py                   # Main application entry point & factory
├── config.py                # Application configuration settings
├── requirement.txt          # Python dependencies
│
├── instance/                # Contains the SQLite database (finance.db)
│
├── models/                  # Database models
│   ├── user.py              # User account model
│   ├── transaction.py       # Financial transaction model
│   └── budget.py            # Budgeting model
│
├── routes/                  # Flask Blueprints for routing
│   ├── auth_routes.py       # Authentication routes (login, register)
│   ├── dashboard_routes.py  # Dashboard and visualization routes
│   ├── transaction_routes.py# Transaction CRUD operations
│   ├── budget_routes.py     # Budget management routes
│   └── insight_routes.py    # AI insights and prediction routes
│
├── ml/                      # Machine Learning module
│   ├── anomly_detector.py   # Script for detecting spending anomalies
│   ├── expense_predictor.py # Script for predicting future expenses
│   ├── train_model.py       # Script to train and save ML models
│   └── *.pkl / *.csv        # Serialized models and datasets
│
├── templates/               # HTML templates (Jinja2)
├── static/                  # Static files (CSS, JavaScript, Images)
└── utils/                   # Helper and utility functions
```

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd personal_finance_tracker
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

4. **Initialize the Database:**
   The database tables will be created automatically when you run the application for the first time thanks to `db.create_all()` in `app.py`.

5. **Run the application:**
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000/`.

## Machine Learning Models
To retrain the machine learning models (expense predictor and anomaly detector) with new data, you can run the training script located in the `ml/` directory:
```bash
python ml/train_model.py
```
This will generate new `.pkl` files used by the application for providing insights.
