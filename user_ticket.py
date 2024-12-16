import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class UserTicketForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crear Ticket")

        # Crear widgets
        self.name_label = QLabel("Nombre:")
        self.name_input = QLineEdit()

        self.grade_label = QLabel("Grado:")
        self.grade_input = QLineEdit()

        self.email_label = QLabel("Correo Electrónico:")
        self.email_input = QLineEdit()

        self.description_label = QLabel("Descripción del Problema:")
        self.description_input = QTextEdit()

        self.submit_button = QPushButton("Enviar Ticket")
        self.submit_button.clicked.connect(self.send_ticket)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.grade_label)
        layout.addWidget(self.grade_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_input)
        layout.addWidget(self.submit_button)

        # Contenedor central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def send_ticket(self):
        name = self.name_input.text()
        grade = self.grade_input.text()
        email = self.email_input.text()
        description = self.description_input.toPlainText()

        if name and grade and email and description:
            try:
                # Enviar un correo de confirmación
                self.send_email(name, grade, email, description)
                QMessageBox.information(self, "Éxito", "¡Ticket enviado correctamente!")

                # Limpiar los campos
                self.name_input.clear()
                self.grade_input.clear()
                self.email_input.clear()
                self.description_input.clear()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo enviar el ticket.\n\n{str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

    def send_email(self, name, grade, email, description):
        sender_email = "techcare.app2024@gmail.com"
        sender_password = "dvexnxbfquajnxtc"
        recipient_email = "techcare.app2024@gmail.com"

        subject = f"Nuevo Ticket de {name}"
        body = f"""
        Nombre: {name}
        Grado: {grade}
        Correo Electrónico: {email}
        Descripción del Problema: {description}
        """

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        # Enviar el correo usando SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserTicketForm()
    window.show()
    sys.exit(app.exec_())
