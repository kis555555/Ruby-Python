#!C:\Users\JW\AppData\Local\Programs\Python\Python38-32\python.exe
#-*- Encoding: utf-8 -*-
#print("content-type: text/html; charset=utf-8\n")
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

in_str = input("입력해주세요.")
print(in_str.upper())