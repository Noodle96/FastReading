# mainwindow.py

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMessageBox, QLabel, QFileDialog, QWidget, QHBoxLayout, QVBoxLayout, QFrame, QScrollArea, QSizePolicy, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
import fitz
import PyPDF2
from .actions import quit_action_triggered, about_action_triggered, open_pdf_action_triggered, open_image_action_triggered
from pdf2image import convert_from_path


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
        # Crear una acción para abrir un archivo PDF
        open_pdf_action = QAction("&Open PDF", self)
        open_pdf_action.setShortcut("Ctrl+O")
        open_pdf_action.setStatusTip("Abrir un archivo PDF")
        open_pdf_action.triggered.connect(lambda: open_pdf_action_triggered(self))

        # Crear una acción para cerrar la ventana
        close_action = QAction("&Quit", self)
        close_action.setShortcut("Ctrl+Q")
        close_action.setStatusTip("Cerrar la aplicación")
        close_action.triggered.connect(quit_action_triggered)

        # Crear una acción para mostrar información "About Us"
        about_action = QAction("&About Us", self)
        about_action.setStatusTip("Acerca de nosotros")
        about_action.triggered.connect(lambda: about_action_triggered(self))

        open_image_action = QAction("&Open Image", self)
        open_image_action.setStatusTip("Abrir una imagen")
        open_image_action.triggered.connect(lambda: open_image_action_triggered(self))

        # ------------------ -End Actions- ------------------ #


        # ------------------ -Begin Menú- ------------------ #
        # Crear la barra de menú
        menubar = self.menuBar()

        # Crear un menú para "File"
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(open_pdf_action)
        file_menu.addAction(open_image_action)
        file_menu.addAction(close_action)

         # Crear una barra de menú adicional para "About Us"
        help_menu = menubar.addMenu("&Help")
        help_menu.addAction(about_action)

        # ------------------ -End Menú- ------------------ #

        # ------------------ -Begin Widgets- ------------------ #

        # Widget principal que contiene los dos frames
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Layout principal para el widget principal
        main_layout = QHBoxLayout(main_widget)

        #izquierda
        # Frame izquierdo para el PDF y el scrollbar
        left_frame = QFrame()
        left_layout = QVBoxLayout(left_frame)

        # Crear el área de desplazamiento para el PDF
        pdf_scroll_area = QScrollArea()
        pdf_scroll_area.setWidgetResizable(True)  # Para que el contenido sea redimensionable
        pdf_widget = QWidget()
        self.pdf_layout = QVBoxLayout(pdf_widget)
        # Agregar elementos de visualización del PDF al pdf_layout
        # Agregar elementos de visualización del PDF al pdf_layout
        # for i in range(50):
        #     label = QLabel(f"Contenido {i}")
        #     pdf_layout.addWidget(label)

        pdf_scroll_area.setWidget(pdf_widget)

        left_layout.addWidget(pdf_scroll_area)
        left_frame.setLayout(left_layout)

        # DERECHO
        # Frame derecho para otros elementos de la interfaz de usuario
        # Marco derecho para mostrar el texto de la página actual
        right_frame = QFrame()
        right_layout = QVBoxLayout(right_frame)
        self.text_edit = QTextEdit()  # Widget de texto para mostrar el texto de la página actual
        right_layout.addWidget(self.text_edit)
        right_frame.setLayout(right_layout)


        # Agregar los frames al layout principal
        main_layout.addWidget(left_frame, stretch=1)
        main_layout.addWidget(right_frame, stretch=1)
        # ------------------ -End Widgets- ------------------ #

    def add_content_to_left_frame(self):
        # Añade contenido al lado izquierdo
        label = QLabel("Left Frame Content")
        self.left_frame_layout.addWidget(label)

    def add_content_to_right_frame(self):
        # Añade contenido al lado derecho usando QScrollArea
        for i in range(10):
            label = QLabel(f"Scroll Content {i}")
            self.scroll_layout.addWidget(label)

    def show_image(self, image_path):
        # Cargar la imagen seleccionada en el lado derecho de la ventana
        pixmap = QPixmap(image_path)
        # Escalar la imagen para que quepa en el QLabel
        scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # Mostrar la imagen en el lado derecho de la ventana
        self.image_label.setPixmap(scaled_pixmap)

    # ------------------ -Begin Methods- ------------------ #
    # def render_pdf(self, pdf_path):
    #     # Convertir el PDF a imágenes
    #     images = convert_from_path(pdf_path)

    #     # Limpiar el área de desplazamiento antes de agregar nuevas imágenes
    #     for i in reversed(range(self.pdf_layout.count())):
    #         widgetToRemove = self.pdf_layout.itemAt(i).widget()
    #         if widgetToRemove is not None:
    #             widgetToRemove.setParent(None)

    #     # Agregar cada página del PDF al área de desplazamiento
    #     # print("images.size(): ", len(images))
    #     for image in images:
            
    #         label = QLabel()
    #         # qr = "elias"
    #         # print("qr: ",type(qr))
    #         # print("image: ",type(image))
    #         image_data = image.tobytes()  # Convierte la imagen a bytes

    #         # Luego, crea un objeto QImage a partir de los datos de la imagen
    #         qimage = QImage(image_data, image.width, image.height, QImage.Format_RGB888)
    #         pixmap = QPixmap.fromImage(qimage)
    #         label.setPixmap(pixmap)
    #         self.pdf_layout.addWidget(label)
    def render_pdf(self, pdf_path):
        # Limpiar el área de desplazamiento antes de agregar nuevas páginas del PDF
        for i in reversed(range(self.pdf_layout.count())):
            widgetToRemove = self.pdf_layout.itemAt(i).widget()
            if widgetToRemove is not None:
                widgetToRemove.setParent(None)

        # Crear un visor de PDF utilizando la biblioteca fitz
        doc = fitz.open(pdf_path)
        list_images = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pixmap = page.get_pixmap()
            label = QLabel()
            label.setPixmap(QPixmap.fromImage(QImage(pixmap.samples, pixmap.width, pixmap.height, pixmap.stride, QImage.Format_RGB888)))
            # label.setScaledContents(True)  # Escalar contenido para que ocupe todo el espacio disponible
            self.pdf_layout.addWidget(label)

            # Recuperar el texto de la página actual
            text = page.get_text()
            self.text_edit.setPlainText(text)  # Mostrar el texto en el widget de texto
            list_images.append((page_num,label))

        # self.text_edit.textChanged.connect(self.handle_text_changed)  # Volver a conectar la señal de cambio de texto
        doc.close()




        # Establecer el layout de las imágenes dentro del área de desplazamiento
        # self.scroll.setLayout(self.pdf_layout)

        # # Agregar el área de desplazamiento al frame izquierdo
        # layout = QVBoxLayout(self.left_frame)
        # layout.addWidget(self.scroll)
        # self.left_frame.setLayout(layout)
    
    def add_content_to_right_frame(self):
        # Añade contenido al lado derecho usando QScrollArea
        for i in range(100):
            label = QLabel(f"monos de africa monos de africa monos de africa monos de africa monos de africa monos de africa monos de africaScroll Content {i}")
            self.scroll_layout.addWidget(label)

    # ------------------ -End Methods- ------------------ #
