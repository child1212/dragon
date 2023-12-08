#%%
##pip install -e git+https://github.com/kpu/kenlm.git#egg=kenlm
import pycorrector
corrected_sent, detail = pycorrector.correct('少先队员因该为老人让坐')
print(corrected_sent, detail)
# %%
# https://github.com/textproofreading/cuobiezi_http_api
# https://www.xfyun.cn/doc/nlp/textCorrection/API.html#%E9%BB%91%E7%99%BD%E5%90%8D%E5%8D%95%E4%B8%8A%E4%BC%A0