import sys
import os

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


import requests
import json

# url
url = "https://m.weibo.cn/comments/hotflow?"

# 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}

# 参数
params = {
    "id" : 4823340205736691,
    "mid" : 4823340205736691,
    # "max_id" : 139275305686179,
    "max_id_type" : 0
}

r = requests.get(url, headers = headers, params = params)

result = r.content.decode('utf8')
content = json.loads(result)
print(content['data']['max_id'])