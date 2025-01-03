# 概要
- このプロジェクトでは、OpenAI o1 proが出力した「鑑賞者が体験するカタルシス」のタイプの分類データからデータベースを作り、ランダムに取り出した「鑑賞者が体験するカタルシス」を目的として物語のプロットのアイデアを生成します。
- このプロジェクトは、ChatGPT Proで使用できる、OpenAIのo1 pro modeの検証を兼ねています

# 手順
- ChatGPT Proのo1 pro modeに、「鑑賞者が体験するカタルシス」を分類させます
  - [catharsis-type.md](https://github.com/masa-jp-art/catharsis-type-db/blob/main/catharsis-type.md)
- 出力されたプロットタイプをスプレッドシートに転記してデータベースを作ります
  - [20250103-catharsis-type-snapshot](https://docs.google.com/spreadsheets/d/1xhIcB0q_PTHrhzuIpWXO23FG2zeVEKbYzZtP-7ES7co/edit)
- Google colabでプログラムを動かし、キャラクターとあらすじを生成します
  - [catharsis-type-for-google-colab.py](https://github.com/masa-jp-art/catharsis-type-db/blob/main/catharsis-type-for-google-colab.py)
 
# 関連
- [OpenAI o1 pro mode検証: 鑑賞者にもたらすカタルシスを分類しデータベース化できるか](https://note.com/msfmnkns/n/n34d4b813cefd)
