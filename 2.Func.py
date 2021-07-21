def Palindrome(word):
    drow=word[::-1]
    if drow==word:
        print('Палиндром')
    else:
        print('Не палиндром')

word=input('Введите слово: ')
Palindrome(word)