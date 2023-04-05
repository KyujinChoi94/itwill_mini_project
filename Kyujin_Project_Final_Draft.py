# -*- coding: utf-8 -*-
"""
Kyujin Choi Project
"""
import FinanceDataReader as fdr
import pandas as pd

def Finace_data(code, name):
    # 데이터 얻기
    data = fdr.DataReader(code, start='2022-01-01', end='2022-12-31')
    # 결측지 제거
    data.dropna(inplace=True)
    # csv로 저장
    path = r'C:\ITWILL\3_TextMining'
    data.to_csv(f'{path}/df_{name}_data.csv')

#함수 실행
Finace_data('005930', 'Samsung')

########################################################################################################################################

# CSV 파일 불러오기

path = r'C:\ITWILL\3_TextMining'
df = pd.read_csv(f'{path}/df_Samsung_data.csv')

print(df.iloc[:, 0].tolist()) # index 칼럼인 Date 만 불러오기

dates = ['2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-10', '2022-01-11', '2022-01-12', '2022-01-13', '2022-01-14', '2022-01-17', '2022-01-18', '2022-01-19', '2022-01-20', '2022-01-21', '2022-01-24', '2022-01-25', '2022-01-26', '2022-01-27', '2022-01-28', '2022-02-03', '2022-02-04', '2022-02-07', '2022-02-08', '2022-02-09', '2022-02-10', '2022-02-11', '2022-02-14', '2022-02-15', '2022-02-16', '2022-02-17', '2022-02-18', '2022-02-21', '2022-02-22', '2022-02-23', '2022-02-24', '2022-02-25', '2022-02-28', '2022-03-02', '2022-03-03', '2022-03-04', '2022-03-07', '2022-03-08', '2022-03-10', '2022-03-11', '2022-03-14', '2022-03-15', '2022-03-16', '2022-03-17', '2022-03-18', '2022-03-21', '2022-03-22', '2022-03-23', '2022-03-24', '2022-03-25', '2022-03-28', '2022-03-29', '2022-03-30', '2022-03-31', '2022-04-01', '2022-04-04', '2022-04-05', '2022-04-06', '2022-04-07', '2022-04-08', '2022-04-11', '2022-04-12', '2022-04-13', '2022-04-14', '2022-04-15', '2022-04-18', '2022-04-19', '2022-04-20', '2022-04-21', '2022-04-22', '2022-04-25', '2022-04-26', '2022-04-27', '2022-04-28', '2022-04-29', '2022-05-02', '2022-05-03', '2022-05-04', '2022-05-06', '2022-05-09', '2022-05-10', '2022-05-11', '2022-05-12', '2022-05-13', '2022-05-16', '2022-05-17', '2022-05-18', '2022-05-19', '2022-05-20', '2022-05-23', '2022-05-24', '2022-05-25', '2022-05-26', '2022-05-27', '2022-05-30', '2022-05-31', '2022-06-02', '2022-06-03', '2022-06-07', '2022-06-08', '2022-06-09', '2022-06-10', '2022-06-13', '2022-06-14', '2022-06-15', '2022-06-16', '2022-06-17', '2022-06-20', '2022-06-21', '2022-06-22', '2022-06-23', '2022-06-24', '2022-06-27', '2022-06-28', '2022-06-29', '2022-06-30', '2022-07-01', '2022-07-04', '2022-07-05', '2022-07-06', '2022-07-07', '2022-07-08', '2022-07-11', '2022-07-12', '2022-07-13', '2022-07-14', '2022-07-15', '2022-07-18', '2022-07-19', '2022-07-20', '2022-07-21', '2022-07-22', '2022-07-25', '2022-07-26', '2022-07-27', '2022-07-28', '2022-07-29', '2022-08-01', '2022-08-02', '2022-08-03', '2022-08-04', '2022-08-05', '2022-08-08', '2022-08-09', '2022-08-10', '2022-08-11', '2022-08-12', '2022-08-16', '2022-08-17', '2022-08-18', '2022-08-19', '2022-08-22', '2022-08-23', '2022-08-24', '2022-08-25', '2022-08-26', '2022-08-29', '2022-08-30', '2022-08-31', '2022-09-01', '2022-09-02', '2022-09-05', '2022-09-06', '2022-09-07', '2022-09-08', '2022-09-13', '2022-09-14', '2022-09-15', '2022-09-16', '2022-09-19', '2022-09-20', '2022-09-21', '2022-09-22', '2022-09-23', '2022-09-26', '2022-09-27', '2022-09-28', '2022-09-29', '2022-09-30', '2022-10-04', '2022-10-05', '2022-10-06', '2022-10-07', '2022-10-11', '2022-10-12', '2022-10-13', '2022-10-14', '2022-10-17', '2022-10-18', '2022-10-19', '2022-10-20', '2022-10-21', '2022-10-24', '2022-10-25', '2022-10-26', '2022-10-27', '2022-10-28', '2022-10-31', '2022-11-01', '2022-11-02', '2022-11-03', '2022-11-04', '2022-11-07', '2022-11-08', '2022-11-09', '2022-11-10', '2022-11-11', '2022-11-14', '2022-11-15', '2022-11-16', '2022-11-17', '2022-11-18', '2022-11-21', '2022-11-22', '2022-11-23', '2022-11-24', '2022-11-25', '2022-11-28', '2022-11-29', '2022-11-30', '2022-12-01', '2022-12-02', '2022-12-05', '2022-12-06', '2022-12-07', '2022-12-08', '2022-12-09', '2022-12-12', '2022-12-13', '2022-12-14', '2022-12-15', '2022-12-16', '2022-12-19', '2022-12-20', '2022-12-21', '2022-12-22', '2022-12-23', '2022-12-26', '2022-12-27', '2022-12-28', '2022-12-29']
#자료가 있는 날짜만 기준으로 뽑혔으니 이 날짜로만 url 생성
len(dates)

