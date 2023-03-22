# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd

def main():
    """코드 작성""" 

    st.title("Hello World")

    st.text('this is {}'.format('good'))
    
    st.header('This is header')

    st.subheader('This is sub Header')

    st.markdown('## This is Markdown Header')

    # Colored Text
    st.success('성공')
    st.warning('위험함')
    st.info('This is information')
    st.error('This is an error')
    st.exception('This is an exception')

    # 수퍼펑션
    st.write(1+1)
    st.write(type(3))

    a=1
    b=2
    st.write(a+b)

    st.write(dir(str))
    st.help(range)
    
    iris = pd.read_csv("data/iris.csv")
    st.dataframe(iris, 200, 100)

    # 색상 추가     <- dataframe : 스크롤바 있음
    st.title('Adding Color on Table')
    st.dataframe(iris.style.highlight_max(axis=0))

    # static table show  <- 스크롤바 없음, 전부 표시
    st.table(iris.head())

    # st.write <- 스크롤바 있음
    st.write(iris)

    # 나의 코드 보여주기
    myCode = """
    def hello():
        print("Hello World")
    """

    st.code(myCode, language='Python')

    # Widges, 버튼, 체크박스
    name = "Dongmin"

    if st.button('Submit'):
        st.write(f'name : {name.upper()}')

    if st.button('Submit', key = 'new02'):
        st.write(f'name : {name.lower()}')

    # Radio button
    status = st.radio("Status", ("활성화", "비활성화"))
    st.write(status)
    if status == "활성화":
        st.success("활성화 상태")
    elif status == "비활성화":
        st.error("비활성화 상태")
    else:
        pass

    # Check Box
    if st.checkbox('Show/Hide'):
        st.text('보여줘!')

if __name__ == "__main__":
    main()