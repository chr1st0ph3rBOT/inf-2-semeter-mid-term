# 내 풀이
class main:
    def __init__(self, remainig_seats):
        self.remainig_seats = remainig_seats

    def __str__(self):
        if self.remainig_seats > 0:
            self.remainig_seats = self.remainig_seats - 1
            return "Booking Granted"
        else:
            return "Sold Out"
            
n=3
print('스머프')
스머프 = main(n)
for _ in range(n+1):
    print(스머프)

m = 7
print('인터스텔라')
인터스텔라 = main(m)
for _ in range(m+1):
    print(인터스텔라)
