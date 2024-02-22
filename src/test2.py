import pyautogui
import time

# Abre Okular (asegúrate de que Okular esté instalado y accesible en tu sistema)
pyautogui.hotkey('ctrl', 'alt', 'o')

# Espera un tiempo para que Okular se abra
time.sleep(2)

# Abre un archivo PDF (reemplaza 'ruta/al/archivo.pdf' con la ruta a tu archivo PDF)
pyautogui.write("/home/russell/Escritorio/CompetitiveProgramming/books/FelixHalim/FelixHalim-Book01.pdf")
pyautogui.press('enter')

# Espera un tiempo para que el archivo se abra
time.sleep(2)

# Puedes realizar más acciones, como hacer clic en ciertos botones utilizando las funciones de pyautogui

# Por ejemplo, para cerrar Okular, puedes hacer clic en el botón de cerrar
pyautogui.click(x=1250, y=25)  # Coordenadas x, y del botón de cerrar en mi pantalla

# Puedes ajustar las coordenadas de acuerdo con tu resolución de pantalla y la posición de los elementos en Okular en tu sistema.
