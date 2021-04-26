#!/usr/bin/python3
# -*- coding: utf-8 -*-
import crypt
from termcolor import colored


def testPass(cryptPass):  # Start the function
    salt = cryptPass[0:2]
    # Open the dictionary file
    dictFile = open('rockyou.txt', 'r')
    for word in dictFile.readlines():  # Scan through the file
        word = word.strip('\n')
        # Check for password in the file
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print(colored("[+] Found Password: " +
                          word + "\n", 'grey', 'on_green'))
            return

    print("[-] Password Not Found.\n")
    return


def main():
    passFile = open('victim.txt', 'r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ').strip('\n')
            print(colored('[*] Cracking Password For: ' +
                          user, 'white', "on_red"))
            testPass(cryptPass)


if __name__ == '__main__':
    main()
