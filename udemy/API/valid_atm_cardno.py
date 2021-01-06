"""
The algorithm we're going to use to verify card numbers is called the Luhn algorithm, 
or Luhn formula. This algorithm is actually used in real-life applications to test
credit or debit card numbers as well as SIM card serial numbers.

"""
card_no = list((input("Enter a card no")))

diz_list = []
counter = 0
for diz in card_no:
    diz_list.append(int(diz))

"""
I can also take an input as below which i will prefer too pythonic...

    card_no_list = list(int(s) for s in input("Enter Card no").strip())
    print(card_no_list)

"""
print(diz_list)  # list of diz
checking_diz = diz_list.pop()
diz_list.reverse()
print(diz_list)  # printing the list after removing the last element and reversing

"""  will be better to use the enumerate function 
as below

    for index, diz in enumerate(diz_list):
        print(index)
        print(diz)
"""

for i in range(0,len(diz_list)):
    if i%2 ==0:
        diz_list[i] = diz_list[i]*2
        if diz_list[i] > 9:
            diz_list[i] -=9

print(diz_list)

sum_diz_with_cheking = sum(diz_list)+ checking_diz
if sum_diz_with_cheking %10 ==0:
    print("It is a valid no")
else:
    print("Card no invalid")
