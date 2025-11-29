from main.constructor.introduction_process import introduction_process
from main.constructor.people_finder_constructor import people_finder_constructor
from main.constructor.people_register_constructor import people_register_constructor

def start():
    while True:
        command = introduction_process()
        match command:
            case '1': 
                people_register_constructor()
            case '2': 
                people_finder_constructor()
            case '5': 
                exit()
            case _: 
                print('\n Comando nao encontrado!! \n\n')
