import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QComboBox, QListWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QMessageBox
)
from models import BankAccount, SavingsAccount


class BankingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI-Bank Application")
        self.setGeometry(100, 100, 300, 400)

        self.owner_input = QLineEdit()
        self.balance_input = QLineEdit()
        self.account_type = QComboBox()
        self.account_type.addItems(["Bank", "Savings"])
        self.interest_input = QLineEdit()
        self.interest_label = QLabel("Interest rate (%):")
        self.interest_input.setPlaceholderText("e.g. 2.5")
        self.interest_input.hide()
        self.interest_label.hide()

        self.account_type.currentTextChanged.connect(self.toggle_interest_input)

        grid = QGridLayout()
        layout = QVBoxLayout()

        grid.addWidget(QLabel("Account Owner:"), 0, 0)
        grid.addWidget(self.owner_input, 0, 1)
        grid.addWidget(QLabel("Starting Balance:"), 1, 0)
        grid.addWidget(self.balance_input, 1, 1)
        grid.addWidget(QLabel("Account Type:"), 2, 0)
        grid.addWidget(self.account_type, 2, 1)
        grid.addWidget(self.interest_label, 3, 0)
        grid.addWidget(self.interest_input, 3, 1)
        layout.addLayout(grid)

        self.create_btn = QPushButton("Create Account")
        self.create_btn.clicked.connect(self.create_account)
        layout.addWidget(self.create_btn)

        self.balance_label = QLabel("Current balance: $0.00")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount:")
        self.deposit_btn = QPushButton("Deposit")
        self.withdraw_btn = QPushButton("Withdraw")
        self.interest_btn = QPushButton("Apply Interest")

        for btn in [self.deposit_btn, self.withdraw_btn, self.interest_btn]:
            btn.setEnabled(False)

        self.deposit_btn.clicked.connect(self.deposit_money)
        self.withdraw_btn.clicked.connect(self.withdraw_money)
        self.interest_btn.clicked.connect(self.apply_interest)

        t_layout = QHBoxLayout()
        t_layout.addWidget(self.amount_input)
        t_layout.addWidget(self.deposit_btn)
        t_layout.addWidget(self.withdraw_btn)
        t_layout.addWidget(self.interest_btn)

        layout.addWidget(self.balance_label)
        layout.addLayout(t_layout)

        layout.addWidget(QLabel("Transaction History:"))
        self.history_list = QListWidget()
        layout.addWidget(self.history_list)
        self.setLayout(layout)

    def toggle_interest_input(self, value):
        is_savings = value == "Savings"
        self.interest_input.setVisible(is_savings)
        self.interest_label.setVisible(is_savings)

    def create_account(self):
        try:
            owner = self.owner_input.text().strip()
            balance = float(self.balance_input.text())
            account_type = self.account_type.currentText()

            if not owner:
                raise ValueError("Account Owner is required")

            if account_type == "Savings":
                if not self.interest_input.text().strip():
                    raise ValueError("Interest rate is required for savings account")
                interest = float(self.interest_input.text())
                self.account = SavingsAccount(owner, balance, interest)
                self.interest_btn.setEnabled(True)
            else:
                self.account = BankAccount(owner, balance)
                self.interest_btn.setEnabled(False)

            self.deposit_btn.setEnabled(True)
            self.withdraw_btn.setEnabled(True)
            self.update_ui()

        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))

    def update_ui(self):
        self.balance_label.setText(f"Current balance: ${self.account.get_balance():.2f}")
        self.history_list.clear()
        for entry in self.account.history:
            self.history_list.addItem(entry)

    def deposit_money(self):
        try:
            amount = float(self.amount_input.text())
            self.account.deposit(amount)
            self.update_ui()
        except ValueError:
            QMessageBox.warning(self, "Error", "Enter a valid number to deposit.")

    def withdraw_money(self):
        try:
            amount = float(self.amount_input.text())
            self.account.withdraw(amount)
            self.update_ui()
        except ValueError as e:
            QMessageBox.warning(self, "Withdraw Error", str(e))

    def apply_interest(self):
        if isinstance(self.account, SavingsAccount):
            self.account.apply_interest()
            self.update_ui()
        else:
            QMessageBox.information(self, "Not Applicable", "Only Savings accounts can apply interest.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BankingApp()
    window.show()
    sys.exit(app.exec_())
