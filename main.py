#!/bin/python3
# main file to run everything
name = input("Enter your name\n")
print("Hello " + name + "\n")

print("Welcome to our game. You may select from several minigames. Your options are as follows")
print("1. Mad Libs")
gameselection = 1
while gameselection > 0 :
    gameselection = int (input ("Enter a number between 1 and 10\n"))