from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtCore import Slot

from . import fetch_object
from .config import CURRENT_DIRECTORY

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chroma Tree")

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)

        button = QPushButton("Process Directory")
        button.clicked.connect(self.process_directory)

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.text_area)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def process_directory(self):
        results = fetch_object(CURRENT_DIRECTORY)
        display = "\n".join(f"{r[0]} -> {r[1]}" for r in results)
        self.text_area.setPlainText(display)


def run():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    run()
