# actions.py

from PyQt5.QtWidgets import QAction, QMessageBox, qApp, QFileDialog
from PyQt5.QtCore import Qt

def quit_action_triggered():
    qApp.quit()

def about_action_triggered(parent):
    about_text = "Esta es una aplicación dual PDF."
    QMessageBox.information(parent, "About Us", about_text)

def open_pdf_action_triggered(parent):
    file_dialog = QFileDialog(parent)
    file_dialog.setNameFilter("Archivos PDF (*.pdf)")
    file_dialog.setViewMode(QFileDialog.Detail)
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    if file_dialog.exec_():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            pdf_path = selected_files[0]
            # Llamar a la función show_pdf de la ventana principal
            parent.render_pdf(pdf_path)

def open_image_action_triggered(parent):
    file_dialog = QFileDialog(parent)
    file_dialog.setNameFilter("Imágenes (*.png *.jpg *.jpeg)")
    file_dialog.setViewMode(QFileDialog.Detail)
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    if file_dialog.exec_():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            image_path = selected_files[0]
            # Llamar a la función show_image de la ventana principal
            parent.show_image(image_path)