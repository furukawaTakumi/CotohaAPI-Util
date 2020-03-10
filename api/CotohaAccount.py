
import json

"""
Cotohaのアカウントデータファイルを読み込み、データを提供するクラス
"""
class CotohaAccount():
    def __init__(self, file_name):
        self.data = {}
        with open(file_name, "r") as f:
            account_str = f.read()
            self.data = json.loads(account_str)