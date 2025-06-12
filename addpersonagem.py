def adicionando_perso():
    nome_perso = str(input('digite o nome :'))
    classe_perso = str(input('digite a classe : '))
    idade_perso = str(input('digite a idade: '))
    habilidade_perso = str(input('digite a habilidade :'))
    personagem_geral = {'nome' : nome_perso ,
                        'classe' : classe_perso ,
                        'idade' : idade_perso ,
                        'habilidade' : habilidade_perso
                        }
    print('adicionado!')
    return personagem_geral
    
