import random as rand
def art():
    art1 = """
__________
|^|     | |
| |_____| |
|  _____  |
| |     | |
| |_____| |
|_|_____|_|
    """
    art2 = """ 
 ____
|,--.|
||__||
|+  o| 
|,'o | 
`----'
    """
    art3 = """
.--.
|__| .-------.
|=.| |.-----.|
|--| ||     ||
|  | |'-----'|
|__|~')_____('
    """
    art4 = """
 .----------------.
|          _       |
|      _.-'|'-._   |
| .__.|    |    |  |
|     |_.-'|'-._|  |
| '--'|    |    |  |
| '--'|_.-'`'-._|  |
| '--'          `  |
'----------------'
    """
    art5 = """ 
b.
88b
888b.
88888b
888888b.
8888P"
P" `8.
    `8.  
     `8
    """
    art6 = """
 __i
|---|    
|[_]|    
|:::|    
|:::|    
`\   \   
  \_=_\ 
    """
    
    art7 = """
.-------------------.
/--"--.------.------/|
|Kodak|__Ll__| [==] ||
|     | .--. |  ""  ||
|     |( () )|      ||
|     | `--' |      |/
`-----'------'------' 
"""    
    art8 = '''
 __________
| ________ |
||12345678||
|""""""""""|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------"  
    '''
    art_liste = [art1, art2, art3, art4, art5, art6, art7, art8]
    print()
    num = rand.randint(0, (len(art_liste))-1)
    return(art_liste[num])
    
