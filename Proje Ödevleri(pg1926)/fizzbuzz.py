#fizzbuzz

for sayılar in range(0,100):
    if sayılar % 3 == 0 and sayılar % 5 == 0:
        print("fizzbuzz")
        continue
    elif sayılar % 3 == 0:
        print("fizz")
        continue
    elif sayılar % 5 == 0:
        print("buzz")
        continue
    print(sayılar)
	