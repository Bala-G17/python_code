#listing prime number of user's given range

print("List prime number of user's range")
start=int(input("Enter the starting number : "))
end=int(input("Enter the ending number : "))

def prime_number(start,end):
    for i in range(start,end):
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
        if prime:
            print(i)
    
    
prime_number(start,end)
