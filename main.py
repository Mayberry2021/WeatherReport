import requests
import json
import time

class Weather_Report(object):
	def __init__(self):
		self.url = 'http://apis.data.go.kr/1360000/WthrWrnInfoService/'
		self.api_local = {}
		self.api_data = {}
		with open(r"C:\Users\pllab\Desktop\MyProgram\MyProgram\WeatherReport\weather_report_api_key.txt", "r", encoding='utf-8') as file, open("weather_report_local_num.txt", "r", encoding='utf-8') as file2:
			self.api_data['serviceKey']=file.readline()
			for data in file2.readlines():
				self.api_local[data.strip('\n').split('\t')[1]] = data.strip('\n').split('\t')[0]
			
	def getWthrInfoList(self, local_name): # 기상정보목록출력
		if local_name in ["전국","서울", "부산", "대구", "광주", "전주", "대전", "청주", "강릉", "제주"]:			
			query = f'?serviceKey={self.api_data["serviceKey"]}&numOfRows=10&pageNo=1&dataType=JSON'
			res = requests.get(self.url + 'getWthrInfoList' + query)
			text = res.text
			jsonObject = json.loads(text)
			content = jsonObject.get("response").get("body").get("items").get("item")
			swap_local = {num:local for local, num in self.api_local.items()}
			checking_dict = {}
			for local_num in self.api_local.values():
				checking_dict[local_num] = 0
			for idx in range(0, 10):
				if (swap_local[content[idx].get('stnId')]):
					checking_dict[content[idx].get('stnId')] += 1
			if checking_dict[self.api_local[local_name]] == 0:
				text = f'{local_name} 지역에는 기상 정보가 없습니다!'
				return text
			else:
				text = f"{local_name} 지역에 {checking_dict[self.api_local[local_name]]}건의 기상정보문이 있습니다!"
				return text
					
	def getWthrInfo(self, local_name):   # 기상정보문출력
		if local_name in ["전국","서울", "부산", "대구", "광주", "전주", "대전", "청주", "강릉", "제주"]:
			idx = 1
			total = " "
			while True:
				query = f'?serviceKey={self.api_data["serviceKey"]}&numOfRows=10&pageNo={idx}&dataType=JSON&stnId={self.api_local[local_name]}'
				res = requests.get(self.url + 'getWthrInfo' + query)
				text = res.text
				jsonObject = json.loads(text)
				if jsonObject.get("response").get("header").get("resultMsg") == 'NO_DATA':
					return total
				else:
					content = jsonObject.get("response").get("body").get("items").get("item")
					result = content[0].get("t1").rstrip('\\n\n')
					total += result
					idx += 1

	def getWthrBrkNewsList(self, local_name):	# 기상속보목록조회
		if local_name in ["전국","서울", "부산", "대구", "광주", "전주", "대전", "청주", "강릉", "제주"]:			
			query = f'?serviceKey={self.api_data["serviceKey"]}&numOfRows=10&pageNo=1&dataType=JSON&stnId={self.api_local[local_name]}'
			res = requests.get(self.url + 'getWthrBrkNewsList' + query)
			text = res.text
			jsonObject = json.loads(text)
			if jsonObject.get("response").get("header").get('resultMsg') == 'NO_DATA':
				text = f'{local_name} 지역에 공지된 기상 속보가 없습니다.'
				return text
			content = jsonObject.get("response").get("body").get("items").get("item")
			if ( content[0].get("stnId") ):
				text = f'{local_name} 기상 속보가 존재합니다.'
				return text


	def getWthrBrkNews(self, local_name):
		if local_name in ["전국","서울", "부산", "대구", "광주", "전주", "대전", "청주", "강릉", "제주"]:
			idx = 1
			total = " "
			tm = time.localtime()
			fromTmFc = int(time.strftime('%Y%m%d', tm))
			toTmFc = int(time.strftime('%Y%m%d', tm))
			while True:
				query = f'?serviceKey={self.api_data["serviceKey"]}&numOfRows=10&pageNo={idx}&dataType=JSON&stnId={self.api_local[local_name]}&fromTmFc={fromTmFc}&toTmFc={toTmFc}'
				res = requests.get(self.url + 'getWthrBrkNews' + query)
				text = res.text
				jsonObject = json.loads(text)
				print(jsonObject)
				if ((idx == 1) and (jsonObject.get("response").get("header").get("resultMsg") == 'NO_DATA')):
					text = f'{local_name} 지역에 공지된 기상 속보문이 없습니다!'
					return text
				if jsonObject.g0et("response").get("header").get("resultMsg") == 'NO_DATA':
					return total
				else:
					content = jsonObject.get("response").get("body").get("items").get("item")
					result = content[0].get("t1").rstrip('\\n\n')
					total += result
					idx += 1		