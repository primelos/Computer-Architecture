Operation           Boolean Operator        Bitwise
AND                     &&                      &
OR                      ||                      |
XOR                                             ^
NOT                      !                      ~


AND
a = True
b = False
a && b == False


  0b10000011
& 0b01010101
--------------
  0b00000001

OR
a = True
b = True
a||b == True

0b10101110
0b11010001
-----------
0b11111111

XOR
a = False
b = True
a xor b == True

a = True
b = True
a xor b == False

 0b10101101
 0b00110110
 ----------
 0b10011011

 NOT
 ~0b10101010
 ------------
  0b01010101

  right bit shifting
  0b10101010
  0b01010101 >> 1
  0b00101010 >> 2
  
  left bit shifting
      0b10101010
     0b101010100  << 1
    0b1010101000  << 2


 bitmasking
   0b10101010   if you want the last 2 valueson the right use the &
 & 0b00000011
   ----------
   0b00000010