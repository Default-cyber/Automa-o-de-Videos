import pyautogui as pg
import time
from tqdm import tqdm
import subprocess
import random

res = 0
hdmi = 0


def print_header():
    print("""
    #  _____                                        _              _      
    # |  ___|__ _ __ _ __ __ _ _ __ ___   ___ _ __ | |_ __ _    __| | ___ 
    # | |_ / _ \ '__| '__/ _` | '_ ` _ \ / _ \ '_ \| __/ _` |  / _` |/ _ \\
    # |  _|  __/ |  | | | (_| | | | | | |  __/ | | | || (_| | | (_| |  __/
    # |_|  \___|_|  |_|  \__,_|_| |_| |_|\___|_| |_|\__\__,_|  \__,_|\___|   
    #                                         )_)           
    """)
    print("             Escolha uma das opções abaixo:")
    print("                 1 - Fechamento de serviços pesados")
    print("                 2 - Preparar vídeo para edição (manutenção eixox e eixoy)")
    print("                 3 - Iniciar postagens de vídeo")
    print("                 4 - Excluir rota")
    print("                 5 - Sair")


def fechar_programas():
    programas = [
        'chrome.exe', 'WhatsApp.exe', 'EpicGamesLauncher.exe', 'EpicWebHelper.exe',
        'steam.exe', 'pycharm64.exe', 'msedge.exe'
    ]
    for prog in programas:
        pg.hotkey('win', 'r')
        pg.write('taskkill /F /IM ' + prog)
        pg.press('enter')
        time.sleep(2)


def tela_de_carregamento(acao):
    print(f"{acao}...")
    for _ in tqdm(range(100), desc=acao, ncols=100):
        time.sleep(0.05)


def verificar_hdmi():
    global hdmi
    resultado = subprocess.run("wmic path Win32_VideoController get Caption", capture_output=True, text=True,
                               shell=True)
    if resultado.returncode == 0:
        if "HDMI" in resultado.stdout:
            print("HDMI detectado!")
            hdmi = 1
        else:
            print("Nenhum HDMI detectado.")
            hdmi = 0
    else:
        print("Erro ao executar o comando.")
        hdmi = 0


def preparar_ambiente():
    pg.hotkey('win', 'r')
    pg.write('cmd')
    pg.press('enter')
    time.sleep(2)
    fechar_programas()
    pg.write('exit')
    pg.press('enter')
    print("Ambiente Preparado")


def abrir_janelas():
    pg.hotkey('win', 'r')
    pg.write('msedge.exe')
    pg.press('enter')
    time.sleep(2)
    pg.write('instagram.com')
    pg.press('enter')
    time.sleep(2)
    pg.hotkey('ctrl', 't')
    pg.write('tiktok.com')
    pg.press('enter')
    pg.hotkey('ctrl', 't')
    pg.write('youtube.com')
    pg.press('enter')
    time.sleep(2)


def abrir_capcut():
    pg.hotkey('win')
    time.sleep(2)
    pg.write('capcut')
    time.sleep(2)
    pg.press('enter')
    pg.click(262, 1049)  # Acessar capcut
    time.sleep(2)
    pg.click(1000, 1000)  # coordenada que varia dependendo do HDMI
    time.sleep(2)
    pg.click(724, 389)
    time.sleep(2)
    pg.click(690, 442)
    time.sleep(2)
    pg.click(917, 685)
    time.sleep(2)
    pg.click(97, 331)
    time.sleep(2)
    pg.click(444, 230)
    pg.click(444, 230)
    time.sleep(2)
    pg.click(1237, 1015)
    pg.click(1237, 1015)
    time.sleep(2)
    tela_de_carregamento("Abrindo as Janelas")


def iniciar_postagens_hdmi():
    if hdmi == 1:
        pg.click(-1027, 340)
        time.sleep(2)
        pg.click(-1069, 515)
        time.sleep(2)
        pg.click(-2331, 295)
        time.sleep(2)
        pg.click(-1740, 68)
        time.sleep(2)
        pg.write("C:\\Users\\nicol\\AppData\\Local\\CapCut\\Videos")
        pg.press('enter')

        x1, y1 = -2180, 193
        x2, y2 = -76, 193
        x3, y3 = -2182, 1031
        x4, y4 = -107, 1031
        min_x = min(x1, x2, x3, x4)
        max_x = max(x1, x2, x3, x4)
        min_y = min(y1, y2, y3, y4)
        max_y = max(y1, y2, y3, y4)

        for _ in range(2):  # Faz 2 cliques aleatórios
            random_x = random.randint(min_x, max_x)
            random_y = random.randint(min_y, max_y)
            pg.moveTo(random_x, random_y, duration=1)
            pg.click()
            time.sleep(1)
        pg.click(-2127, 241)
        pg.click(-2127, 241)


def iniciar_postagens_sem_hdmi():
    pg.click(1137, 210)


def menu_principal():
    print_header()
    resp = int(input("Escolha: "))

    if resp == 1:  # Fechamento de Serviços pesados
        fechar_programas()
        tela_de_carregamento("Fechando as Janelas")

    elif resp == 2:  # Preparar vídeo para edição
        preparar_ambiente()
        abrir_janelas()
        verificar_hdmi()
        abrir_capcut()

    elif resp == 3:  # Iniciar Postagens de vídeo
        preparar_ambiente()
        iniciar_postagens_hdmi() if hdmi == 1 else iniciar_postagens_sem_hdmi()

    elif resp == 4:
        print("Excluir rota")

    elif resp == 5:
        print("Sair")


if __name__ == "__main__":
    menu_principal()
