import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QCheckBox

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generatore di Password")
        self.setGeometry(100, 100, 400, 250)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Campo password
        self.password_field = QLineEdit()
        self.password_field.setReadOnly(True)
        layout.addWidget(self.password_field)

        # Lunghezza password
        length_layout = QHBoxLayout()
        length_layout.addWidget(QLabel("Lunghezza:"))
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setRange(8, 32)
        self.length_spinbox.setValue(12)
        length_layout.addWidget(self.length_spinbox)
        layout.addLayout(length_layout)

        # Opzioni caratteri
        self.uppercase_cb = QCheckBox("Maiuscole")
        self.uppercase_cb.setChecked(True)
        layout.addWidget(self.uppercase_cb)

        self.lowercase_cb = QCheckBox("Minuscole")
        self.lowercase_cb.setChecked(True)
        layout.addWidget(self.lowercase_cb)

        self.digits_cb = QCheckBox("Numeri")
        self.digits_cb.setChecked(True)
        layout.addWidget(self.digits_cb)

        self.symbols_cb = QCheckBox("Simboli")
        self.symbols_cb.setChecked(True)
        layout.addWidget(self.symbols_cb)

        # Pulsante genera
        generate_button = QPushButton("Genera Password")
        generate_button.clicked.connect(self.generate_password)
        layout.addWidget(generate_button)

    def generate_password(self):
        length = self.length_spinbox.value()
        char_sets = []

        if self.uppercase_cb.isChecked():
            char_sets.append(string.ascii_uppercase)
        if self.lowercase_cb.isChecked():
            char_sets.append(string.ascii_lowercase)
        if self.digits_cb.isChecked():
            char_sets.append(string.digits)
        if self.symbols_cb.isChecked():
            char_sets.append(string.punctuation)

        if not char_sets:
            self.password_field.setText("Seleziona almeno un tipo di carattere")
            return

        all_chars = ''.join(char_sets)
        password = ''.join(random.choice(all_chars) for _ in range(length))
        self.password_field.setText(password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
