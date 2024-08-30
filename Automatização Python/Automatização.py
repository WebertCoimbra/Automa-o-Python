#Importas as ferramentas necessárias
import pyautogui as pt
import pandas as pd
import time 
pt.PAUSE=0.5
#abrir o navegador
pt.press ("win")
pt.write ("edge")
pt.press ("enter")
pt.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pt.press ("enter")
#Fazer Login
pt.press ("tab")
pt.write ("weberteste@outlook.com")
pt.press ("tab")
pt.write ("senhateste123")
pt.press ("tab")
pt.press ("enter")
time.sleep (3)
 #pt.press ("tab")#
#importar base dados
tabela=pd.read_csv("produtos.csv")
print (tabela)
#cadastrar os produtos
for linha in tabela.index:
    pt.click (x=657, y=275)
    codigo=tabela.loc[linha,"codigo"]
    pt.write(str(codigo))
    pt.press ("tab")
    pt.write(str(tabela.loc[linha, "marca"]))
    pt.press ("tab")
    pt.write(str(tabela.loc[linha, "tipo"]))
    pt.press ("tab")
    pt.write(str(tabela.loc[linha, "categoria"]))
    pt.press ("tab")
    pt.write(str(tabela.loc[linha, "preco_unitario"]))
    pt.press ("tab")  
    pt.write(str(tabela.loc[linha, "custo"]))
    pt.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pt.write(str(tabela.loc[linha, "obs"]))
    pt.press ("tab")
    pt.press("enter")
    pt.press ("pgup")
        
