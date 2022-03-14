import tkinter as tk
import requests

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

apiURLAdd_1 = '&seq='
apiURLAdd_2 = '&lang=en-US'

m=0; s=0
seqVal = 0

stop_flag=False
sendBool = False
newClock = True

reset_txt=f"00:00"

def sendUpdate(seqCounter, apiKeyValue):
    url = apiKeyValue+apiURLAdd_1+str(seqCounter)+apiURLAdd_2
    headers = {'Content-type': 'text/plain'}
    x = requests.post(url, headers=headers, data = 'Elapsed Time: ' + clock_lbl['text'] + '\n') 
    if 200 <= x.status_code <= 299:
        return True
    else:
        return False

def getLastSeq():
    global seqVal
    apiKeyValue = apiKey.get()
    if apiKeyValue.startswith('http'):
        index = apiKeyValue.find('?')
        url = apiKeyValue[:index] + '/seq' + apiKeyValue[index:]
        x = requests.get(url)
        if 200 <= x.status_code <=299:
            check_btn['text'] = 'Success'
            check_btn['bg'] = 'green'
            check_btn['fg'] = 'white'
            seqVal = int(x.text)
        else:
            check_btn['text'] = 'Fail'
            check_btn['bg'] = 'red'
            check_btn['fg'] = 'white'
    else:
        check_btn['text'] = 'Fail'
        check_btn['bg'] = 'red'
        check_btn['fg'] = 'white'


def clock_run():
    global m, s, sendBool, seqVal, apiKeyValue
    if not stop_flag:
        s+=1
        if s ==30:
            sendBool = True
        elif s == 60:
            m+=1; s=0
            sendBool = True

        clock_lbl['text']=f"{m:02}:{s:02}"

        if sendBool:
            seqVal += 1
            if not sendUpdate(seqVal, apiKeyValue):
                getLastSeq()
                seqVal += 1
                if not sendUpdate(seqVal, apiKeyValue):
                    print('Failed to Send Update')
                sendBool = False
            else:
                sendBool = False
    canvas1.after(1000, clock_run)

def  Start():
    global stop_flag, apiKeyValue, newClock
    apiKeyValue = apiKey.get()
    stop_flag=False
    if newClock:
        clock_run()
        newClock = False

def Stop():
    global stop_flag
    stop_flag=True 


def reset1(event=None):
    global s, m, stop_flag, newClock
    s=0; m=0
    clock_lbl['text']=reset_txt
    stop_flag=True
    newClock = True


apiLabel = tk.Label(root, text= 'API Key')
canvas1.create_window(200, 20, window=apiLabel)
apiKey = tk.Entry(root)
canvas1.create_window(200, 50, window=apiKey)
check_btn = tk.Button(master=canvas1, text="Check API Key", width=20, command=getLastSeq)
canvas1.create_window(200, 80, window=check_btn)


clock_lbl = tk.Label(master=canvas1, height=2, width=10,text=reset_txt,font=(None, 20))
canvas1.create_window(200, 150, window=clock_lbl)

start_btn = tk.Button(master=canvas1, text="START", width=10, command=Start, bg='green', fg='white')
canvas1.create_window(75, 200, window=start_btn)
stop_btn = tk.Button(master=canvas1, text="STOP", width=10, command=Stop, bg='red', fg='white')
canvas1.create_window(200, 200, window=stop_btn)
reset_btn = tk.Button(master=canvas1, text="RESET",width=10,command = reset1, bg='yellow')
canvas1.create_window(325, 200, window=reset_btn)

root.mainloop()
