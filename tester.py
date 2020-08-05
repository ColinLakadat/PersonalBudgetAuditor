###########
List= [['1001', '45,0504'],['1002','45,000000']]

def Tester():
    for x in List:
        print(x[0])
        if x[0] == '1002':
            print('Yes')
        else:
            print('No')
