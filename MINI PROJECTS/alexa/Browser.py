import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # back button
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # forward button
        forward_btn = QAction("forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # reload button
        reload_btn = QAction("reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # home button
        home_btn = QAction("home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # search box
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # update the url
        self.browser.urlChanged.connect(self.update_url)

        # just for me
        self.cross = QMenuBar()
        navbar.addWidget(self.cross)

    # navigate home
    def navigate_home(self):
        self.browser.setUrl(QUrl("https://google.com"))

    # navigate search bos / url text-box
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    # update the url in textbox
    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("Error-404")
window = main_window()
app.exec()