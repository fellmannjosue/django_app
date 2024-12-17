from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import sys

class TicketForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crear Ticket")
        self.setWindowIcon(QIcon("static/img/ana-transformed.png"))
        self.setFixedSize(400, 500)

        # Logo
        logo = QLabel(self)
        pixmap = QPixmap("static/img/ana-transformed.png")
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)

        # Campos del formulario
        self.name_label = QLabel("Nombre:")
        self.name_input = QLineEdit()

        self.grade_label = QLabel("Grado:")
        self.grade_input = QLineEdit()

        self.email_label = QLabel("Correo Electrónico:")
        self.email_input = QLineEdit()

        self.description_label = QLabel("Descripción del Problema:")
        self.description_input = QTextEdit()

        # Botón para enviar el formulario
        self.submit_button = QPushButton("Enviar Ticket")
        self.submit_button.clicked.connect(self.submit_ticket)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(logo)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.grade_label)
        layout.addWidget(self.grade_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_ticket(self):
        # Aquí se enviaría el ticket a la base de datos o servidor
        print("Ticket enviado")
        print(f"Nombre: {self.name_input.text()}")
        print(f"Grado: {self.grade_input.text()}")
        print(f"Correo Electrónico: {self.email_input.text()}")
        print(f"Descripción: {self.description_input.toPlainText()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicketForm()
    window.show()
    sys.exit(app.exec_())
