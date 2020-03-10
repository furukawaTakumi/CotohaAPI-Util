import sys
sys.path.append('api')

import unittest 
from CotohaAccount import CotohaAccount

class TestCotohaAccount(unittest.TestCase):
    def test_init(self):
        self.cotoha_account = CotohaAccount('./api/data/account_data.json')
        self.assertTrue(dict, type(self.cotoha_account.data))

        account_dict = self.cotoha_account.data
        self.assertTrue("accessTokenPublish" in account_dict, "accessTokenPublishが定義されていません")
        self.assertTrue("forDevelopers" in account_dict, "forDevelopersが定義されていません")
        self.assertTrue("clientSecret" in account_dict["forDevelopers"], "clientSecretが定義されていません")
        
