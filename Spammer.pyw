while True:
    import subprocess

    try:
        import time
        import pyautogui
        import tkinter as tk
        import random as rd
        import easygui

        b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        def Ja():
            global a
            a = 1
            enter.configure(text="Ja")

        def Nein():
            global a
            a = 2
            enter.configure(text="Nein")

        def beginn():
            global a
            global b
            te = textEingabe.get()
            zh = int(zahlEingabe.get())

            tete = te.lower()

            kp = easygui.msgbox(f'Bitte klicke bervor du den Spammer startest in die Zeile wo du {zh}mal "{te}" eingeben möchtest! Sobald du auf die Zeile geklickt hast und das Programm starten möchtest klicke bitte unten auf den Knopf "STARTEN".','Zuerst in die Zeile klicken!', 'STARTEN')

            if kp == "STARTEN":

                if tete == "alphabet-klein-getrennt" or tete == "a-k-g":
                    b = b.lower()
                    if a == 1:
                        for i in b:
                            pyautogui.write(i)
                            pyautogui.press("enter")
                    elif a == 2:
                        for i in b:
                            pyautogui.write(i)

                elif tete == "alphabet-groß-getrennt" or tete == "a-g-g":
                    if a == 1:
                        for i in b:
                            pyautogui.write(i)
                            pyautogui.press("enter")
                    elif a == 2:
                        for i in b:
                            pyautogui.write(i)

                elif tete == "alphabet-klein-zusammen" or tete == "a-k-z":
                    b = b.lower()
                    if a == 1:
                        for i in range(zh):
                            pyautogui.write(b)
                            pyautogui.press("enter")
                    elif a == 2:
                        for i in range(zh):
                            pyautogui.write(b)

                elif tete == "alphabet-groß-zusammen" or tete == "a-g-z":
                    if a == 1:
                        for i in range(zh):
                            pyautogui.write(b)
                            pyautogui.press("enter")
                    elif a == 2:
                        for i in range(zh):
                            pyautogui.write(b)

                else:
                    te = te.replace("ß", "ss")
                    if a == 1:
                        for i in range(zh):
                            pyautogui.write(te)
                            pyautogui.press("enter")
                    elif a == 2:
                        for i in range(zh):
                            pyautogui.write(te)

        root = tk.Tk()
        root.geometry("500x100")
        root.title("Spammer")
        root.resizable(width=False, height=False)

        text = tk.Label(root, text="Gib hier den Text ein den du senden möchtest", anchor="w")
        textEingabe = tk.Entry(root)
        text.grid(row=0, column=0)
        textEingabe.grid(row=0, column=1)

        zahl = tk.Label(root, text="Gib hier die Zahl ein wie oft du den Text senden möchtest", anchor="w")
        zahlEingabe = tk.Entry(root)
        zahl.grid(row=1, column=0)
        zahlEingabe.grid(row=1, column=1)

        enter = tk.Label(root, text="Möchtest du dass immer am Ende enter gedrückt wird?", anchor="w")
        enterButtonJa = tk.Button(root, text="Ja", command=Ja)
        enterButtonNein = tk.Button(root, text="Nein", command=Nein)
        enter.grid(row=2, column=0)
        enterButtonJa.grid(row=2, column=1)
        enterButtonNein.grid(row=2, column=2)

        Go = tk.Button(root, text="Los", command=beginn)
        Go.grid(row=3, column=0)

        root.mainloop()
        break
    except ImportError:
        subprocess.call("pip install pyautogui", shell=True)
        subprocess.call("pip install easygui", shell=True)