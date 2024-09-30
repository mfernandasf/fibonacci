import time

lampada1 = {'ligada': False, 'quente': False}
lampada2 = {'ligada': False, 'quente': False}
lampada3 = {'ligada': False, 'quente': False}


def ligar_interruptor_1():
    print("Ligando Interruptor 1 e aguardando para aquecer a lâmpada...")
    lampada1['ligada'] = True
    time.sleep(2)  # Simula o tempo de espera para a lâmpada aquecer
    lampada1['quente'] = True
    print("Desligando Interruptor 1.")
    lampada1['ligada'] = False


def ligar_interruptor_2():
    print("Ligando Interruptor 2.")
    lampada2['ligada'] = True


def checar_lampadas():
    print("\nChecando as lâmpadas nas outras salas...")

    if lampada1['ligada']:
        print("Lâmpada 1 está acesa.")
    elif lampada1['quente']:
        print("Lâmpada 1 está apagada, mas está quente.")
    else:
        print("Lâmpada 1 está apagada e fria.")

    if lampada2['ligada']:
        print("Lâmpada 2 está acesa.")
    else:
        print("Lâmpada 2 está apagada e fria.")

    if lampada3['ligada']:
        print("Lâmpada 3 está acesa.")
    else:
        print("Lâmpada 3 está apagada e fria.")


def main():
    print("Situação inicial: todas as lâmpadas estão apagadas e frias.")

    ligar_interruptor_1()

    ligar_interruptor_2()

    checar_lampadas()


if __name__ == "__main__":
    main()
