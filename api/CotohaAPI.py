
from urllib import request
import json
import time

class CotohaAPI():
    """
    初期化メソッド
    
    引数：
        cotoha_account: CotohaAccountクラスのインスタンス
    """
    def __init__(self, cotoha_account):
        self.account = cotoha_account
        self.auth_data = None
        self.access_token = None
        self.api_data = self.__load_api_data()

    """
    cotoha_api_data.jsonからAPIの情報をロードするプライベートメソッド

    引数
        api_data_name: Cotoha APIの情報がファイルのパス
    """
    def __load_api_data(self, api_data_name="./api/data/cotoha_api_data.json"):
        with open(api_data_name, "r") as f:
            return json.loads( f.read() )

    """
    APIのトークンを取得するメソッド。
    認証済みの場合は処理を中断する。また、有効期限が切れた場合は
    """
    def setting_api_token(self):
        if not self.access_token or not self.auth_data:
            self.__gain_token()
            return
        
        endtime = int(self.auth_data['issued_at']) + int(self.auth_data['expires_in'])
        if time.time() <= endtime:
            print('token still effective')
        else:
            self.__gain_token()


    """
    認証トークンを取得するメソッド。
    正常な201レスポンス以外だった場合はエラーを投げる。
    """
    def __gain_token(self):
        response = request.urlopen(
            request.Request(
                method='POST',
                url=self.account.data["accessTokenPublish"],
                headers={
                    'Content-Type': 'application/json',
                },
                data=json.dumps({
                    "grantType": 'client_credentials',
                    "clientId": self.account.data['forDevelopers']['clientId'],
                    "clientSecret": self.account.data["forDevelopers"]['clientSecret']
                }).encode()
        ), timeout=1)
        if response.status == 201:
            self.auth_data = json.loads( response.read().decode() )
            self.access_token = self.auth_data['access_token']
        else:
            raise Exception('response status is not 201')


    """
    Cotoha APIに対してリクエストを送信するためのメソッド。

    引数：
        kind: 利用するAPIの種類。例えば、構文解析であるなら'parse'を引数として渡す。
        body_data: APIに渡したいデータを辞書型として渡す。例えば、構文解析を利用したいなら、"{'sentence': '送りたい文章'}"といったデータを渡す。
    """
    def request_submit(self, kind, body_data):
        self.setting_api_token()

        to_use_api_request = request.Request(
            method='POST',
            url=self.api_data["endpoints"][kind].replace(
                '[API Base URL]',
                self.account.data["forDevelopers"]["apiBaseURL"]
            ),
            headers={
                'Content-Type':'application/json',
                'Authorization': 'Bearer ' + self.access_token 
            },
            data=json.dumps(body_data).encode()
        )
        response = request.urlopen(to_use_api_request)
        if response.status == 200:
            return json.loads( response.read().decode())
        else:
            raise Exception('response.status is not 201')