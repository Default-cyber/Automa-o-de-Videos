import pyautogui as pg
import time
from tqdm import tqdm
import subprocess

res=0
hdmi = 0
print("""
#  _____                                        _              _      
# |  ___|__ _ __ _ __ __ _ _ __ ___   ___ _ __ | |_ __ _    __| | ___ 
# | |_ / _ \ '__| '__/ _` | '_ ` _ \ / _ \ '_ \| __/ _` |  / _` |/ _ \
# |  _|  __/ |  | | | (_| | | | | | |  __/ | | | || (_| | | (_| |  __/
# |_|  \___|_|  |_|  \__,_|_| |_| |_|\___|_| |_|\__\__,_|  \__,_|\___|
#     _         _                             /\/|                    
#    / \  _   _| |_ ___  _ __ ___   __ _  ___|/\/_  ___               
#   / _ \| | | | __/ _ \| '_ ` _ \ / _` |/ __/ _` |/ _ \              
#  / ___ \ |_| | || (_) | | | | | | (_| | (_| (_| | (_) |             
# /_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\___\__,_|\___/              
#                                         )_)           
""")

print("             escolha uma das Opções abaixo:")
print("                 1 - Fechamento de serviços pesados")
print("                 2 - Preparar vídeo para edição")
print("                 3 - Alterar Rota")
print("                 4 - Excluir Rota")
print("                 5 - Sair")

resp = int(input("Escolha: "));
if(resp == 1): #Fechamento de Serviços pesados
    pg.hotkey('win','r')
    pg.write('cmd')
    pg.press('enter')
    time.sleep(2)
    pg.write('tasklist')
    pg.press('enter')
    time .sleep(2)
    pg.write('taskkill /F /IM chrome.exe')
    pg.press('enter')
    time.sleep(2)
    pg.write('taskkill /F /IM WhatsApp.exe')
    pg.press('enter')
    time.sleep(2)
    pg.write('taskkill /F /IM EpicGamesLauncher.exe')
    pg.press('enter')
    time.sleep(2)
    pg.write('taskkill /F /IM EpicWebHelper.exe')
    pg.press('enter')
    time.sleep(2)
    pg.write('taskkill /F /IM steam.exe')
    pg.press('enter')
    time.sleep(2)
    pg.write('taskkill /F /IM pycharm64.exe')
    pg.press('enter')
    time.sleep(2)
    pg.write('taskkill /F /IM msedge.exe')
    pg.press('enter')
    time.sleep(2)
    pg.write('exit')
    pg.press('enter')

    # Função para simular o carregamento
    def tela_de_carregamento():
        print("Fechando as Janelas...")
        # A barra de progresso será exibida com 100 etapas
        for _ in tqdm(range(100), desc="Fechando", ncols=100):
            time.sleep(0.05)  # Simula o tempo de carregamento
    # Chama a função para mostrar a tela de carregamento
    tela_de_carregamento()

elif(resp == 2):#Preparar vídeo para edição
    print("Abrindo Janelas")

    def verificar_hdmi():
        # Executa o comando xrandr
        resultado = subprocess.run(["xrandr"], capture_output=True, text=True)

        if resultado.returncode == 0:
            dispositivos = resultado.stdout
            if "HDMI" in dispositivos:
                print("HDMI detectado!")
                hdmi = 1
            else:
                print("Nenhum HDMI detectado.")
                hdmi = 0
        else:
            print("Erro ao executar o comando.")
            hdmi = 0


    verificar_hdmi()

    pg.hotkey('win', 'r')
    pg.write('msedge.exe')
    pg.press('enter')
    time.sleep(2)
    pg.write('instagram.com')
    pg.press('enter')
    time.sleep(2)
    pg.hotkey('ctrl','t')
    pg.write('tiktok.com')
    pg.press('enter')
    pg.hotkey('ctrl', 't')
    pg.write('youtube.com')
    pg.press('enter')
    time.sleep(2)
    pg.hotkey('win')

    #Edição
#Se não houver nenhum alteração de vídeo (Padrão)
    eixox = 758
    eixoy = 385

    pg.write('capcut')
    pg.press('enter')
    time.sleep(2)
    pg.click(eixox, eixoy)


    # Função para simular o carregamento
    def tela_de_carregamento():
        print("Abrindo as Janelas...")
        # A barra de progresso será exibida com 100 etapas
        for _ in tqdm(range(100), desc="Abrindo", ncols=100):
            time.sleep(0.05)  # Simula o tempo de carregamento

    # Chama a função para mostrar a tela de carregamento
    tela_de_carregamento()

elif(resp == 3):
    print("alterar rota")
elif(resp == 4):
    print("excluir rota")
elif(resp == 5):
    print("sair")
