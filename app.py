import re
writelog = open('data.txt','w',encoding="utf-8")
with open('[LINE]LINE BK Alerts.txt','r',encoding="utf-8") as f:
	lines = f.readlines()
	amount = 5518
	for line in lines:
		cleanLine = line.replace("\n","").replace(",","")
		try:
			txt = re.search(r"(\d\d:\d\d) .+ (Deposit) ฿(\d+.\d{2})",cleanLine)
			amount += float(txt.group(3))
			print(f'{dt} {txt.group(1)}:00,D,+{txt.group(3)},{amount}')
			writelog.write(f'{dt} {txt.group(1)}:00,D,+{txt.group(3)},{amount}\n')
			continue
		except Exception as e:
			pass
		try:
			txt = re.search(r"(\d\d:\d\d) .+ (Withdraw\/Transfer) ฿(\d+.\d{2})",cleanLine)
			amount -= float(txt.group(3))
			print(f'{dt} {txt.group(1)}:00,W,-{txt.group(3)},{amount}')
			writelog.write(f'{dt} {txt.group(1)}:00,W,-{txt.group(3)},{amount}\n')
			continue
		except Exception as e:
			pass
		try:
			txt = re.search(r"(20\d\d).([01]\d).([0-3]\d) (.+)",cleanLine)
			dt = f'{txt.group(4)[:3]},{int(txt.group(2))}/{int(txt.group(3))}/{txt.group(1)}'
			continue
		except Exception as e:
			pass
	f.close()
writelog.close()