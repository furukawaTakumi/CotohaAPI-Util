import sys
sys.path.append('api')

import unittest
from CotohaAccount import CotohaAccount
from CotohaAPI import CotohaAPI

class TestCotohaAPI(unittest.TestCase):
    def setUp(self):
        cotoha_account = CotohaAccount('./api/data/account_data.json')
        self.cotoha = CotohaAPI(cotoha_account)

    def test_setting_api_token(self):
        self.cotoha.setting_api_token()
        self.assertEqual( str, type(self.cotoha.access_token), "設定されたapi tokenが文字列ではありません" )
        self.assertTrue( 'token_type' in self.cotoha.auth_data, "レスポンスに'token_type'が存在しません" )
        self.assertTrue( 'expires_in' in self.cotoha.auth_data, "レスポンスに'expires_in'が存在しません" )
        pass

    def test_request_submit(self):
        resdata = self.cotoha.request_submit('parse', {'sentence': '犬は歩く。'})
        self.assertLessEqual( 0, resdata['status'], 'レスポンスステータスデータが正常でありません。' )
        self.assertEqual( dict, type(resdata), 'dict型になっていません。' )
        self.assertTrue( 'result' in resdata, 'resultキーが存在していません' )
        self.assertTrue( 'chunk_info' in resdata['result'][0], 'chunk_infoキーが存在していません。')
        self.assertTrue( 'tokens' in resdata['result'][1] ,'tokensキーが存在していません')
