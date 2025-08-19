from classfrac import fracao


def escolhermenu(num):
    while(1):
        try:
            x = int(input("Escolha: "))
        except:
            print("Inválido!")
            continue
        if(x <= num and x > 0):
            return x
        else:
            print("Inválido!")


if __name__ == "__main__":


    print("Digite as Frações iniciais:")
    print("Fração 1-")
    try:
        frac1 = fracao(int(input("Numerador: ")), int(input("Denominador: ")))
    except:
        frac1 = fracao(1,1)
        print("Inválido, valores base atribuídos.")
    print("Fração 2-")
    try:
        frac2 = fracao(int(input("Numerador: ")), int(input("Denominador: ")))
    except:
        frac2 = fracao(1,1)
        print("Inválido, valores base atribuídos.")

    while(1):
        print("Frações: " + str(frac1) + " e " + str(frac2) )
        print("1- Alterar Frações")
        print("2- Operações aritmétricas")
        print("3- Operações comparadoras")
        print("4- Sair")
        match(escolhermenu(4)):
            case 1:
                print("1- Fração 1")
                print("2- Fração 2")
                match(escolhermenu(2)):
                    case 1:
                        frac1.setnum(int(input("Numerador: ")))
                        frac1.setden(int(input("Denominador: ")))
                    case 2:
                        frac2.setnum(int(input("Numerador: ")))
                        frac2.setden(int(input("Denominador: ")))

            case 2:
                print("1- Adição")
                print("2- Subtração")
                print("3- Multiplicação")
                print("4- Divisão")
                match(escolhermenu(4)):
                    case 1:
                        fracres = frac1 + frac2
                    case 2:
                        fracres = frac1 - frac2
                    case 3:
                        fracres = frac1 * frac2
                    case 4: 
                        fracres = frac1 / frac2
                print("Mostrar resultado simplificado?")
                print("1- Sim     2- Não")
                match(escolhermenu(2)):
                    case 1:
                        try:
                            fracres.simpl()
                            print(fracres)
                        except:
                            print(fracres)
                    case 2:
                        print(fracres)
            
            case 3:
                print("1- Maior que")
                print("2- Menor que")
                print("3- Maior ou igual que")
                print("4- Menor ou igual que")
                print("5- Iguais")
                print("6- Diferentes")
                match(escolhermenu(6)):
                    case 1:
                        print(frac1 > frac2)
                    case 2:
                        print(frac1 < frac2)
                    case 3:
                        print(frac1 >= frac2)
                    case 4: 
                        print(frac1 <= frac2)
                    case 5:
                        print(frac1 == frac2)
                    case 6: 
                        print(frac1 != frac2)
                        
            case 4: 
                break

