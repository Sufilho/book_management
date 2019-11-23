import json


book1 = {
	'code':'101231',
	'name':'A lenda do arqueiro',
	'publisher':'Abril',
	'year':'2010',
	'price':'50',
	}
book2 = {
	'code':'101231',
	'name':'O nome do vento',
	'publisher':'Abril',
	'year':'2010',
	'price':'50',
}
book3 = {
	'code':'101231',
	'name':'Jogos Vorazes',
	'publisher':'Abril',
	'year':'2010',
	'price':'50',
}
list_of_books = [book1,book2]

def json_dumps(var):
	return json.dumps((var),indent=4)

# with open('data.json','a') as f:
# 	f.write(json_dumps(book1))
# 	f.write('\n')
# 	f.write(json_dumps(book2))
# 	f.write('\n')
# 	f.write(json_dumps(book3))
# 	f.write('\n')

with open('data.json','r') as r:
	read = r.read()

data = json.loads(read)

