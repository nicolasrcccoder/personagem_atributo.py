import json
def mostrar_perso():
   try:
     with open('personagem.txt' , 'r') as arquivoPersonagem:
       mostrar_dados = arquivoPersonagem.readlines() 
       if not mostrar_dados:
          print('não há nenhum personagem aqui!')
       else:
         print('-----ESTATISTICA DE PERSONAGEM-----')
         for linha in mostrar_dados:
           personagemfinal = json.loads(linha.strip())
           print(f'--- NOME : {personagemfinal["nome"]} ---')
           print(f'--- CLASSE : {personagemfinal["classe"]} ---')
           print(f'--- IDADE : {personagemfinal["idade"]} ---')
           print(f'--- HABILIDADE : {personagemfinal["habilidade"]} ---')
           print('--------------------------------')
   except FileNotFoundError:
      print('arquivo não encontrado!')