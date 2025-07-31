# 내 풀이
class main:
    def __init__(self, remaining_seats, seats):
        self.remainig_seats = remaining_seats
        self.seats = seats

    def __str__(self):
        if self.remainig_seats > 0:
            self.remainig_seats = self.remainig_seats - 1
            return "Booking Granted"
        else:
            return "Sold Out"
            
CGV = main(1, 100)
print(CGV)
print(CGV)

