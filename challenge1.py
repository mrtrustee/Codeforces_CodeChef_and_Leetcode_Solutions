#The challenge just to input the flag as already found in the instruction
import base64
from binascii import unhexlify

message = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"
string_ = "label"
flag_ = " "
for j in string_:
    flag_+= chr(ord(j) ^ 13)
data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded_data = bytes.fromhex(data)

input_ = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
convert = bytes.fromhex(input_)
attempt = base64.b64encode(convert)

flag ="crypto{y0ur_f1rst_fl4g}"
#for Ascii, to convert the number given
list_ = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
then = ""
for i in list_:
    conv = chr(i)
    then = then + conv

print()
print(then)
print(attempt)

