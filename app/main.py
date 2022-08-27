# version1.7 @AmiaaaZ
import streamlit as st
import pandas as pd
from streamlit.runtime.scriptrunner import add_script_run_ctx
import requests
import time
import re
import threading

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'}
requests.packages.urllib3.disable_warnings()
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def getList(urls, protocol):
    for _ in urls:
        url_list = urls.split("\n")
    if protocol == 'http':
        for _ in url_list:
            _ = f'http://{_}/'
    elif protocol == 'https':
        for _ in url_list:
            _ = f'https://{_}/'
    elif protocol == 'none':
        pass
    return url_list, len(url_list)


def getURL(url_list, work_now, delay_time, timeout_time):
    for i in range(work_num):
        url = url_list[work_now + i]
        try:
            alive = 1
            r = requests.get(url, verify=False, allow_redirects=True, stream=True, headers=headers, timeout=timeout_time)
            # r = requests.get(url, verify=False, proxies = proxies, allow_redirects=True, stream=True, headers=headers, timeout=timeout_time)

            ip = r.raw._connection.sock.getpeername()[0]

            if r.encoding == "ISO-8859-1":
                r.encoding = "gbk-2312"
            title_pat = r'(?<=<title>).*?(?=</title>)'
            title_ex = re.compile(title_pat, re.M | re.S)
            title = re.search(title_ex, r.text).group().strip()
            if str(title).count('\\x') >= 1:
                title = title.encode('latin1').decode('utf-8')
            elif str(title).count('&#x') >= 1 or (str(title).count('&') + str(title).count(';')) >= 2:
                import html
                title = (html.unescape(title))

            result = f"[+] {url.ljust(30)} - {ip.ljust(15)} - {r.status_code} - {str(r.headers.get('content-length')).center(6)} - {''.join(title)}"
            df.loc[df.shape[0]] = dict(zip(df.columns, [url, alive, str(r.status_code), str(r.headers.get('content-length')), ''.join(title), ip]))

        except:
            result = f"[-] {url}"
            alive = 0
            df.loc[df.shape[0]] = dict(zip(df.columns, [url, alive]))
        result_file.writelines(result + '\n')
        time.sleep(delay_time)


if __name__ == '__main__':
    st.set_page_config(page_title="200 Scan", page_icon="🍥", layout="wide")
    st.title('- 200 Scan -')
    col1, col2 = st.columns([1.2, 2], gap='medium')

    with col1:
        urls = st.text_area('urls here', height=300)
        protocol = st.radio('protocol', ('http', 'https', 'none'))
        run = st.button("run")

        with st.expander('more options'):
            thread_num = st.slider("thread_num", min_value=1, max_value=50, value=10)
            delay_time = st.slider("delay_time", min_value=0, max_value=10, value=0)
            timeout_time = st.slider("timeout_time", min_value=0, max_value=10, value=3)
            result_file = st.text_input("result_file", value=".\\result.txt")

        if run:
            df = pd.DataFrame(columns=("Url", "Alive", "Status", "Length", "Title", "IP"))
            time1 = time.time()
            result_file = open(result_file, 'a', encoding='utf-8')
            url_list, urls_num = getList(urls, protocol)
            info = f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}  -  <targets: {urls_num}>'
            result_file.writelines(info + '\n')

            threads = []
            work_num = urls_num // thread_num

            for i in range(thread_num):
                t = threading.Thread(target=getURL, args=[url_list, (i - 1) * work_num, delay_time, timeout_time])
                t = add_script_run_ctx(t)
                threads.append(t)
            for i in range(thread_num):
                threads[i].start()
            for i in range(thread_num):
                threads[i].join()

            time2 = time.time()
            info2 = f'⏰total {time2 - time1}s'
            result_file.writelines(f'[*] scan over... {info2}\n\n')
            result_file.close()

            with col2:
                st.subheader(info2)
                st.dataframe(df)
                csv = df.to_csv(encoding='utf_8_sig')   # 虽然但是excel打开还是乱码TAT
                st.download_button("Download results as CSV", csv, "scan_result.csv", "text/csv")
        else:
            with col2:
                pass

