"""
利用サンプル
"""

from api.CotohaAccount import CotohaAccount
from api.CotohaAPI import CotohaAPI

account = CotohaAccount('api/data/account_data.json')
cotoha_api = CotohaAPI(account)

parse_res = cotoha_api.request_submit('parse', {
    'sentence': '犬も歩けば棒に当たる'
    })
similarity_res = cotoha_api.request_submit('similarity', {
    's1': 'わけわかめ',
    's2': '意味がわからないよ',
    'type': 'kuzure'
    })

print(parse_res)
print(similarity_res)