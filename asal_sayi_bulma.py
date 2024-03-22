n=int(input("bir sayi giriniz"))
asal=1
if(n==0 or n==1):
    print("asal sayi değil")
elif(n==2):
    print("asal sayidir")
elif(n%2==0):
    print("asal sayi değil")
else:
    i=3
    while(i*i<=n):
        if(n%i==0):
            asal=0
        i=i+2
    if(asal==0):
        print("asal sayi değildir")
    else:
        print("asal sayidir")