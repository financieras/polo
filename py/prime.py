def nprimos(n):
    lista = []
    i = 2
    while n != 0:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            lista.append(i)
            n -= 1
        i += 1
    return lista

if __name__ == "__main__":
    n = 10
    print(nprimos(n))