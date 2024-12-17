import sys
import json
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

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
        name = self.name_input.text()
        grade = self.grade_input.text()
        email = self.email_input.text()
        description = self.description_input.toPlainText()

        if not all([name, grade, email, description]):
            QMessageBox.warning(self, "Error", "Por favor, completa todos los campos.")
            return

        data = {
            'name': name,
            'grade': grade,
            'email': email,
            'description': description
        }

        try:
            response = requests.post(
                'http://127.0.0.1:8000/helpdesk/submit_ticket/',
                data=json.dumps(data),
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code == 201:
                QMessageBox.information(self, "Éxito", "Ticket enviado correctamente.")
                # Limpiar el formulario automáticamente
                self.name_input.clear()
                self.grade_input.clear()
                self.email_input.clear()
                self.description_input.clear()
            else:
                error_message = response.json().get('error', 'Error desconocido.')
                QMessageBox.warning(self, "Error", f"Error al enviar el ticket: {error_message}")

        except requests.ConnectionError:
            QMessageBox.critical(self, "Error", "No se pudo conectar al servidor. Asegúrate de que el servidor esté en ejecución.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ha ocurrido un error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicketForm()
    window.show()
    sys.exit(app.exec_())
