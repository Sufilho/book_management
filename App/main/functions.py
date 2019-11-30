import sqlite3
import time
from main import *
from prettytable import PrettyTable

div = '-'*50

conn = sqlite3.connect('data.db')
c = conn.cursor()

# cadastrar item
def register_book():
    print(div,'\nCADASTRO DE LIVROS\n',div)
    code = input('\nCódigo do livro: ')
    name = input('Nome do livro: ')
    publisher = input('Nome da editora: ')
    year = int(input('Ano de publicação: '))
    price = float(input('Preço do livro: '))
        
    with conn:
        c.execute("INSERT INTO book VALUES (:code, :name, :publisher, :year, :price)", {'code':code,'name':name,'publisher':publisher,'year':year,'price':price})
    print('Livro cadastrado!')

# alterar item
def change_book(code_inp):
    print('Insira os novos dados:\n')  
    new_code = input('Código do livro: ')
    new_name = input('Nome do livro: ')
    new_publisher = input('Nome da editora: ')
    new_year = int(input('Ano de pubilação: '))
    new_price = float(input('Preço do livro: '))
        
    with conn:
        c.execute("""UPDATE book SET code = :newcode, name = :name, publisher= :publisher, year = :year, price = :price 
        WHERE code = :code""", {'code':code_inp,'newcode':new_code,'name':new_name,'publisher':new_publisher,'year':new_year,'price':new_price})
    print('Cadastro alterado!')
# deletar item
def remove_book(code_inp):
    with conn:
        c.execute("DELETE from book WHERE code = :code", {'code':code_inp})
    print('Livro removido!')

# localizar item
def find_book(code_inp):
    with conn:
        c.execute("SELECT * FROM book WHERE code = :code",{'code':code_inp})
        data = c.fetchall()
        data_book = data[0]
        data_list = []
        for eachData in data_book:
            data_list.append(eachData)

        table = PrettyTable()
        table.field_names = ['Código','Nome','Editora','Ano','Preço']
        table.add_row(data_list)
        print(table)

# listar item
def list_books():
    with conn:
        x = PrettyTable(['Código','Nome','Editora','Ano','Preço'])
        c.execute("SELECT * FROM book")
        data = c.fetchall()
        # print(data)
        for n in range(len(data)):
            x.add_row(data[n])
        tot = 0
        for book in data:
            tot += book[4]
        tot_frmtd = '{:.2f}'.format(tot)
        x.add_row(['-'*10,'-'*10,'-'*10,'-'*10,'-'*10])
        x.add_row(["Nº de livros = " + str(len(data)),'','','','Preço Total = ' + tot_frmtd])
        print(x.get_string(title='LISTA DE LIVROS'))

def menu():
    print(div,'\nOpções:\n[1] - CADASTRAR LIVRO \n[2] - ALTERAR CADSTRO DE LIVRO \n[3] - EXCLUIR CADASTRO DE LIVRO PELO CÓDIGO \n[4] - LOCALIZAR LIVRO PELO CÓDIGO \n[5] - LISTAR ITENS\n[6] - SAIR')

