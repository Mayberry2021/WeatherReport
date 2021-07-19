	def getWthrBrkNewsList(self, local_name):	# 기상속보목록조회
		elif local_name == False:	# 지역이름 미입력시
			query = f'?serviceKey={self.api_data["serviceKey"]}&numOfRows=10&pageNo=1&dataType=JSON'
			res = requests.get(self.url + 'getWthrBrkNewsList' + query)
			text = res.text
			jsonObject = json.loads(text)
			if jsonObject.get("response").get("header").get('resultMsg') == 'NO_DATA':
				print('기상 속보 목록이 없습니다.')
				return False
			content = jsonObject.get("response").get("body").get("items").get("item")
			swap_local = {num:local for local, num in self.api_local.items()}
			checking_dict = {}
			for local_num in self.api_local.values():
				checking_dict[local_num] = 0
			for idx in range(0, 10):
				if (swap_local[content[idx].get('stnId')]):
					checking_dict[content[idx].get('stnId')] += 1
			for local_num, count in checking_dict.items():
				if count != 0:
					print(f'{swap_local[local_num]} : {count}건')

	def getWthrInfoList(self, local_name): # 기상정보목록출력
		elif local_name == "전부":	
			query = f'?serviceKey={self.api_data["serviceKey"]}&numOfRows=11&pageNo=1&dataType=JSON'
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
			for local_num, count in checking_dict.items():
				if count != 0:
					print(f'{swap_local[local_num]} : {count}건')