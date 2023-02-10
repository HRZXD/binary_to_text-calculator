import os
os.system("cls")

#binary to text
binary = []
binary_output = []
translate =[]
times = 0
y = int(input("Enter your times of your binary : "))
times += y
for i in range(times):
    x = input("Enter your binary : ")
    binary.append(x)
    binary_output.append(x)
    # translate to text
    if "01000001" in binary:
        trns = "A"
        translate.append(trns)
        binary.remove("01000001")
        
    elif "01000010" in binary:
        trns = "B"
        translate.append(trns)
        binary.remove("01000010")
        
    elif "01000011" in binary:
        trns = "C"
        translate.append(trns)
        binary.remove("01000011")
        
    elif "01000100" in binary:
        trns = "D"
        translate.append(trns)
        binary.remove("01000100")
        
    elif "01000101" in binary :
        trns = "E"
        translate.append(trns)
        binary.remove("01000101")
        
    elif "01000110" in binary :
        trns = "F"
        translate.append(trns)
        binary.remove("01000110")
        
    elif "01000111" in binary :
        trns = "G"
        translate.append(trns)
        binary.remove("01000111")
        
    elif "01001000" in binary :
        trns = "H"
        translate.append(trns)
        binary.remove("01001000")
        
    elif "01001001" in binary :
        trns = "I"
        translate.append(trns)
        binary.remove("01001001")
        
    elif "01001010" in binary :
        trns = "J"
        translate.append(trns)
        binary.remove("01001010")
        
    elif "01001011" in binary :
        trns = "K"
        translate.append(trns)
        binary.remove("01001011")
        
    elif "01001100" in binary :
        trns = "L"
        translate.append(trns)
        binary.remove("01001100")
        
    elif "01001101" in binary :
        trns = "M"
        translate.append(trns)
        binary.remove("01001101")
        
    elif "01001110" in binary :
        trns = "N"
        translate.append(trns)
        binary.remove("01001110")
        
    elif "01001111" in binary :
        trns = "O"
        translate.append(trns)
        binary.remove("01001111")
        
    elif "01010000" in binary :
        trns = "P"
        translate.append(trns)
        binary.remove("01010000")
        
    elif "01010001" in binary :
        trns = "Q"
        translate.append(trns)
        binary.remove("01010001")
        
    elif "01010010" in binary :
        trns = "R"
        translate.append(trns)
        binary.remove("01010010")
        
    elif "01010011" in binary :
        trns = "S"
        translate.append(trns)
        binary.remove("01010011")
        
    elif "01010100" in binary :
        trns = "T"
        translate.append(trns)
        binary.remove("01010100")
        
    elif "01010101" in binary :
        trns = "U"
        translate.append(trns)
        binary.remove("01010101")
        
    elif "01010110" in binary :
        trns = "V"
        translate.append(trns)
        binary.remove("01010110")
        
    elif "01010111" in binary :
        trns = "W"
        translate.append(trns)
        binary.remove("01010111")
        
    elif "01011000" in binary :
        trns = "X"
        translate.append(trns)
        binary.remove("01011000")
        
    elif "01011001" in binary :
        trns = "Y"
        translate.append(trns)
        binary.remove("01011001")
        
    elif "01011010" in binary :
        trns = "Z"
        translate.append(trns)
        binary.remove("01011010")
    
    elif "00100000" in binary :
        trns = " "
        translate.append(trns)
        binary.remove("00100000")

def ListToString(m):
    strcv =""
    return(
        strcv.join(m)
        )

def ListToBinary(v):
    strcv =" "
    return(
        strcv.join(v)
        )

os.system("cls")

print("Your binary that input :" , ListToBinary(binary_output))
print("Your text that translated :" , ListToString(translate))
