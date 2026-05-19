import os
import string
import time
import hashlib

print(f"de:Darwin Cruz Lopes\n para:")


print(r"""
   ##       ##     ######   ######            #####     #####            #######  ######
  ###      ###     ##       ##                 ## ##   ##   ##            ##   #  # ## #
   ##       ##     #####    #####              ##  ##  ##   ##            ## #      ##
   ##       ##         ##       ##             ##  ##  ##   ##            ####      ##
   ##       ##         ##       ##             ##  ##  ##   ##            ## #      ##
   ##       ##     ##  ##   ##  ##             ## ##   ##   ##            ##   #    ##
 ######   ######    ####     ####             #####     #####            #######   ####
""")
time.sleep(2)
print("\nRecuperador de boot do Windows\n")
def identificador_disc_windows():

    windows_instalacoes = []

    # Percorre todas as letras de disco
    for letra in string.ascii_uppercase:
        drive = f"{letra}:\\"

        # Verifica se o disco existe
        if os.path.exists(drive):

            # Caminhos importantes do Windows
            system32 = os.path.join(drive, "Windows", "System32")
            explorer = os.path.join(drive, "Windows", "explorer.exe")

            # Verifica se parece uma instalação válida
            if os.path.exists(system32) and os.path.exists(explorer):
                windows_instalacoes.append(drive)
    #discos com windows encontrados
    disc_windows = []
    time.sleep(2)
    # Resultado
    if windows_instalacoes:
        print("\nWindows encontrado em:\n")
        time.sleep(1)

        for i, sistema in enumerate(windows_instalacoes, start=1):
            print(f"[{i}] {sistema}")
            disc_windows.append(sistema)
            time.sleep(1)

    else:
        print("Nenhuma instalação Windows encontrada.")
    if i > 1:
        escolha = input("\nDigite o número da instalação que deseja usar: ")
        try:
            escolhedor = escolha - 1
            caminho_escolhido = disc_windows[escolhedor]
            print(f"\nVocê escolheu: {caminho_escolhido}")
        except (ValueError, IndexError):
            print("\nOpção inválida. Usando a primeira instalação encontrada.")
            caminho_escolhido = disc_windows[0]
    else:
        caminho_escolhido = disc_windows[0]
        print(f"\nUsando a única instalação encontrada: {caminho_escolhido}")
        time.sleep(1.5)
    return caminho_escolhido
disc_windows = identificador_disc_windows()
import os

def recuperar_boot(disco_windows, particao_efi):

    # Garante barra no final
    if not disco_windows.endswith("\\"):
        disco_windows += "\\"

    if not particao_efi.endswith("\\"):
        particao_efi += "\\"

    # Monta comando universal
    comando = (
        f'bcdboot {disco_windows}Windows '
        f'/s {particao_efi} '
        f'/f ALL'
    )

    print("\nExecutando recuperação do boot...")
    print(f"\nComando: {comando}\n")

    resultado = os.system(comando)

    if resultado == 0:
        print("Boot recuperado com sucesso!")
    else:
        print("Erro ao recuperar boot.")

# Exemplo
recuperar_boot("C:\\", "S:\\")

        
   
