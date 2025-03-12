if __name__ == '__main__':
    Lista=[1,2,87,5,7,3,2,8,5,10,78,56,98,16,37,-8,100,70,58]
    totales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    adoptados: int = 0
    for elemento in Lista:

        # print(elemento)
        match elemento:
            case 1: totales[0]+=1
            case 2: totales[1]+=1
            case 3: totales[2]+=1
            case 4: totales[3]+=1
            case 5: totales[4]+=1
            case 6: totales[5]+=1
            case 7: totales[6]+=1
            case 8: totales[7]+=1
            case 9: totales[8]+=1
            case 10: totales[9]+=1
            case _: adoptados+=1
    i = 1
    for n in totales:
        print(f" {i}.- {n}")
        i += 1
    print(f"Y el total de conocidos es {adoptados}")








