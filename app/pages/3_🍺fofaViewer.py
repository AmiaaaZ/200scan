import pandas as pd
import streamlit as st
import fofa     # 如运行报错请直接复制[fofa.client](https://github.com/fofapro/fofa-py/blob/master/fofa/client.py)到此处

if __name__ == '__main__':
    st.set_page_config(page_title="Fofa viewer", page_icon="🍺", layout="wide")
    st.title('- Fofa viewer -')
    col1, col2 = st.columns([1, 2], gap='medium')

    with col1:
        query_str = st.text_input('query_str')

        options = st.radio('options', ['search', 'search_host', 'search_stats'])
        _fields = st.multiselect('fields', ['ip', 'port', 'protocol', 'country', 'country_name', 'region', 'city', 'longitude', 'latitude', 'as_number', 'as_organization', 'host', 'domain', 'os', 'server', 'icp', 'title', 'jarm', 'header', 'banner', 'cert', 'body', 'fid', 'structinfo'], ['host', 'ip', 'port', 'title', 'protocol', 'banner', 'server'])
        fields = ','.join(_fields)
        page = st.slider('page', 1, 10, 1)
        size = st.slider('size', 10, 500, 10)
        with st.expander('↓↓↓ enter email & key here'):
            email = st.text_input('email')
            key = st.text_input('api_key')

        if query_str and email and key:
            # st.write('Current Fcoin: ' + str(client.get_userinfo()['fcoin']))
            client = fofa.Client(email, key)
            if options == 'search':
                res = client.search(query_str, page, size, fields)
            elif options == 'search_host':
                res = client.search_host(query_str, detail=True)
            elif options == 'search_stats':
                res = client.search_stats(query_str, page, fields)

            with col2:
                df = pd.DataFrame(res['results'])
                df.columns = _fields
                st.dataframe(df)
                csv = df.to_csv(encoding='utf_8_sig')   # 虽然但是excel打开还是乱码TAT
                st.download_button("Download results as CSV", csv, "fofa_result.csv", "text/csv")
        else:
            pass

