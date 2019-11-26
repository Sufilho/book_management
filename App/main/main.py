from functions import *

def App():
    print('-'*50,'\nGERENCIADOR DE LIVROS')
    def Core():
        toggle_menu = input('Digite [1] para vizualizar o menu --> ')
        if toggle_menu == '1':
            menu()
        option = int(input('Digite qual operação você deseja fazer: '))
        option_check(option)
        if option == 1:
            register_book()
            Core()
        elif option == 2:
            code = input('Digite o código do livro que você deseja alterar o cadastro: ')
            change_book(code)
            time.sleep(0.5)
            Core()
        elif option == 3:
            code = input('Digite o código do livro que você deseja excluir o cadastro: ')
            remove_book(code)
            time.sleep(0.5)
            Core()
        elif option == 4:
            code = input('Digite o código do livro que você deseja encontrar o cadastro: ')
            find_book(code)
            time.sleep(0.5)
            Core()
        elif option == 5:
            list_books()
            time.sleep(0.5)
            Core()
        elif option == 6:
            cont = input('Você realmente deseja sair?[S]-Sim [N]-Não --> ')
            if cont.upper() == 'S':
                exit
            else:
                return Core()
    Core()
        
if __name__ == "__main__":
    App()
