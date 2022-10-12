#author = PassePortOut

def kaprekar(sayi, all=False):
    big = " "
    little = " "
    adim = 0
    while sayi != 6174:
        sayi_list = sorted([_ for _ in str(sayi)])
        sayi_listReverse = sorted([_ for _ in str(sayi)])
        sayi_listReverse.reverse()
        for i,j in zip(sayi_list, sayi_listReverse):
            big += j
            if i != 0 : little += i
        sayi = abs(int(big)-int(little))
        if not all: print(f"{big} - {little} = {sayi}")
        big,little = " "," "
        adim += 1
    return f"You reached Kaprekar number 6174 in {adim} steps", adim
    

def main(all = False):
    if all:
        liste = []
        for i in range(1001, 10000):
            if len(set(_ for _ in str(i))) >= 3:
                print(f"{i}, number can reach kaprekar number in {kaprekar(i, 1)[1]}")
            else: pass
    else:
        sayi = int(input("Give a number"))
        if 10000>sayi>1000:
            pass
        else:
            raise Exception("The number must be 4 digits")
        if len(set(_ for _ in str(sayi))) <= 2:
            raise Exception("Each digit of a number cannot be a separate number.")
        print(kaprekar(sayi)[0])
main(all=True)