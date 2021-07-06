import requests
import json

class Weather_Report(object):
	def __init__(self):
		self.url = 'http://apis.data.go.kr/1360000/WthrWrnInfoService/'
		self.api_local = {}
		self.api_data = {}
		with open(r"C:\Users\user\Desktop\MyProgram\MyProgram\WeatherReport\weather_report_api_key.txt", "r", encoding='utf-8') as file, open("weather_report_local_num.txt", "r", encoding='utf-8') as file2:
			self.api_data['serviceKey']=file.readline()
			for data in file2.readlines():
				self.api_local[data.strip('\n').split('\t')[1]] = data.strip('\n').split('\t')[0]
			
	def getWthrinfo(self, numOfRows, pageNo, local_name):   # 기상정보문출력
		if local_name in ["전국","서울", "부산", "대구", "광주", "전주", "대전", "청주", "강릉", "제주"]:
			self.api_data['numOfRows'] = numOfRows
			self.api_data['pageNo'] = pageNo
			query = f'?serviceKey={self.api_data["serviceKey"]}&numOfRows={self.api_data["numOfRows"]}&pageNo={self.api_data["pageNo"]}&dataType=JSON&stnId={self.api_local[local_name]}'
			res = requests.get(self.url + 'getWthrInfo' + query)
			text = res.text
			jsonObject = json.loads(text)
			content = jsonObject.get("response").get("body").get("items").get("item")
			result = content[0].get("t1").rstrip('\\n\n')
			return result
		else:
			raise AttributeError
	
wp = Weather_Report()
numOfRows, pageNo, local_name = input("write Rows, pageNo, local_name >>> ").split(" ")
text = wp.getWthrinfo(numOfRows, pageNo, local_name)
print(text)


