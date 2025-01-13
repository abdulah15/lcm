def findhcf (no1, no2):
    while no1:
        numberStore = no1
        no2 = no1 % no2
        no2 = numberStore
        print("HCF is: ", no2)
        break

numberLargest = int(input( "Enter the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))
findhcf (numberLargest, numberSmallest)