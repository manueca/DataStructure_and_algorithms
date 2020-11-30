lines = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20","10.0.0.2 - GET 2020-08-20"]
def findRepeatingIP(lines:list):
	dict_ip={}
	for i in lines:
		ip=i.split('-')[0].rstrip()
		dict_ip[ip]=dict_ip.get(ip,0)+1
	max_value = max(dict_ip.values())
	max_keys=sorted([k for k,v in dict_ip.items() if v==max_value])
	return max_keys
