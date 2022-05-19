class Power_two:

    def power2(self,terms):

        result = list(map(lambda x: 2 ** x , range(terms)))

        print("total terms " , terms )

        for i  in  range(terms):
            print(" 2 raised to power ", i ,"is ", result[i])


if __name__ == '__main__':
    pow = Power_two()
    pow.power2(5)