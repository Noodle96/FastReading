# import fitz  # PyMuPDF
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
# import sys

# class PDFViewer(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PDF Viewer")
#         self.setGeometry(100, 100, 800, 600)

#         self.central_widget = QWidget()
#         self.setCentralWidget(self.central_widget)

#         self.layout = QVBoxLayout(self.central_widget)

#         self.text_edit = QTextEdit()
#         self.text_edit.setReadOnly(True)

#         self.load_pdf("/home/russell/Escritorio/CompetitiveProgramming/books/FelixHalim/FelixHalim-Book01.pdf")
#         self.render_pdf()

#         self.layout.addWidget(self.text_edit)

#     def load_pdf(self, filename):
#         self.doc = fitz.open(filename)

#     def render_pdf(self):
#         text = ""
#         for page_num in range(self.doc.page_count):
#             page = self.doc.load_page(page_num)
#             text += page.get_text()

#         self.text_edit.setPlainText(text)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     viewer = PDFViewer()
#     viewer.show()
#     sys.exit(app.exec_())


import fitz  # PyMuPDF
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QTextCursor
import sys
from PyQt5.QtCore import Qt


class PDFViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        # self.load_pdf("example.pdf")
        self.load_pdf("/home/russell/Escritorio/CompetitiveProgramming/books/FelixHalim/FelixHalim-Book01.pdf")
        self.render_pdf()

        self.layout.addWidget(self.text_edit)

    def load_pdf(self, filename):
        self.doc = fitz.open(filename)

    def render_pdf(self):
        for page_num in range(self.doc.page_count):
            page = self.doc.load_page(page_num)
            text = page.get_text()
            self.text_edit.moveCursor(QTextCursor.End)
            self.text_edit.insertPlainText(f"Page {page_num + 1}:\n{text}\n\n")

            # Aplicar formato al texto de la página (ejemplo: cambiar color y tamaño de fuente)
            cursor = self.text_edit.textCursor()
            cursor.select(QTextCursor.LineUnderCursor)
            format = cursor.charFormat()
            format.setForeground(Qt.red)  # Cambiar color de texto a rojo
            format.setFontPointSize(12)   # Cambiar tamaño de fuente a 12
            cursor.setCharFormat(format)
            self.text_edit.setTextCursor(cursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = PDFViewer()
    viewer.show()
    sys.exit(app.exec_())

