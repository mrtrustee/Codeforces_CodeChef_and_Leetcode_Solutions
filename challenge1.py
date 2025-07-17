#The challenge just to input the flag as already found in the instruction
import base64
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
print(then)
print(attempt)

