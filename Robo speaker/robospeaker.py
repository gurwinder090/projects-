import win32com.client

speaker = win32com.client.Dispatch("SAPI.Spvoice")

A = "Welcome to robo speaker by Gurwinder singh"
speaker.speak(A)
while True:
    X = print("enter what you want me to speak: ")

    s = input()
    speaker.speak(s)


###Exit code is pending in this program





