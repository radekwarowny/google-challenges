#!/usr/bin/env python

""" Braille.py: Results to the Google Challenge. foobar.withgoogle.com"""

__author__ = "Radek Warowny"

"""
Braille Translation
===================

Because Commander Lambda is an equal-opportunity despot, they have several visually-impaired minions.
But Lambda never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station. 
You figure printing out Braille signs will help them, and -- since you'll be promoting efficiency at the same time -- increase your chances of a promotion. 
Braille is a writing system used to read by touch instead of by sight. 
Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). 
You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and "read" the text with their touch. 
The special printer which can print the bumps onto the signs expects the dots in the following order:

1 4
2 5
3 6

So given the plain text word "code", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00

where 1 represents a bump and 0 represents no bump.  Put together, "code" becomes the output string "100100101010100110100010".

Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.
"""


letters = {'a':'100000', 'b':'110000','c':'100100','d':'100110', 'e':'100010',
            'f':'110100','g':'110110','h':'110010','i':'010100', 'j':'010110','k':'101000','l':'111000','m':'101110',
            'n':'101110','o':'101010','p':'111100','q':'111110', 'r':'111010','s':'011100','t':'011110','u':'101001',
            'v':'111001','w':'010111','x':'101101','y':'101111', 'z':'101011', ' ':'000000'}

capital = '000001'


def solution(s):
    letters = {'a':'100000', 'b':'110000','c':'100100','d':'100110', 'e':'100010',
               'f':'110100','g':'110110','h':'110010','i':'010100', 'j':'010110',
               'k':'101000','l':'111000','m':'101100','n':'101110','o':'101010',
               'p':'111100','q':'111110', 'r':'111010','s':'011100','t':'011110',
               'u':'101001','v':'111001','w':'010111','x':'101101','y':'101111', 'z':'101011'}
    capital = '000001'
    space = '000000'
    translation = []

    for i in s:
        if i.isspace():
            translation.append(space)
        elif i.isupper() and (i.lower() in letters):
            translation.append(capital)
            translation.append(letters.get(i.lower()))
        elif i in letters:
            translation.append(letters.get(i))
        else:
            pass
    string = ''.join(translation)

    return string

print(solution("code"))
print(solution("Braille"))
print(solution("The quick brown fox jumpes over the lazy dog"))