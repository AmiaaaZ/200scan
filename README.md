# 200scan

```bash
pip install streamlit==1.12.0
streamlit run .\app\main.py
# localhost:8501
```

批量访问url，探测存活情况并返回简单信息（状态码、大小、标题、实际IP）

支持完整的url或仅ip（可选http或https协议），可自定义访问时的线程数、两次访问的delay_time、单次访问的timeout_time、是否使用代理，扫描结果支持按列排序查看，可导出CSV

![运行截图](.\image.jpg)

------

*自用99新，功能比较简单，欢迎issue

会长期更新捏QwQ
