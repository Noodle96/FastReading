# main.py
import sys
from PyQt5.QtWidgets import QApplication
from ui.mainwindow import MainWindow  # Importar la clase MainWindow desde el módulo mainwindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
