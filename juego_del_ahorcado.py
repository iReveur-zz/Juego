from ast import Index
import random
from typing import SupportsIndex
from unidecode import unidecode
import os
from pathlib import Path

def read():

    here = Path(__file__).parent
    fname = here/'data.txt'
    with fname.open(mode="r", encoding="utf-8") as f:

    #with open("./archivos/data.txt", "r", encoding="utf-8") as f:

        words = [i for i in f]

        global random_word
        random_word = random.choice(words).strip()
        random_word = unidecode(random_word)
    

def ciclo():

    global S_SPACE

    S_SPACE = "_ "*len(random_word)
    print(S_SPACE) #, "(" + random_word + ")")
    
    while "_" in S_SPACE:       
            
        ipt = input("Ingrese una letra: ").lower()
        os.system("clear") 
        
        matt = {idx: value for idx, value in enumerate(random_word) if value ==ipt}
        
        idx = [idx*2 for idx in matt]
        #print(idx)
        
        if ipt in random_word and ipt != "":
       
            ipt = ipt.upper()

            for i in idx:
                os.system("clear")
                S_SPACE = S_SPACE[:i] + ipt + S_SPACE[i+1:]        
                skin4()
                print(S_SPACE)  
            
        else:
            os.system("clear")
            skin3()
            print(S_SPACE)
            
    os.system("clear")
    skin2()


def skin():

        
    print(""" Sálvate si puedes
         ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''./
        | |/         |/  _  \/
        | |          ||  `/,|           ¡Bienvenido mortal! 
        | |          (\.`_.'            Te propongo un reto,
        | |         .-`--'.             descubre la palabra.
        | |        /Y . . Y\.           ¿Te atreves?
        | |       // |   | \..
        | |      //  | . |  \..
        | |     ()   |   |   ()
        | |          ||'||
        | |          || ||
        | |          || ||
        | |          || ||
        | |         / | | \.
-------------------------
|  -------------------- |
| |                   | |
: :                   : :  
-------------------------

""")
                          

def skin2():
    
    print(f""" Sálvate si puedes
         ___________.._______
        | .__________))______|
        | | / /      
        | |/ /       
        | | /         .-''./
        | |/         |/  _  \/          La palabra era "{S_SPACE.replace(" ","")}"
        | |          ||  `/,|           Ten mucho cuidado mortal 
        | |          (\.`_.'            solo por esta vez te dejaré ir,
        | |         .-`--'.             pero recuerda, los laureles del infierno te esperan
        | |        /Y . . Y\.           nos vemos pronto...
        | |       // |   | \..
        | |      //  | . |  \..
        | |     ()   |   |   ()
        | |          ||'||
        | |          || ||
        | |          || ||
        | |          || ||
        | |         / | | \.            (Don't look back)
-------------------------
|  -------------------- |
| |                   | |
: :                   : :  
-------------------------

""")    
    
    
def skin3():

    print(""" Sálvate si puedes
         ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''./
        | |/         |/  _  \/
        | |          ||  `/,|           ¡Erraste mortal!
        | |          (\.`_.'            te daré otra oportunidad, 
        | |         .-`--'.             igual, solamente tu vida está en juego.
        | |        /Y . . Y\.           ¿No lo sabías?
        | |       // |   | \..          
        | |      //  | . |  \..         
        | |     ()   |   |   ()
        | |          ||'||
        | |          || ||
        | |          || ||
        | |          || ||
        | |         / | | \.
-------------------------
|  -------------------- |
| |                   | |
: :                   : :  
-------------------------

""")


def skin4():

    print(""" Sálvate si puedes
         ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''./
        | |/         |/  _  \/
        | |          ||  `/,|           Sigue así...
        | |          (\.`_.'            ya casi...
        | |         .-`--'.             
        | |        /Y . . Y\.           ¿O no?
        | |       // |   | \..
        | |      //  | . |  \..
        | |     ()   |   |   ()
        | |          ||'||
        | |          || ||
        | |          || ||
        | |          || ||
        | |         / | | \.
-------------------------
|  -------------------- |
| |                   | |
: :                   : :  
-------------------------

""")
    

def run():
    
    os.system("clear")
    skin()
    read()
    ciclo()
    

if __name__ == "__main__":
    run()
