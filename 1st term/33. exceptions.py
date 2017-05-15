try:
    s = int(input())
    print (s)
except ValueError as error:
    print("Вводи как надо!")
    print(error)
    raise
except IndexError:
    print('AAAAAAAAA')
else:
    print('если безз ошибок')
finally:
    print('done')
'''В ходе выполнения программы удобно бывает отслеживать исключения, возникающие при выполнении,
    при этом можно указывать решение проблемы. Raise пробрасывает на предыдущий уровень стека вызовов, там может быть
    обработчик, если нет, выдает возникшую ошибку, как стандартное исключение.
     Все исключения - объекты Exception, который является подклассом BaseException которыйявляется подклассом object'''

def clean():
    try:
        mit()
    except:
        print('исправь')
        raise
def mit():
    try:
        n = int(input())
        print(n)
    except:
        print('net shvabri')
        raise
clean()

'''33. Исключения в Python. Генерирование и перехват исключений.'''