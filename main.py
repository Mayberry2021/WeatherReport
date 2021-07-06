import requests

class Weather_Report(object):
	def __init__(self):
		self.url = 'http://apis.data.go.kr/1360000/WthrWrnInfoService/'
		self.api_local = {}
		self.api_data = {}
		with open("weather_report_api_key.txt", "r", encoding='utf-8') as file, open("weather_report_local_num.txt", "r", encoding='utf-8') as file2:
			self.api_data['serviceKey']=file.readline()
			for data in file2.readlines():
				self.api_local[data.strip('\n').split('\t')[1]] = data.strip('\n').split('\t')[0]
			
	def getWthrinfo(self, numOfRows, pageNo, local_name):   # 기상정보문출력
		if local_name in ["전국","서울", "부산", "대구", "광주", "전주", "대전", "청주", "강릉", "제주"]:
			self.api_data['numOfRows'] = numOfRows
			self.api_data['pageNo'] = pageNo
			query = f'?serviceKey={self.api_data["serviceKey"]}&numOfRows={self.api_data["numOfRows"]}&pageNo={self.api_data["pageNo"]}&stnId={self.api_local[local_name]}'
			res = requests.get(self.url + 'getWthrInfo' + query)
			text = res.text
			return text
		else:
			raise AttributeError
	
wp = Weather_Report()
numOfRows, pageNo, local_name = input("write Rows, pageNo, local_name >>> ").split(" ")
text = wp.getWthrinfo(numOfRows, pageNo, local_name)

print(text)


'''
result = list(map(int,(input("한 페이지 결과 수와 페이지 번호를 입력하시오 >>> ")).split(' ')))

serviceKey='KcPvvyVEaqORzpTkpeX8%2Bk36SeU1KPEAdUK7gVD%2BKt6hYBONhpq0ZQ8NcPEQR6O%2FuYEdi4c030PNJp5TL66XLw%3D%3D'
Rows=result[0]
pageNo=result[1]

data = {'serviceKey':'KcPvvyVEaqORzpTkpeX8%2Bk36SeU1KPEAdUK7gVD%2BKt6hYBONhpq0ZQ8NcPEQR6O%2FuYEdi4c030PNJp5TL66XLw%3D%3D',
		'Rows':result[0],
		'pageNo':result[1]}

url = 'http://apis.data.go.kr/1360000/WthrWrnInfoService/getWthrWrnList'
query = f'?serviceKey={data["serviceKey"]}&numOfRows={data["Rows"]}&pageNo={data["pageNo"]}'

res = requests.get(url+query)
print(res.status_code, '|' , res.text)
'''