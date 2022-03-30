from G_sheet import Google_sheet
#make a public google sheet editor with anyone
url='https://docs.google.com/spreadsheets/d/1N2yFPBUSNqcBqmQND9ejt2tRdOwEr0DEGPbzHDx9w1M/edit#gid=0'


x=Google_sheet(url=url,sheet_name='ss')
#inputting
x.input_data(position=[1,1],data='12121231443')


#fetching data from a cell
print(x.show_data(pos=[1,1]))

