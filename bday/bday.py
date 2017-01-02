import time
import os
bday_data = {"prabhat":"23/10", "me":"29/09","test":"3/1"}

def number_padding(digits_req,number_to_pad):
	min_val = 1
	init_val = 10

	result = str(number_to_pad)
	if number_to_pad>=min_val and number_to_pad<init_val:
		result = "0"+result
		number_to_pad = number_to_pad*10

	return result



def create_page(name):
	script = "<HTML>\
				<center>\
				<img src='bday.jpeg'>\
				</center>\
				<center><H1>"+name+"</H1></center>\
			</HTML>"

	f = open("bday.html",'w')
	f.write(script)
	f.close()
	

current_date = time.strftime("%d/%m")
#print current_date

for key, value in bday_data.iteritems():
	day,month = value.split("/")
	day = number_padding(2,int(day))
	month = number_padding(2,int(month))
	new_format = day+"/"+month
	
	if current_date == new_format:
		create_page(key)


os.system("open ./bday.html")


