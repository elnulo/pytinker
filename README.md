# Messing about with stuff

## Main.py 
This is the first attempt with tkinter and webview
However, it won't work because the webview implementation just must have its own window

## second.py
Found a CEF (chromium) bit that *looked* like it would work. Failed miserably because the guy who maintains it seems to have stopped and doesn't support anything beyond Python 3.7.... which is pretty much deprecated so FML.

## withqt.py (aka Switch to QT with PyQt)
This actually worked quite well. Had to switch to a diffrent UI toolkit (QT via PyQT) but that's been around forever and seems to still be well maintained. Webviews came in and all.


Some installs and pip3 installs were required but not that many.
Pip3 ones:
- pyqt6
- PyQt6-WebEngine


