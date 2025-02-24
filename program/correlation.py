import sqlite3
import pandas as pd

from program.config import DB_PATH

col_names = [
"廃棄率",
"エネルギーkJ",
"エネルギーkcal",
"水分",
"アミノ酸組成によるたんぱく質",
"たんぱく質",
"脂肪酸のトリアシルグリセロール当量",
"コレステロール",
"脂質",
"利用可能炭水化物（単糖当量）",
"利用可能炭水化物（質量計）",
"差引き法による利用可能炭水化物",
"食物繊維総量",
"糖アルコール",
"炭水化物",
"有機酸",
"灰分",
"ナトリウム",
"カリウム",
"カルシウム",
"マグネシウム",
"リン",
"鉄",
"亜鉛",
"銅",
"マンガン",
"ヨウ素",
"セレン",
"クロム",
"モリブデン",
"レチノール",
"α-カロテン",
"β-カロテン",
"β-クリプトキサンチン",
"β-カロテン等量",
"レチノール活性等量",
"ビタミンD",
"α-トコフェノール",
"β-トコフェノール",
"γ-トコフェノール",
"δ-トコフェノール",
"ビタミンK",
"ビタミンB1",
"ビタミンB2",
"ナイアシン",
"ナイアシン等量",
"ビタミンB6",
"ビタミンB12",
"葉酸",
"パントテン酸",
"ビオチン",
"ビタミンC",
"アルコール",
"食塩相当量",
]

corrs = []

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()

    for col_name in col_names:
        query = f'SELECT "索引番号","{col_name}", "好み" FROM "食品" WHERE "{col_name}" IS NOT NULL AND "好み" IS NOT NULL'
        df = pd.read_sql_query(query, conn)
        query = f'SELECT "{col_name}", "好み" FROM "食品" WHERE "{col_name}" IS NOT NULL AND "好み" IS NOT NULL'
        df = pd.read_sql_query(query, conn)

        correlation_matrix = df.corr("pearson")
        corrs.append((col_name , correlation_matrix.to_numpy()[0][1]))

corrs.sort(key=lambda a: a[1], reverse=True)
for item in corrs:
    print(f'{item[0]} {item[1]}')


