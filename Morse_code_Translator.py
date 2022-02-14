import tkinter as tk
root = tk.Tk()
root.title("Morse Code Translator")
root.geometry("300x200")
message = tk.StringVar()

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def encrypt(string):
    cipher = ''
    for letter in string:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher
def decrypt(string):
    string += ' '
    decipher = ''
    citext = ''
    for letter in string:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher
def Translate_encode():
    mesg= message.get()
    mesencode = encrypt(mesg.upper())
    print("Your encrypted cipher "+mesencode)
    message.set("")

def Translate_decode():
    mesg = message.get()
    mesencode = decrypt(mesg.upper())
    print("Your Decrypted cipher " +mesencode)
    message.set("")

message_label = tk.Label(root,text = 'Enter message', font=('calibre',10,'bold'))
message_entry = tk.Entry(root,textvariable = message,font=('calibre',10,'normal'))
encode = tk.Button(root, text="Encode",command = Translate_encode)
decode = tk.Button(root, text="Decode",command = Translate_decode)
message_label.grid(row=0,column=0)
message_entry.grid(row=0,column = 1)
encode.grid(row=2,column=1)
decode.grid(row=2,column=2)
root.mainloop()
