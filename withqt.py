from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QSize, QUrl

# Only needed for access to command line arguments
import sys



# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.

layout = QGridLayout()
mainWidget = QWidget()
mainWidget.setLayout(layout)

window = QMainWindow()
window.setWindowTitle("I amd doing this thang")
window.setCentralWidget(mainWidget)


layout.addWidget(QPushButton("TopLeft"), 0, 0)
layout.addWidget(QPushButton("Topright"), 0, 1)
layout.addWidget(QPushButton("ButtonLeft"), 1, 0)

rightButton = QPushButton("ButtonRight")
rightButton.setStyleSheet("background-color: red")

webEngine = QWebEngineView()
layout.addWidget(webEngine, 2, 0, 1, 2)
webEngine.load(QUrl("https://www.google.com"))

def buttonWasClicked():
    print("button was clicked")


rightButton.clicked.connect(buttonWasClicked)
layout.addWidget(rightButton, 1, 1)


window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()