from G_sheet import Google_sheet
#make a public google sheet editor with anyone
url='https://docs.google.com/spreadsheets/d/10pA-PS4iclTpgX0bx3RLWUhNMRapDeGQms5KQQKVe1c/edit#gid=0'


x=Google_sheet()
#inputting
x.input_data(url=url,sheet_name='ss',position=[1,3],data=709999)

'''
#fetching data in a list of lists
xx=x.show_data(url=url,sheet_name='ss')
print(xx[3][2])
print(xx)
'''