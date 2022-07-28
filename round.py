def myRound(number):
     if len(str(number).split('.')) == 1:
          return number
     int_number = str(number).split('.')[0]
     float_number = f"0.{str(number).split('.')[1]}"
     if float(float_number) >= 0.5 and int(int_number) % 2 != 0:
          return int(int_number) + 1
     return int(int_number)

def test_myRound():
     assert myRound(1.5) == 2
     assert myRound(1.4) == 1
     assert myRound(1.6) == 2
     assert myRound(1.1) == 1
     assert myRound(1.9) == 2
     assert myRound(1.0) == 1
     assert myRound(1.7) == 2
     assert myRound(1.8) == 2
     assert myRound(1.9) == 2
     assert myRound(1.01) == 1
     assert myRound(1.02) == 1
     assert myRound(1.03) == 1
     assert myRound(1.04) == 1
     assert myRound(1.05) == 2
     assert myRound(1.06) == 2
     assert myRound(1.07) == 2
     assert myRound(1.08) == 2
     assert myRound(1.09) == 2
     assert myRound(1.10) == 2
     assert myRound(1.11) == 2
     assert myRound(1.12) == 2
     assert myRound(1.13) == 2
     assert myRound(1.14) == 2
     assert myRound(1.15) == 2
     assert myRound(1.16) == 2
     assert myRound(1.17) == 2
     assert myRound(1.18) == 2
     assert myRound(1.19) == 2
     assert myRound(1.20) == 2
     assert myRound(1.21) == 2
     assert myRound(1.22) == 2
     assert myRound(1.23) == 2
     assert myRound(1.24) == 2
     assert myRound(1.25) == 2
     assert myRound(1.26) == 2
     assert myRound(1.27) == 2
     assert myRound(1.28) == 2
     assert myRound(1.29) == 2
     assert myRound(1.30) == 2
     assert myRound(1.31) == 2
     assert myRound(1.32) == 2
     assert myRound(1.33) == 2
     assert myRound(10) == 10
     assert myRound(11.4) == 11
     assert myRound(2.5) == 2
     assert myRound(11.6) == 12