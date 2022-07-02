ones = {"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six", "7":"Seven","8":"Eight","9":"Nine"}
teens = {"10":"Ten","11":"Eleven","12":"Twelve","13":"Thirteen","14":"Fourteen","15":"Fifteen","16":"Sixteen", "17":"Seventeen","18":"Eighteen","19":"Nineteen"}
tens = {"2":"Twenty","3":"Thirty","4":"Fourty","5":"Fifty","6":"Sixty", "7":"Seventy","8":"Eighty","9":"Ninety"}

x = input("\nInput a number from 0-99:  ") 
tens_digit = int(x)//10
ones_digit = int(x)%10

converted_tens_digit = str(tens_digit)
converted_tens_digit_2 = tens[converted_tens_digit]
converted_ones_digit = str(ones_digit)
converted_ones_digit_2 = ones[converted_ones_digit]

print(f"\n{converted_tens_digit_2}-{converted_ones_digit_2}")