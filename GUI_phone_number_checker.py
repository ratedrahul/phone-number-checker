from tkinter import *   
from functools import partial   
import phonenumbers  
from phonenumbers import timezone, carrier, geocoder
window = Tk()  
window.geometry('600x600')
window.title('Phone Number Checker by rinku junwal')
font = ('bold',22,'normal')
font1 = ('bold',17,'normal')
font2 = ('LED',7,'normal')
window.config(bg = '#AA0F2F')
L1 = Label(window,text = 'Mobile Number verification Application ',font = font1)
L1.pack(pady = 10)

E = Entry(window,font = font,justify = LEFT)
# E = Entry(window,font = font,justify = LEFT)
E.pack(pady = 10)

L1 = Label(window,text = 'Please Use Country Code as well, for india it is +91 and so on ',font = font2)
L1.pack()

# scFrame = Frame(window)

# f1 = Frame(window)
# # f1.pack(side= BOTTOM)
# f1.place(x = 200, y = 200)

def p():
	# f1.forget()
	# f1.pack_forget()
	# window.update()
	
	# f1 = Frame(window)
	# f1.pack(side= BOTTOM)
	try:
		mobile_number = E.get()
		mobile_number = phonenumbers.parse(mobile_number)
		tzone = str(timezone.time_zones_for_number(mobile_number))

		# print(carrier.name_for_number(mobile_number,'en'))
		op = carrier.name_for_number(mobile_number,'en')

		# print(geocoder.description_for_number(mobile_number,'en'))
		country = geocoder.description_for_number(mobile_number,'en')

		# print('Valid Mobile number : ',phonenumbers.is_valid_number(mobile_number))
		Valid_number = phonenumbers.is_valid_number(mobile_number)
		Valid_number = str(Valid_number)
		poss = phonenumbers.is_possible_number(mobile_number)
		poss = str(poss)
	except Exception:
		op = 'Invalid Entry'		
		country = '        '
		Valid_number = '      '
		poss = '         '
	# print('Phonemetada : ',phonenumbers.PhoneMetadata(mobile_number))

	# print('Checking Possibility of number ',phonenumbers.is_possible_number(mobile_number))
	# f4 = Label(f1,text ='Operator \n'+op+'\nCountry',font = font)
	# f4 = Label(f1,text ='Operator \n'+op+'\nCountry '+country+'\nValid Number '+Valid_number,font = font)
	# f4 = Label(window,text ='Operator : '+op+'\nCountry : '+country+'\nValid Number : '+Valid_number,font = font)
	f4 = Label(window,text ='Operator : '+op+'\nLocation : '+country+'\nValid Number : '+Valid_number+'\nPossible Number : '+poss+'\nTimezone: '+tzone,font = font)
	# f4.pack()
	f4.place(x =40, y = 280)
	# f4.pack()
	# f4 = Label(f1,text ='Operator '+carrier.name_for_number(mobile_number,'en'),font = font)
	# f4.place(x= 200, y = 200)
	# f4.clear()
	# f1.update()
	window.update()
	# f1.pack_forget()
	# f4.forget()
	# f1.forget()

B = Button(text = 'SEARCH',font = ('bold',12,'normal'),command = p)
B.pack(pady = 10)


# B = Button(command = e.get)
# x = Text()
# x.pack()