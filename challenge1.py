#The challenge just to input the flag as already found in the instruction
flag ="crypto{y0ur_f1rst_fl4g}"
#for Ascii, to convert the number given
list_ = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
then = ""
for i in list_:
    conv = chr(i)
    then = then + conv
print(then)
