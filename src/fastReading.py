import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMessageBox, QLabel, QFileDialog, QWidget, QHBoxLayout, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fast Reading")
        
        # Obtener la geometría de la pantalla
        screen_geometry = QApplication.desktop().screenGeometry()
        width, height = screen_geometry.width(), screen_geometry.height()

        # Establecer la geometría de la ventana para que ocupe toda la pantalla
        self.setGeometry(0, 0, width, height)

        # ------------------ -Begin Actions- ------------------ #

        # Crear una acción para cerrar la ventana
        close_action = QAction("&Quit", self)
        close_action.setShortcut("Ctrl+Q")
        close_action.setStatusTip("Cerrar la aplicación")
        close_action.triggered.connect(qApp.quit)

        # Crear una acción para mostrar información "About Us"
        about_action = QAction("&About Us", self)
        about_action.setStatusTip("Acerca de nosotros")
        about_action.triggered.connect(self.show_about_message)

         # Crear una acción para abrir una imagen
        open_image_action = QAction("&Open Image", self)
        open_image_action.setStatusTip("Abrir una imagen")
        open_image_action.triggered.connect(self.open_image_dialog)

        # ------------------ -End Actions- ------------------ #

        # ------------------ -Begin Menú- ------------------ #
        # Crear la barra de menú
        menubar = self.menuBar()

        # Crear un menú para "File"
        file_menu = menubar.addMenu("&File")
        # file_menu.addAction(open_image_action)
        file_menu.addAction(close_action)

         # Crear una barra de menú adicional para "About Us"
        help_menu = menubar.addMenu("&Help")
        help_menu.addAction(about_action)

        # ------------------ -End Menú- ------------------ #

        # Crear un widget para mostrar la imagen
        # self.image_label = QLabel()
        # self.image_label.setAlignment(Qt.AlignCenter)
        # self.setCentralWidget(self.image_label)

         # Crear un layout horizontal para dividir la ventana
        layout = QHBoxLayout()
        
        # Crear dos marcos para las partes izquierda y derecha de la ventana
        left_frame = QFrame()
        right_frame = QFrame()
        left_frame.setStyleSheet("background-color: #f0f0f0;")
        right_frame.setStyleSheet("background-color: #ffffff;")

        # Agregar los marcos al layout horizontal
        layout.addWidget(left_frame)
        layout.addWidget(right_frame)

        # Establecer el layout como el layout principal de la ventana
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # ------------------ -Begin Triggered- ------------------ #
    def show_about_message(self):
        # Método para mostrar un cuadro de diálogo con información "About Us"
        about_text = "Esta es una aplicacion dual PDF."
        QMessageBox.information(self, "About Us", about_text)

    def open_image_dialog(self):
        # Abrir un cuadro de diálogo para seleccionar una imagen
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Imágenes (*.png *.jpg *.jpeg)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            # print("selected files: ", selected_files) #path
            if selected_files:
                image_path = selected_files[0]
                self.show_image(image_path)
    # ------------------ -End Triggered- ------------------ #
    


    # ------------------ -Begin Methods- ------------------ #
    def show_image(self, image_path):
        # Mostrar la imagen seleccionada en el centro de la pantalla
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    # ------------------ -End Methods- ------------------ #

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
