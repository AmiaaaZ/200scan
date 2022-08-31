import streamlit as st
st.set_page_config(page_title="Fofa Docs", page_icon="🍻", layout="wide")
st.title('- Fofa Docs -')

st.write('完整文档参见-> https://fofa.info/api')

tab1, tab2, tab3 = st.tabs(["查询接口支持的字段(search)", "统计聚合接口支持的字段(search stats)", "Host聚合接口支持的字段(search host)"])

with tab1:
    doc1 = '''
| 序号 | 字段名          | 描述                                             | 权限     |
| ---- | --------------- | ------------------------------------------------ | -------- |
| 1    | ip              | ip地址                                           | 无       |
| 2    | port            | 端口                                             | 无       |
| 3    | protocol        | 协议名                                           | 无       |
| 4    | country         | 国家代码                                         | 无       |
| 5    | country_name    | 国家名                                           | 无       |
| 6    | region          | 区域                                             | 无       |
| 7    | city            | 城市                                             | 无       |
| 8    | longitude       | 地理位置 经度                                    | 无       |
| 9    | latitude        | 地理位置 纬度                                    | 无       |
| 10   | as_number       | asn编号                                          | 无       |
| 11   | as_organization | asn组织                                          | 无       |
| 12   | host            | 主机名                                           | 无       |
| 13   | domain          | 域名                                             | 无       |
| 14   | os              | 操作系统                                         | 无       |
| 15   | server          | 网站server                                       | 无       |
| 16   | icp             | icp备案号                                        | 无       |
| 17   | title           | 网站标题                                         | 无       |
| 18   | jarm            | jarm指纹                                         | 无       |
| 19   | header (*1)     | 网站header                                       | 无       |
| 20   | banner (*1)     | 协议banner                                       | 无       |
| 21   | cert (*1)       | 证书                                             | 企业会员 |
| 22   | body (*2)       | 网站正文内容                                     | 企业会员 |
| 23   | fid             | 网站指纹信息                                     | 企业会员 |
| 24   | structinfo      | 结构化信息（部分协议支持，比如elastic, mongodb） | 企业会员 |

*1： 当查询包含cert、banner ，size参数值最大为2000

*2： 当查询包含body, size参数值最大为500'''
    st.markdown(doc1)

with tab2:
    doc2 = '''
| 序号 | 字段名          | 描述         | 权限     |
| ---- | --------------- | ------------ | -------- |
| 1    | port            | 端口         | 无       |
| 2    | protocol        | 协议名       | 无       |
| 3    | country         | 国家代码     | 无       |
| 4    | as_number       | asn编号      | 无       |
| 5    | as_organization | asn组织      | 无       |
| 6    | domain          | 域名         | 无       |
| 7    | asset_type      | 资产类型     | 无       |
| 8    | os              | 操作系统     | 无       |
| 9    | server          | 网站server   | 无       |
| 10   | icp             | icp备案号    | 无       |
| 11   | title           | 网站标题     | 无       |
| 12   | fid             | 网站指纹信息 | 企业会员 |
'''
    st.markdown(doc2)

with tab3:
    doc3 = '''#### 普通模式(detail=False)
| 序号 | 字段名   | 描述     |
| ---- | -------- | -------- |
| 1    | port     | 端口列表 |
| 2    | protocol | 协议列表 |
| 3    | domain   | 域名列表 |
| 4    | category | 分类列表 |
| 5    | product  | 产品标签 |

#### 详情模式(detail=True)
| 序号 | 字段名         | 描述                                                         |
| ---- | -------------- | ------------------------------------------------------------ |
| 1    | products       | 产品详情列表                                                 |
| 2    | product        | 产品名                                                       |
| 3    | category       | 产品分类                                                     |
| 4    | level          | 产品分层： 5 应用层， 4 支持层， 3 服务层，2 系统层， 1 硬件层， 0 无组件分层 |
| 5    | soft_hard_code | 产品是否为硬件；值为 1 是硬件，否则为非硬件                  |
'''
    st.markdown(doc3)

