def frieze(n):
    print('\\ ' + ' /\\ ' * n + ' /')
    print(' \\' + '/..\\' * n + '/')
    print(' |'+'|  |' * n + '|')
    print('/' + '    ' * n + '  \\')



def numbers(filename):
    list_n = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                a = 0
                b = ''
                c = 0
                pl = 1
                sign = 0
                for j in range(len(line)):
                    if line[j] == '.' and sign == 0:
                        a += 1
                    elif line[j] == 'x':
                        sign = 1
                    elif sign == 1 and line[j] == '-':
                        pl = -1
                    elif line[j] == '^':
                        sign = 2
                    elif sign == 1:
                        b += line[j]
                    elif line[j] == '.' and sign != 0:
                        c += 1
                if b:
                    b = int(b)
                else:
                    b = 1
                num = a * ((pl * b) ** c)
                list_n.append(num)
    print(list_n)
    

frieze(1)
numbers('test_1.txt')