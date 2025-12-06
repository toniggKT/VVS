from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
#from PySide6 import QtCore, QtWidgets, QtGui

#Вводить image1.jpg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initImage()

    def initImage(self):
        self.setWindowTitle('Просмотр изображений')
        self.setGeometry(100, 100, 800, 600)

        # Центральный виджет и layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        #Поле для ввода пути
        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText('Введите путь к изображению:')
        layout.addWidget(self.path_input)

        #Кнопка выбора файла
        self.select_btn = QPushButton('Выбрать файл')
        self.select_btn.clicked.connect(self.select_file)
        layout.addWidget(self.select_btn)

        #Кнопка вывода изображения
        self.show_btn = QPushButton('Вывести изображение')
        self.show_btn.clicked.connect(self.show_image)
        layout.addWidget(self.show_btn)

        #Метка для изображения
        self.image_label = QLabel('Изображение')
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setMinimumHeight(400)

        layout.addWidget(self.image_label)

    def select_file(self):
        """Открывает диалог выбора файла"""
        file_path, _ = QFileDialog.getOpenFileName(self,'Выберите изображение','','Изображения (*.png *.jpg *.jpeg *.bmp *.gif *.tiff)')
        if file_path:
            self.path_input.setText(file_path)

    def show_image(self):
        """Выводит изображение по указанному пути"""
        path = self.path_input.text().strip()
        if not path:
            self.image_label.setText('Введите путь к изображению!')
            return

        pixmap = QPixmap(path)
        if pixmap.isNull():
            self.image_label.setText('Ошибка!')
            return

        # Масштабирование изображения
        scaled_pixmap = pixmap.scaled(
            self.image_label.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)



if __name__ == '__main__':
    app = QApplication([])
    #настройка стиля:
    app.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:, y1:0, x2:1, y2:1,
                    stop:0 #667eea, stop:1 #764ba2);
            }
            
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: white;
            }
        """)

    mainapp = MainWindow()
    mainapp.show()
    app.exec()

