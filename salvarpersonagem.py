import json
import time
def salvando_perso(personagem_geral):
    arquivoPersonagem = open('personagem.txt' , 'w')
    arquivoPersonagem.write(json.dumps(personagem_geral) + '\n')
    arquivoPersonagem.close()
    print('salvando...')
    time.sleep(2)