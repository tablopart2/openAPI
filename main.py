
import requests

url = 'http://apis.data.go.kr/1160100/service/GetDeriBusiInfoService/getDeriBusiTrusExclTota'
# params ={'serviceKey' : 'aX1/0K5vrAPPZYc+mlG8Obaj/GWEYhST44hEm+XcworI7H02Jz1E2sYx1/F2g4zbWsoaO8Dr911xvY1mq70Uqg==', 'numOfRows' : '10000', 'pageNo' : '1', 'resultType' : 'xml', 'title' : '파생상품_총괄(신탁제외)_파생상품거래규모', 'basYm' : '202003' }
params ={'serviceKey' : 'aX1/0K5vrAPPZYc+mlG8Obaj/GWEYhST44hEm+XcworI7H02Jz1E2sYx1/F2g4zbWsoaO8Dr911xvY1mq70Uqg==', 'numOfRows' : '10000', 'pageNo' : '1', 'resultType' : 'xml', 'basYm' : '202003' }

response = requests.get(url, params=params)
xml_data = response.text
with open("data_total.xml","w",encoding="utf-8") as file:
    file.write(xml_data)


url = 'http://apis.data.go.kr/1160100/service/GetDeriBusiInfoService/getDeriBusiTrusBusi'
params ={'serviceKey' : 'aX1/0K5vrAPPZYc+mlG8Obaj/GWEYhST44hEm+XcworI7H02Jz1E2sYx1/F2g4zbWsoaO8Dr911xvY1mq70Uqg==', 'numOfRows' : '10000', 'pageNo' : '1', 'resultType' : 'xml', 'title' : '파생상품_신탁_파생거래규모', 'basYm' : '202003' }

response = requests.get(url, params=params)
xml_data = response.text
with open("data_shintak.xml","w",encoding="utf-8") as file:
    file.write(xml_data)

print(response.content)