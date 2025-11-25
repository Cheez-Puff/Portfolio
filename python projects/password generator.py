import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *





class passwordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.enterInput = QLineEdit(self)
        self.generatePassword = QPushButton('Generate Password', self)
        self.enterInputLabel = QLabel('Please Enter Desired Password Length:', self)
        self.charLength = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')
        self.setGeometry(1000, 500, 400, 300)

        vbox = QVBoxLayout()
        vbox.addWidget(self.enterInputLabel)
        vbox.addWidget(self.enterInput)
        vbox.addWidget(self.generatePassword)
        self.setLayout(vbox)
        self.enterInputLabel.setStyleSheet("""font-size: 30px; font-family: sans-serif;""")
        self.enterInput.setStyleSheet("""font-size: 20px; font-family: sans-serif; padding: 5px;""")
        self.generatePassword.setStyleSheet("""font-size: 20px; font-family: sans-serif;""")

        self.generatePassword.clicked.connect(self.generate_password)

    def generate_password(self):
        import random
        import string

        length_text = self.enterInput.text()
        if not length_text.isdigit():
            QMessageBox.warning(self, "Input Error", "Please enter a valid number for password length.")
            return
        
        if int(length_text) <= 5:
            QMessageBox.warning(self, "Too Short!", "Passwords should be at least 6 characters.")
            return
        
        if int(length_text) >= 128:
            QMessageBox.warning(self, "Too Long!", "No one needs a password that long lol.")
            return
        


        length = int(length_text)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        QMessageBox.information(self, "Generated Password", f"Your password is:\n{password}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = passwordGenerator()
    window.show()
    sys.exit(app.exec_())