import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton

class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de Usuario")
        self.setGeometry(100, 100, 400, 200)

        # Diseño de la ventana
        layout = QVBoxLayout()

        self.label = QLabel("¡Bienvenido al sistema de tickets!")
        layout.addWidget(self.label)

        self.button = QPushButton("Enviar Ticket")
        self.button.clicked.connect(self.send_ticket)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def send_ticket(self):
        self.label.setText("Ticket enviado con éxito.")

def main():
    app = QApplication(sys.argv)
    window = UserWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