# url 생성기
import urllib.parse
text_inputs = ["삼성전자"]

results = []
for text in text_inputs:
    encoded_string = text.encode('euc-kr')
    encoded_result = encoded_string.hex().upper()
    encoded_bytes = bytes.fromhex(encoded_result)
    encoded_string = encoded_bytes.decode('euc-kr')
    encoded_string = urllib.parse.quote(encoded_string, encoding='euc-kr')
    results.append(encoded_string)

print(results)
#      %BB%EF%BC%BA%C0%FC%C0%DA


urls = []
def url_maker(dates):
    for date in (dates):
        url = f"https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart={date}&stDateEnd={date}"
        urls.append(url)

#함수 실행
url_maker(dates)

print(urls)
urls = ['https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-03&stDateEnd=2022-01-03', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-04&stDateEnd=2022-01-04', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-05&stDateEnd=2022-01-05', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-06&stDateEnd=2022-01-06', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-07&stDateEnd=2022-01-07', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-10&stDateEnd=2022-01-10', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-11&stDateEnd=2022-01-11', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-12&stDateEnd=2022-01-12', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-13&stDateEnd=2022-01-13', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-14&stDateEnd=2022-01-14', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-17&stDateEnd=2022-01-17', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-18&stDateEnd=2022-01-18', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-19&stDateEnd=2022-01-19', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-20&stDateEnd=2022-01-20', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-21&stDateEnd=2022-01-21', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-24&stDateEnd=2022-01-24', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-25&stDateEnd=2022-01-25', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-26&stDateEnd=2022-01-26', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-27&stDateEnd=2022-01-27', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-28&stDateEnd=2022-01-28', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-03&stDateEnd=2022-02-03', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-04&stDateEnd=2022-02-04', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-07&stDateEnd=2022-02-07', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-08&stDateEnd=2022-02-08', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-09&stDateEnd=2022-02-09', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-10&stDateEnd=2022-02-10', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-11&stDateEnd=2022-02-11', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-14&stDateEnd=2022-02-14', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-15&stDateEnd=2022-02-15', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-16&stDateEnd=2022-02-16', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-17&stDateEnd=2022-02-17', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-18&stDateEnd=2022-02-18', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-21&stDateEnd=2022-02-21', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-22&stDateEnd=2022-02-22', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-23&stDateEnd=2022-02-23', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-24&stDateEnd=2022-02-24', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-25&stDateEnd=2022-02-25', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-28&stDateEnd=2022-02-28', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-02&stDateEnd=2022-03-02', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-03&stDateEnd=2022-03-03', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-04&stDateEnd=2022-03-04', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-07&stDateEnd=2022-03-07', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-08&stDateEnd=2022-03-08', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-10&stDateEnd=2022-03-10', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-11&stDateEnd=2022-03-11', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-14&stDateEnd=2022-03-14', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-15&stDateEnd=2022-03-15', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-16&stDateEnd=2022-03-16', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-17&stDateEnd=2022-03-17', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-18&stDateEnd=2022-03-18', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-21&stDateEnd=2022-03-21', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-22&stDateEnd=2022-03-22', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-23&stDateEnd=2022-03-23', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-24&stDateEnd=2022-03-24', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-25&stDateEnd=2022-03-25', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-28&stDateEnd=2022-03-28', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-29&stDateEnd=2022-03-29', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-30&stDateEnd=2022-03-30', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-31&stDateEnd=2022-03-31', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-01&stDateEnd=2022-04-01', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-04&stDateEnd=2022-04-04', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-05&stDateEnd=2022-04-05', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-06&stDateEnd=2022-04-06', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-07&stDateEnd=2022-04-07', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-08&stDateEnd=2022-04-08', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-11&stDateEnd=2022-04-11', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-12&stDateEnd=2022-04-12', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-13&stDateEnd=2022-04-13', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-14&stDateEnd=2022-04-14', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-15&stDateEnd=2022-04-15', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-18&stDateEnd=2022-04-18', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-19&stDateEnd=2022-04-19', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-20&stDateEnd=2022-04-20', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-21&stDateEnd=2022-04-21', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-22&stDateEnd=2022-04-22', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-25&stDateEnd=2022-04-25', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-26&stDateEnd=2022-04-26', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-27&stDateEnd=2022-04-27', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-28&stDateEnd=2022-04-28', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-29&stDateEnd=2022-04-29', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-02&stDateEnd=2022-05-02', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-03&stDateEnd=2022-05-03', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-04&stDateEnd=2022-05-04', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-06&stDateEnd=2022-05-06', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-09&stDateEnd=2022-05-09', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-10&stDateEnd=2022-05-10', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-11&stDateEnd=2022-05-11', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-12&stDateEnd=2022-05-12', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-13&stDateEnd=2022-05-13', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-16&stDateEnd=2022-05-16', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-17&stDateEnd=2022-05-17', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-18&stDateEnd=2022-05-18', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-19&stDateEnd=2022-05-19', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-20&stDateEnd=2022-05-20', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-23&stDateEnd=2022-05-23', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-24&stDateEnd=2022-05-24', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-25&stDateEnd=2022-05-25', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-26&stDateEnd=2022-05-26', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-27&stDateEnd=2022-05-27', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-30&stDateEnd=2022-05-30', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-05-31&stDateEnd=2022-05-31', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-02&stDateEnd=2022-06-02', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-03&stDateEnd=2022-06-03', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-07&stDateEnd=2022-06-07', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-08&stDateEnd=2022-06-08', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-09&stDateEnd=2022-06-09', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-10&stDateEnd=2022-06-10', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-13&stDateEnd=2022-06-13', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-14&stDateEnd=2022-06-14', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-15&stDateEnd=2022-06-15', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-16&stDateEnd=2022-06-16', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-17&stDateEnd=2022-06-17', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-20&stDateEnd=2022-06-20', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-21&stDateEnd=2022-06-21', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-22&stDateEnd=2022-06-22', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-23&stDateEnd=2022-06-23', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-24&stDateEnd=2022-06-24', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-27&stDateEnd=2022-06-27', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-28&stDateEnd=2022-06-28', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-29&stDateEnd=2022-06-29', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-06-30&stDateEnd=2022-06-30', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-01&stDateEnd=2022-07-01', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-04&stDateEnd=2022-07-04', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-05&stDateEnd=2022-07-05', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-06&stDateEnd=2022-07-06', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-07&stDateEnd=2022-07-07', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-08&stDateEnd=2022-07-08', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-11&stDateEnd=2022-07-11', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-12&stDateEnd=2022-07-12', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-13&stDateEnd=2022-07-13', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-14&stDateEnd=2022-07-14', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-15&stDateEnd=2022-07-15', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-18&stDateEnd=2022-07-18', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-19&stDateEnd=2022-07-19', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-20&stDateEnd=2022-07-20', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-21&stDateEnd=2022-07-21', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-22&stDateEnd=2022-07-22', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-25&stDateEnd=2022-07-25', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-26&stDateEnd=2022-07-26', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-27&stDateEnd=2022-07-27', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-28&stDateEnd=2022-07-28', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-29&stDateEnd=2022-07-29', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-01&stDateEnd=2022-08-01', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-02&stDateEnd=2022-08-02', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-03&stDateEnd=2022-08-03', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-04&stDateEnd=2022-08-04', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-05&stDateEnd=2022-08-05', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-08&stDateEnd=2022-08-08', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-09&stDateEnd=2022-08-09', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-10&stDateEnd=2022-08-10', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-11&stDateEnd=2022-08-11', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-12&stDateEnd=2022-08-12', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-16&stDateEnd=2022-08-16', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-17&stDateEnd=2022-08-17', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-18&stDateEnd=2022-08-18', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-19&stDateEnd=2022-08-19', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-22&stDateEnd=2022-08-22', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-23&stDateEnd=2022-08-23', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-24&stDateEnd=2022-08-24', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-25&stDateEnd=2022-08-25', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-26&stDateEnd=2022-08-26', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-29&stDateEnd=2022-08-29', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-30&stDateEnd=2022-08-30', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-08-31&stDateEnd=2022-08-31', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-01&stDateEnd=2022-09-01', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-02&stDateEnd=2022-09-02', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-05&stDateEnd=2022-09-05', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-06&stDateEnd=2022-09-06', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-07&stDateEnd=2022-09-07', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-08&stDateEnd=2022-09-08', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-13&stDateEnd=2022-09-13', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-14&stDateEnd=2022-09-14', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-15&stDateEnd=2022-09-15', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-16&stDateEnd=2022-09-16', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-19&stDateEnd=2022-09-19', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-20&stDateEnd=2022-09-20', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-21&stDateEnd=2022-09-21', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-22&stDateEnd=2022-09-22', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-23&stDateEnd=2022-09-23', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-26&stDateEnd=2022-09-26', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-27&stDateEnd=2022-09-27', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-28&stDateEnd=2022-09-28', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-29&stDateEnd=2022-09-29', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-09-30&stDateEnd=2022-09-30', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-04&stDateEnd=2022-10-04', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-05&stDateEnd=2022-10-05', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-06&stDateEnd=2022-10-06', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-07&stDateEnd=2022-10-07', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-11&stDateEnd=2022-10-11', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-12&stDateEnd=2022-10-12', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-13&stDateEnd=2022-10-13', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-14&stDateEnd=2022-10-14', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-17&stDateEnd=2022-10-17', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-18&stDateEnd=2022-10-18', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-19&stDateEnd=2022-10-19', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-20&stDateEnd=2022-10-20', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-21&stDateEnd=2022-10-21', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-24&stDateEnd=2022-10-24', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-25&stDateEnd=2022-10-25', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-26&stDateEnd=2022-10-26', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-27&stDateEnd=2022-10-27', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-28&stDateEnd=2022-10-28', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-31&stDateEnd=2022-10-31', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-01&stDateEnd=2022-11-01', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-02&stDateEnd=2022-11-02', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-03&stDateEnd=2022-11-03', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-04&stDateEnd=2022-11-04', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-07&stDateEnd=2022-11-07', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-08&stDateEnd=2022-11-08', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-09&stDateEnd=2022-11-09', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-10&stDateEnd=2022-11-10', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-11&stDateEnd=2022-11-11', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-14&stDateEnd=2022-11-14', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-15&stDateEnd=2022-11-15', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-16&stDateEnd=2022-11-16', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-17&stDateEnd=2022-11-17', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-18&stDateEnd=2022-11-18', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-21&stDateEnd=2022-11-21', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-22&stDateEnd=2022-11-22', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-23&stDateEnd=2022-11-23', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-24&stDateEnd=2022-11-24', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-25&stDateEnd=2022-11-25', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-28&stDateEnd=2022-11-28', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-29&stDateEnd=2022-11-29', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-11-30&stDateEnd=2022-11-30', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-01&stDateEnd=2022-12-01', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-02&stDateEnd=2022-12-02', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-05&stDateEnd=2022-12-05', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-06&stDateEnd=2022-12-06', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-07&stDateEnd=2022-12-07', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-08&stDateEnd=2022-12-08', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-09&stDateEnd=2022-12-09', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-12&stDateEnd=2022-12-12', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-13&stDateEnd=2022-12-13', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-14&stDateEnd=2022-12-14', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-15&stDateEnd=2022-12-15', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-16&stDateEnd=2022-12-16', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-19&stDateEnd=2022-12-19', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-20&stDateEnd=2022-12-20', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-21&stDateEnd=2022-12-21', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-22&stDateEnd=2022-12-22', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-23&stDateEnd=2022-12-23', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-26&stDateEnd=2022-12-26', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-27&stDateEnd=2022-12-27', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-28&stDateEnd=2022-12-28', 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%BB%EF%BC%BA%C0%FC%C0%DA&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-29&stDateEnd=2022-12-29']
len(urls) # 246

########################################################################################################################################

#뉴스 크롤링으로 날짜별 뉴스를 모으기

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def scrape_news(date, url):
    subjects = []
    summaries = []
    news_dates = []

    for page in range(1, 3):
        response = requests.get(f"{url}&page={page}")
        soup = BeautifulSoup(response.content, "html.parser")

        for subject, summary in zip(soup.find_all("dd", class_="articleSubject"), soup.find_all("dd", class_="articleSummary")):
        
            subject_str = re.sub('[^a-zA-Z가-힣\s]', '', subject.text.replace('\n', '').replace('\t', ''))
            subjects.append(subject_str)

            summary_str = re.sub('[^a-zA-Z가-힣\s]', '', summary.text.replace('\n', '').replace('\t', ''))
            summaries.append(summary_str)

            news_dates.append(date)

    if len(subjects) == len(summaries):
        data = {"dates": news_dates, "subjects": subjects, "summaries": summaries}
        df = pd.DataFrame(data, index=None)
        path = r"C:\ITWILL\3_TextMining"
        df.to_csv(f"{path}/samsung_news_crawl.csv", mode='a',header=False, index=False)

for date, url in zip(dates, urls):
    scrape_news(date, url)

########################################################################################################################################

# 파일 불러오기
path = r"C:\ITWILL\3_TextMining"
df_crawl = pd.read_csv(f'{path}/samsung_news_crawl.csv')

# 칼럼 추가
df_crawl.columns = ['Date', 'Title', 'Summary']
df_crawl['Sentence'] = df_crawl['Title'] + ' ' + df_crawl['Summary']
df_crawl = df_crawl.drop(columns=['Title', 'Summary'])

# 날짜별로 그룹
grouped = df_crawl.groupby(df_crawl.columns[0], as_index=False).agg({'Sentence': ' '.join})
grouped.to_csv(f'{path}/samsung_newscrawl_grouped.csv', index=False)

########################################################################################################################################

from googletrans import Translator
import pandas as pd

# 파일 불러오기
path = r"C:\ITWILL\3_TextMining"
df_grouped = pd.read_csv(f'{path}/samsung_newscrawl_grouped.csv')

translator = Translator()

# Sentence 칼럼 번역하기
df_grouped['Sentence'] = df_grouped['Sentence'].apply(lambda x: translator.translate(x, src='ko', dest='en').text)

# 파일 저장하기
df_grouped.to_csv(f'{path}/samsung_newscrawl_translated.csv', index=False)

########################################################################################################################################

# Affin 사용하여 날짜별 점수를 모으기
import pandas as pd
from afinn import Afinn

path = r"C:\ITWILL\3_TextMining"
df_translated = pd.read_csv(f'{path}/samsung_newscrawl_translated.csv')

afinn = Afinn()

# Add a new column "Afinn" with the Afinn scores
df_translated['Afinn'] = df_translated['Sentence'].apply(lambda x: afinn.score(x))

# Afinn 점수가 40점 이상이면 긍정, 미만이면 부정으로 나타냄
df_translated['Pos_Neg'] = df_translated['Afinn'].apply(lambda x: 'Positive' if x >= 40 else 'Negative')

# Drop the "Sentence" column
df_translated = df_translated.drop(columns=['Sentence'])

df_translated.to_csv(f'{path}/samsung_newscrawl_afinn_scores.csv', index=False)

########################################################################################################################################

#파일을 하나의 데이터프레임으로 만들기
path = r'C:\ITWILL\3_TextMining'

# 삼성 데이터 불러옴
df = pd.read_csv(f'{path}/df_Samsung_data.csv')
df_affin_scores = pd.read_csv(f'{path}/samsung_newscrawl_afinn_scores.csv')

# 두 파일 합치기
merged_df = pd.merge(df, df_affin_scores, on='Date')
merged_df.to_csv(f'{path}/samsung_merged.csv', index=False) # index 열 제외

########################################################################################################################################

#정확도 예측하기 

path = r'C:\ITWILL\3_TextMining'

df_final = pd.read_csv(f'{path}/samsung_merged.csv')

# 긍정과 부정예측이 맞는 부분 갯수 세기
df_final['Pos_Count'] = ((df_final['Change'] > 0) & (df_final['Pos_Neg'] == 'Positive')).astype(int)
df_final['Neg_Count'] = ((df_final['Change'] < 0) & (df_final['Pos_Neg'] == 'Negative')).astype(int)

(df_final["Pos_Count"].sum() + df_final["Neg_Count"].sum()) / len(df_final["Change"]) * 100      # 55.6910569105691

'''
긍정 예측 성공: 22
부정 예측 성공: 115
total value : 246

정확도 : (22+115) / 246 * 100 = 55.6910569105691 %
'''

########################################################################################################################################

#Afinn 과 Change 변수의 상관분석

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

path = r'C:\ITWILL\3_TextMining'
df_final = pd.read_csv(f'{path}/samsung_merged.csv')

#산점도 (Scatter plot)
Afinn = df_final.Afinn
Change = df_final.Change

plt.scatter(Afinn, Change, alpha = 0.5)
plt.title('Scatter Afinn Change')
plt.xlabel('Afinn')
plt.ylabel('Change')
plt.show()

#공분산
np.cov(Afinn, Change)[0,1] # 0.02332267589241042

#상관계수
np.corrcoef(Afinn, Change)[0,1]   # 0.07930514646928592

#상관계수 그래프
corr = df_final[["Afinn", "Change"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")

#피어슨 계수
import scipy.stats as stats
stats.pearsonr(Afinn, Change)   # PearsonRResult(statistic=0.07930514646928591, pvalue=0.21517130626461337)

########################################################################################################################################

# 긍정 부정값이 일치하는 행만 남기고 나머지를 drop
path = r'C:\ITWILL\3_TextMining'
df_final = pd.read_csv(f'{path}/samsung_merged.csv')

df_final['Pos_Count'] = ((df_final['Change'] > 0) & (df_final['Pos_Neg'] == 'Positive')).astype(int)
df_final['Neg_Count'] = ((df_final['Change'] < 0) & (df_final['Pos_Neg'] == 'Negative')).astype(int)

df_final_filtered = df_final[(df_final['Pos_Count'] != 0) | (df_final['Neg_Count'] != 0)]
df_final_filtered.to_csv(f'{path}/samsung_filtered_data.csv', index=False)

########################################################################################################################################

#필터된 항목으로 다시 상관분석 진행

path = r'C:\ITWILL\3_TextMining'
df_final_filtered = pd.read_csv(f'{path}/samsung_filtered_data.csv')

#산점도 (Scatter plot)
Afinn = df_final_filtered.Afinn
Change = df_final_filtered.Change

plt.scatter(Afinn, Change, alpha = 0.5)
plt.title('Scatter Afinn Change')
plt.xlabel('Afinn')
plt.ylabel('Change')
plt.show()

#공분산
np.cov(Afinn, Change)[0,1] # 0.13720858217816367

#상관계수
np.corrcoef(Afinn, Change)[0,1]   # 0.61436281454109

#상관계수 그래프
corr = df_final_filtered[["Afinn", "Change"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")

#피어슨 계수
import scipy.stats as stats
stats.pearsonr(Afinn, Change) 
# PearsonRResult(statistic=0.61436281454109, pvalue=1.411286245756649e-15)

########################################################################################################################################










'''
###############################################################################################################
    
#  두 날짜 사이의 주말제외 모든날짜를 리스트로 만드는 함수
from datetime import datetime, timedelta

def get_all_dates(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    delta = timedelta(days=1)
    dates = []
    while start <= end:
        if start.weekday() < 5:  # 5 is Saturday, 6 is Sunday
            dates.append(start.strftime('%Y-%m-%d'))
        start += delta
    return dates


start_date = '2022-01-01'
end_date = '2022-01-31'

all_dates = get_all_dates(start_date, end_date)

print(all_dates)

###############################################################################################################

# 주가의 Change(변화량)이 가장 큰 20개의 날짜를 추출함

import FinanceDataReader as fdr
import pandas as pd

def get_topN_date(code, name):
    # Get data
    data = fdr.DataReader(code, start='2020-01-01', end='2022-12-31')

    # Drop missing values
    data.dropna(inplace=True)
    
    # Save data to CSV
    path = r'C:\ITWILL\3_TextMining'
    data.to_csv(f'{path}/df_{name}_change_data.csv')
    
    # Find max and min change
    data['Abs_Change'] = data['Change'].abs()
    topN = data.sort_values(by='Abs_Change', ascending=False).head(30)
   
    # Drop the 'Abs_Change' column + 날짜 형식 변환
    topN = topN.drop('Abs_Change', axis=1)
    topN_date = topN.index.strftime('%Y-%m-%d').tolist()
    return topN_date

# Call the function max and store the results in a list
get_topN_date_list = []
get_topN_date_list.append(get_topN_date('259960', 'Krafton'))
print(f"{name}get_topN_date_list = {get_topN_date_list}")


get_topN_date_list.append(get_topN_date('251270', 'Netmarble'))
get_topN_date_list.append(get_topN_date('225570', 'Nexongames'))
get_topN_date_list.append(get_topN_date('194480', 'Devsisters'))
get_topN_date.append(get_topN_date('293490', 'Kakaogames'))


###############################################################################################################################################################################
#get_top5_date_list =  [['2022-11-11', '2022-02-11', '2021-11-11', '2021-08-11', '2022-11-02'], ['2022-12-29', '2022-05-13', '2020-09-03', '2022-01-20', '2020-10-15'], ['2021-01-05', '2021-12-17', '2022-03-03', '2022-03-25', '2021-11-03'], ['2021-02-01', '2021-09-13', '2021-01-25', '2021-01-22', '2020-11-30'], ['2020-09-11', '2021-07-02', '2022-01-06', '2022-08-03', '2021-07-22']]



#Krafton
get_topN_date_list =  ['2022-11-11', '2022-02-11', '2021-11-11', '2021-08-11', '2022-11-02', '2022-06-29', '2022-12-05', '2022-12-02', '2022-05-20', '2022-06-30', '2022-03-10', '2021-08-13', '2022-04-04', '2022-10-11', '2021-10-05', '2022-07-27', '2022-06-07', '2022-01-05', '2021-09-10', '2021-09-14', '2021-08-27', '2022-02-07', '2022-01-13', '2022-11-03', '2022-10-05', '2021-12-06', '2022-09-19', '2021-11-09', '2022-03-04', '2022-07-20']


# date 생성기
from datetime import datetime, timedelta

def date_maker(date_list):
    # Create an empty list to store the start and end dates
    dates = []
    
    # Loop through the input date list and create a tuple of start and end dates for each date
    for date_str in date_list:
        # Convert the input date string to a datetime object
        d = datetime.strptime(date_str, '%Y-%m-%d')
    
        # Calculate the start date (14 days before the input date)
        d_before = d - timedelta(days=14)
    
        # Add the start and end dates to the list of dates
        dates.append((d_before.strftime('%Y-%m-%d'), date_str))
    
    return dates


get_top5_date_list =  [['2022-11-11', '2022-02-11', '2021-11-11', '2021-08-11', '2022-11-02'], ['2022-12-29', '2022-05-13', '2020-09-03', '2022-01-20', '2020-10-15'], ['2021-01-05', '2021-12-17', '2022-03-03', '2022-03-25', '2021-11-03'], ['2021-02-01', '2021-09-13', '2021-01-25', '2021-01-22', '2020-11-30'], ['2020-09-11', '2021-07-02', '2022-01-06', '2022-08-03', '2021-07-22']]

change_top5_dates = []

# Loop through each sublist in get_top5_date_list and call the date_maker function for each of them
for date_list in get_top5_date_list:
    dates = date_maker(date_list)
    change_top5_dates.append(dates)

print('change_top5_dates = ', change_top5_dates)




###############################################################################################################################################################################
change_top5_dates =  [[('2022-10-28', '2022-11-11'), ('2022-01-28', '2022-02-11'), ('2021-10-28', '2021-11-11'), ('2021-07-28', '2021-08-11'), ('2022-10-19', '2022-11-02')], [('2022-12-15', '2022-12-29'), ('2022-04-29', '2022-05-13'), ('2020-08-20', '2020-09-03'), ('2022-01-06', '2022-01-20'), ('2020-10-01', '2020-10-15')], [('2020-12-22', '2021-01-05'), ('2021-12-03', '2021-12-17'), ('2022-02-17', '2022-03-03'), ('2022-03-11', '2022-03-25'), ('2021-10-20', '2021-11-03')], [('2021-01-18', '2021-02-01'), ('2021-08-30', '2021-09-13'), ('2021-01-11', '2021-01-25'), ('2021-01-08', '2021-01-22'), ('2020-11-16', '2020-11-30')], [('2020-08-28', '2020-09-11'), ('2021-06-18', '2021-07-02'), ('2021-12-23', '2022-01-06'), ('2022-07-20', '2022-08-03'), ('2021-07-08', '2021-07-22')]]


# url 생성기
import urllib.parse
text_inputs = ["크래프톤", "넷마블", "넥슨", "데브시스터즈", "카카오게임즈"]

results = []
for text in text_inputs:
    encoded_string = text.encode('euc-kr')
    encoded_result = encoded_string.hex().upper()
    encoded_bytes = bytes.fromhex(encoded_result)
    encoded_string = encoded_bytes.decode('euc-kr')
    encoded_string = urllib.parse.quote(encoded_string, encoding='euc-kr')
    results.append(encoded_string)


top5_urls = []
def url_maker_top5(results, change_top5_dates):
    for result,  change_top5_dates in zip(results, change_top5_dates):
        top5_url = f"https://finance.naver.com/news/news_search.naver?rcdate=&q={result}&x=0&y=0&sm=all.basic&pd=4&stDateStart={change_top5_dates[0]}&stDateEnd={change_top5_dates[1]}"
        top5_urls.append(top5_url)



url_maker_top5(results, change_top5_dates)
print(url_maker_top5)
'''
['https://finance.naver.com/news/news_search.naver?rcdate=&q=%C5%A9%B7%A1%C7%C1%C5%E6&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-28&stDateEnd=2022-11-11', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%DD%B8%B6%BA%ED&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-15&stDateEnd=2022-12-29', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%D8%BD%BC&x=0&y=0&sm=all.basic&pd=4&stDateStart=2020-12-22&stDateEnd=2021-01-05', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B5%A5%BA%EA%BD%C3%BD%BA%C5%CD%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-01-18&stDateEnd=2021-02-01', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%C4%AB%C4%AB%BF%C0%B0%D4%C0%D3%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2020-08-28&stDateEnd=2020-09-11']
'''




import urllib.parse

text_inputs = ["크래프톤", "넷마블", "넥슨", "데브시스터즈", "카카오게임즈"]

change_top5_dates =  [[('2022-10-28', '2022-11-11'), ('2022-01-28', '2022-02-11'), ('2021-10-28', '2021-11-11'), ('2021-07-28', '2021-08-11'), ('2022-10-19', '2022-11-02')], [('2022-12-15', '2022-12-29'), ('2022-04-29', '2022-05-13'), ('2020-08-20', '2020-09-03'), ('2022-01-06', '2022-01-20'), ('2020-10-01', '2020-10-15')], [('2020-12-22', '2021-01-05'), ('2021-12-03', '2021-12-17'), ('2022-02-17', '2022-03-03'), ('2022-03-11', '2022-03-25'), ('2021-10-20', '2021-11-03')], [('2021-01-18', '2021-02-01'), ('2021-08-30', '2021-09-13'), ('2021-01-11', '2021-01-25'), ('2021-01-08', '2021-01-22'), ('2020-11-16', '2020-11-30')], [('2020-08-28', '2020-09-11'), ('2021-06-18', '2021-07-02'), ('2021-12-23', '2022-01-06'), ('2022-07-20', '2022-08-03'), ('2021-07-08', '2021-07-22')]]

top5_urls = []
for text, date_list in zip(text_inputs, change_top5_dates):
    encoded_text = urllib.parse.quote(text.encode('euc-kr'))
    for start_date, end_date in date_list:
        url = f"https://finance.naver.com/news/news_search.naver?rcdate=&q={encoded_text}&x=0&y=0&sm=all.basic&pd=4&stDateStart={start_date}&stDateEnd={end_date}"
        top5_urls.append(url)

print(top5_urls)

top5_urls =[
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%C5%A9%B7%A1%C7%C1%C5%E6&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-28&stDateEnd=2022-11-11', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%C5%A9%B7%A1%C7%C1%C5%E6&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-28&stDateEnd=2022-02-11', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%C5%A9%B7%A1%C7%C1%C5%E6&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-10-28&stDateEnd=2021-11-11', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%C5%A9%B7%A1%C7%C1%C5%E6&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-07-28&stDateEnd=2021-08-11', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%C5%A9%B7%A1%C7%C1%C5%E6&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-10-19&stDateEnd=2022-11-02', 
 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%DD%B8%B6%BA%ED&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-12-15&stDateEnd=2022-12-29', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%DD%B8%B6%BA%ED&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-04-29&stDateEnd=2022-05-13', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%DD%B8%B6%BA%ED&x=0&y=0&sm=all.basic&pd=4&stDateStart=2020-08-20&stDateEnd=2020-09-03', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%DD%B8%B6%BA%ED&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-01-06&stDateEnd=2022-01-20', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%DD%B8%B6%BA%ED&x=0&y=0&sm=all.basic&pd=4&stDateStart=2020-10-01&stDateEnd=2020-10-15', 
 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%D8%BD%BC&x=0&y=0&sm=all.basic&pd=4&stDateStart=2020-12-22&stDateEnd=2021-01-05', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%D8%BD%BC&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-12-03&stDateEnd=2021-12-17', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%D8%BD%BC&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-02-17&stDateEnd=2022-03-03', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%D8%BD%BC&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-03-11&stDateEnd=2022-03-25', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B3%D8%BD%BC&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-10-20&stDateEnd=2021-11-03', 
 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B5%A5%BA%EA%BD%C3%BD%BA%C5%CD%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-01-18&stDateEnd=2021-02-01', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B5%A5%BA%EA%BD%C3%BD%BA%C5%CD%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-08-30&stDateEnd=2021-09-13', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B5%A5%BA%EA%BD%C3%BD%BA%C5%CD%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-01-11&stDateEnd=2021-01-25', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B5%A5%BA%EA%BD%C3%BD%BA%C5%CD%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-01-08&stDateEnd=2021-01-22', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%B5%A5%BA%EA%BD%C3%BD%BA%C5%CD%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2020-11-16&stDateEnd=2020-11-30', 

 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%C4%AB%C4%AB%BF%C0%B0%D4%C0%D3%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2020-08-28&stDateEnd=2020-09-11', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%C4%AB%C4%AB%BF%C0%B0%D4%C0%D3%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-06-18&stDateEnd=2021-07-02', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%C4%AB%C4%AB%BF%C0%B0%D4%C0%D3%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-12-23&stDateEnd=2022-01-06', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%C4%AB%C4%AB%BF%C0%B0%D4%C0%D3%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2022-07-20&stDateEnd=2022-08-03', 
 'https://finance.naver.com/news/news_search.naver?rcdate=&q=%C4%AB%C4%AB%BF%C0%B0%D4%C0%D3%C1%EE&x=0&y=0&sm=all.basic&pd=4&stDateStart=2021-07-08&stDateEnd=2021-07-22'
 ]



company_name_list = ['Krafton_top5_change', 'Netmarble_top5_change', 'Nexongames_top5_change', 'Devsisters_top5_change', 'Kakaogames_top5_change']


datas = {}

cnt = 0
for name in company_name_list :
    datas[name] = [] 
    for url in top5_urls :              
        datas[name].append(url)
        cnt += 1
        if cnt % 5 == 0 :
            break

datas = {}

for name in company_name_list:
    datas[name] = [] 
    for i, url in enumerate(top5_urls):
        datas[name].append(url)
        if i == 4: # Break after adding the first five elements
            break
datas

len(datas['Krafton_top5_change'])
len(datas['Kakaogames_top5_change'])



# 웹 크롤러 (뉴스 기사의 제목, 요약, 날짜를 저장)

import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_news(name, url):
    subjects = []
    summaries = []

    for page in range(1, 30):
        response = requests.get(f"{url}&page={page}")
        soup = BeautifulSoup(response.content, "html.parser")

        for subject, summary in zip(
            soup.find_all("dd", class_="articleSubject"),
            soup.find_all("dd", class_="articleSummary")
        ):
            # Remove special characters from subjects and summaries
            subject_str = subject.text.replace('\n', '').replace('\t', '').replace('\r', '').strip()
            subject_str = ''.join(c for c in subject_str if c.isalnum() or c.isspace())
            subjects.append(subject_str)

            summary_str = summary.text.replace('\n', '').replace('\t', '').replace('\r', '').strip()
            summary_str = ''.join(c for c in summary_str if c.isalnum() or c.isspace())
            summaries.append(summary_str)

    if len(subjects) == len(summaries):
        data = {"subjects": subjects, "summaries": summaries}
        df = pd.DataFrame(data, index=None)
        path = r"C:\ITWILL\3_TextMining"
        df.to_csv(path + f'\{name}_dataframe.csv', index=False)


for name, url in change_max_url.items():
    scrape_news(name, url)
    
for name, url in change_min_url.items():
    scrape_news(name, url)

'''
