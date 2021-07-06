with open("weather_report_local_num.txt", "r", encoding='utf-8') as file2:
	for data in file2.readlines():
		data2 = data.strip('\n').split('\t')
		print(data2)
		