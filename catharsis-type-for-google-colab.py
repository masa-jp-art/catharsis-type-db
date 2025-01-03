!pip install gspread oauth2client openai==0.28 google-auth google-auth-oauthlib google-auth-httplib2 pandas --upgrade

import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import openai
import pandas as pd
from google.colab import auth
from google.auth import default
import os
import json

# 生成AIを動かす関数を定義
openai.api_key = "<ここにOpenAIのAPI Keyを入れる>"

def ai(x):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "人間の仕事を助ける優秀なAIアシスタントとして、指示に従い、必要な情報を出力します。出力が長大になっても構わないので、網羅的かつ詳細に出力します。"},
            {"role": "user", "content": x},
        ]
    )
    return response["choices"][0]["message"]["content"]

# Google認証
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)

# スプレッドシートとシートを開く
sheet_url = '<ここにスプレッドシートのURLを入れる>'
spreadsheet = gc.open_by_url(sheet_url)

# 各シートを取得
sheet_catharsis = spreadsheet.worksheet('catharsis')

# シートからランダムに値を取得
catharsis_reference= random.choice(sheet_catharsis.col_values(2)[1:])
print(catharsis_reference)

# 登場人物の設定を定義

protagonist = """
<ここに主人公の人物像を入れる>
"""

SubCharacter = """
<ここにサブキャラクターの人物像を入れる>
"""

antagonist = """
<ここに主人公と対立する者の人物像を入れる>
"""

# プロットを生成
prot = ai(f"""
下記の資料を元に、「鑑賞者が体験するカタルシス」を目的とした、物語のプロットを出力してください。「鑑賞者が体験するカタルシス」にそぐわない登場人物の設定がある場合は、省いてしまって構いません。鑑賞者が規定されたカタルシスに到達するために、最大限の創造性を発揮して、完成度の高い緻密で詳細なプロットを出力してください。
\n# 資料
\n\n## 鑑賞者が体験するカタルシス: {catharsis_reference},
\n\n## 主人公の設定: {protagonist},
\n\n## サブキャラクターの設定: {SubCharacter},
\n\n## 主人公と対立する者の設定: {antagonist},
""")

print(prot)
