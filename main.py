from addpersonagem import adicionando_perso
from salvarpersonagem import salvando_perso
from verpersonagens import mostrar_perso
personagem_geral = {}
def main():
   while True: 
    print(' 1 - adicionar personagem\n 2 - ver todos os personagens\n 3 - SAIR\n')
    opcao = str(input('qual a opção : '))
    if opcao == '1':
       global personagem_geral
       personagem_geral = adicionando_perso()
       salvando_perso(personagem_geral)
    elif opcao == '2':
       mostrar_perso()
    elif opcao == '3':
        print('até mais')
        break
    else:
       print('invalido!')

main()