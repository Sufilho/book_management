from functions import *

def App():
    print('-'*50,'\nGERENCIADOR DE LIVROS')
    def Core():
        toggle_menu = input('Digite [1] para vizualizar o menu --> ')
        if toggle_menu == '1':
            menu()
        else:
            Core()
        option = input('Digite qual operação você deseja fazer: ')
        def option_check(option):
            if option not in ['1','2','3','4','5','6']:
                print('*'*30 +'\n[ERRO] - OPÇÃO INVÁLIDA!\nEscolha uma opção válida!\n'+'*'*30)
                time.sleep(0.5)
                Core()
        option_check(option)
        if option == '1':
            register_book()
            Core()
        elif option == '2':
            change_book()
            time.sleep(0.5)
            Core()
        elif option == '3':
            remove_book()
            time.sleep(0.5)
            Core()
        elif option == '4':
            find_book()
            time.sleep(0.5)
            Core()
        elif option == '5':
            list_books()
            time.sleep(0.5)
            Core()
        elif option == '6':
            cont = input('Você deseja sair?[S]-Sim [N]-Não --> ')
            if cont.upper() == 'S':
                exit
            else:
                Core()
    Core()
        
if __name__ == "__main__":
    App()
