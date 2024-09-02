def mr_decoder(numer=20):
    intermediate, result = [], ''
    for i in range(1, numer+1):
        for j in range(1, i+1):
            if numer % (i+j) == 0 and i != j:
                intermediate.append([j, i])
                #print(intermediate)
    for k in sorted(intermediate):
        x = str(k[0]) + str(k[1])
        result = result + x
    return result
print(mr_decoder(int(input('Введите число с первого камня: '))))
