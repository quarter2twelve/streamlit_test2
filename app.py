import streamlit as st
from PIL import Image
import datetime
import pandas as pd


st.title('売上日計表 ダッシュボード')
st.caption('streamlitを用いたテストアプリ')
st.subheader('サブヘッダー')
st.text('サブヘッダーの下に表示されるテキストです\n'
        '改行するには"\n"を使用')

date1 = datetime.date.today() 


code = '''
import streamlit as st

st.title('売上日計表 ダッシュボード')
'''
st.code(code, language='python')

# 画像
image = Image.open('Barbados.png')
st.image(image, width=600)



with st.form(key='profile_form'):

    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')
    
    # 日付
    start_date = st.date_input(
        '売上日',
        )
    
    # セレクトボックス
    staff_ID = st.selectbox(
        '担当者ID',
        (11,12,13))
    
    # 複数選択
    product_cat = st.multiselect(
        '製品カテゴリ',
        ('DSP', 'DSP/AMP', 'SP KIT','SUB', 'BOX SUB')
    )


    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ{name}さん!{address}に書類を送付しました！')
        st.text(f'担当者ID: {staff_ID}')
        
    
# データ分析関連
df = pd.read_excel('sales.xlsx', index_col='売上番号')
st.dataframe(df)





