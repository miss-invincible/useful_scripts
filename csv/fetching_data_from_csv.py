import csv
with open('practise.csv') as csvfile:
	spa = csv.reader(csvfile,delimiter='\n',quotechar='|')
	contents = ["Institution","team_name","login_id","password"]
	f = open("practise_icpc.txt",'w')
	info=""
	for row in spa:
		for item in row:
			#print(item)
			
			data = []
			for i in item.split(','):
				data.append(i)

			data_size = len(data)

			if data_size==4:
				info ="\n\n\n\n" +contents[0]+":	"+data[0]+"\n" + contents[1]+":	"+data[1]+"\n"+contents[2]+":	"+data[2]+"\n"+contents[3]+":	"+data[3]

			else:
				info ="\n\n\n\n" +contents[0]+":	"+data[0]+" "+data[1]+"\n"+ contents[1]+":	"+data[2]+"\n"+ contents[2]+":	"+data[3]+"\n"+contents[3]+":	"+data[4]


		f.write(info)

f.close()	
