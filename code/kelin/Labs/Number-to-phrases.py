# Lab 3: Number to Phrase
# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

one = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
ten = {'1':'ten','2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
teen = {'11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
hundred = {'1':'one hundred','2':'two hundred','3':'three hundred','4':'four hundred','5':'five hundred','6':'six hundred','7':'seven hundred','8':'eight hundred','9':'nine hundred'}
hundred_ten = {'12':'twenty','13':'thirty','14':'forty','15':'fifty','16':'sixy','17':'seventy','18':'eighty','19':'ninety'}
hundred_teen = {'111':'eleven','112':'twelve','113':'thirteen','114':'fourteen','115':'fifteen','116':'sixteen','117':'seventeen','118':'eighteen','119':'nineteen'}
two_hundred_teen = {'211':'eleven','212':'twelve','213':'thirteen','214':'fourteen','215':'fifteen','216':'sixteen','217':'seventeen','218':'eighteen','219':'nineteen'}
three_hundred_teen = {'311':'eleven','312':'twelve','313':'thirteen','314':'fourteen','315':'fifteen','316':'sixteen','317':'seventeen','318':'eighteen','319':'nineteen'}
four_hundred_teen = {'411':'eleven','412':'twelve','413':'thirteen','414':'fourteen','415':'fifteen','416':'sixteen','417':'seventeen','418':'eighteen','419':'nineteen'}
five_hundred_teen = {'511':'eleven','512':'twelve','513':'thirteen','514':'fourteen','515':'fifteen','516':'sixteen','517':'seventeen','518':'eighteen','519':'nineteen'}
six_hundred_teen = {'611':'eleven','612':'twelve','613':'thirteen','614':'fourteen','615':'fifteen','616':'sixteen','617':'seventeen','618':'eighteen','619':'nineteen'}
seven_hundred_teen = {'711':'eleven','712':'twelve','713':'thirteen','714':'fourteen','715':'fifteen','716':'sixteen','717':'seventeen','718':'eighteen','719':'nineteen'}
eight_hundred_teen = {'811':'eleven','812':'twelve','813':'thirteen','814':'fourteen','815':'fifteen','816':'sixteen','817':'seventeen','818':'eighteen','819':'nineteen'}
nine_hundred_teen = {'911':'eleven','912':'twelve','913':'thirteen','914':'fourteen','915':'fifteen','916':'sixteen','917':'seventeen','918':'eighteen','919':'nineteen'}
hundred_twenty = {'22':'twenty','23':'thirty','24':'forty','25':'fifty','26':'sixty','27':'seventy','28':'eighty','29':'ninety'}
hundred_thirty = {'32':'twenty','33':'thirty','34':'forty','35':'fifty','36':'sixty','37':'seventy','38':'eighty','39':'ninety'}
hundred_forty = {'42':'twenty','43':'thirty','44':'forty','45':'fifty','46':'sixty','47':'seventy','48':'eighty','49':'ninety'}
hundred_fifty = {'52':'twenty','53':'thirty','54':'forty','55':'fifty','56':'sixty','57':'seventy','58':'eighty','59':'ninety'}
hundred_sixty = {'62':'twenty','63':'thirty','64':'forty','65':'fifty','66':'sixty','67':'seventy','68':'eighty','69':'ninety'}
hundred_seventy = {'72':'twenty','73':'thirty','74':'forty','75':'fifty','76':'sixty','77':'seventy','78':'eighty','79':'ninety'}
hundred_eighty = {'82':'twenty','83':'thirty','84':'forty','85':'fifty','86':'sixty','87':'seventy','88':'eighty','89':'ninety'}
hundred_ninety = {'92':'twenty','93':'thirty','94':'forty','95':'fifty','96':'sixty','97':'seventy','98':'eighty','99':'ninety'}

num = input('Enter a number between 0 and 999: ')
ones = int(num)%10
teens = int(num)
tens = int(num)//10
hundreds = int(num)//100
user_num = int(num)

if user_num == 0:
    print('zero')

elif user_num < 10:
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_ones)

elif user_num in range (11, 20):
    teens_phrase = str(teens)
    num_phrase_teens = teen[teens_phrase]
    print(num_phrase_teens)

elif user_num in range (10, 100, 10):
    tens_phrase = str(tens)
    num_phrase_tens = ten[tens_phrase]
    print(num_phrase_tens)

elif user_num in range (20, 100, 1):
    tens_phrase = str(tens)
    num_phrase_tens = ten[tens_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_tens,num_phrase_ones)

# Version 2
# Handle numbers from 100-999.

elif user_num in range (100, 1000, 100):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    print(num_phrase_hundreds)

elif user_num in range (100, 1000, 10):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    tens_phrase = str(tens)
    num_phrase_tens = hundred_ten[tens_phrase]
    print(num_phrase_hundreds,num_phrase_tens)

elif user_num in range (100, 109, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_ones)

elif user_num in range (200, 209, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_ones)

elif user_num in range (300, 309, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_ones)

elif user_num in range (400, 409, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_ones)

elif user_num in range (500, 509, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_ones)

elif user_num in range (600, 609, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_ones)

elif user_num in range (700, 709, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_ones)

elif user_num in range (800, 809, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_ones)

elif user_num in range (900, 909, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_ones)

elif user_num in range (111, 120, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    teens_phrase = str(teens)
    num_phrase_teens = hundred_teen[teens_phrase]
    print(num_phrase_hundreds,num_phrase_teens)

elif user_num in range (121, 200, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    tens_phrase = str(tens)
    num_phrase_tens = hundred_ten[tens_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_tens,num_phrase_ones)

elif user_num in range (211, 220, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    teens_phrase = str(teens)
    num_phrase_teens = two_hundred_teen[teens_phrase]
    print(num_phrase_hundreds,num_phrase_teens)

elif user_num in range (311, 320, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    teens_phrase = str(teens)
    num_phrase_teens = three_hundred_teen[teens_phrase]
    print(num_phrase_hundreds,num_phrase_teens)

elif user_num in range (411, 420, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    teens_phrase = str(teens)
    num_phrase_teens = four_hundred_teen[teens_phrase]
    print(num_phrase_hundreds,num_phrase_teens)

elif user_num in range (511, 520, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    teens_phrase = str(teens)
    num_phrase_teens = five_hundred_teen[teens_phrase]
    print(num_phrase_hundreds,num_phrase_teens)

elif user_num in range (611, 620, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    teens_phrase = str(teens)
    num_phrase_teens = six_hundred_teen[teens_phrase]
    print(num_phrase_hundreds,num_phrase_teens)

elif user_num in range (711, 720, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    teens_phrase = str(teens)
    num_phrase_teens = seven_hundred_teen[teens_phrase]
    print(num_phrase_hundreds,num_phrase_teens)

elif user_num in range (811, 820, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    teens_phrase = str(teens)
    num_phrase_teens = eight_hundred_teen[teens_phrase]
    print(num_phrase_hundreds,num_phrase_teens)

elif user_num in range (911, 920, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    teens_phrase = str(teens)
    num_phrase_teens = nine_hundred_teen[teens_phrase]
    print(num_phrase_hundreds,num_phrase_teens)

elif user_num in range (221, 300, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    tens_phrase = str(tens)
    num_phrase_tens = hundred_twenty[tens_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_tens,num_phrase_ones)

elif user_num in range (321, 400, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    tens_phrase = str(tens)
    num_phrase_tens = hundred_thirty[tens_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_tens,num_phrase_ones)

elif user_num in range (421, 500, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    tens_phrase = str(tens)
    num_phrase_tens = hundred_forty[tens_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_tens,num_phrase_ones)

elif user_num in range (521, 600, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    tens_phrase = str(tens)
    num_phrase_tens = hundred_fifty[tens_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_tens,num_phrase_ones)

elif user_num in range (621, 700, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    tens_phrase = str(tens)
    num_phrase_tens = hundred_sixty[tens_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_tens,num_phrase_ones)

elif user_num in range (721, 800, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    tens_phrase = str(tens)
    num_phrase_tens = hundred_seventy[tens_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_tens,num_phrase_ones)

elif user_num in range (821, 900, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    tens_phrase = str(tens)
    num_phrase_tens = hundred_eighty[tens_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_tens,num_phrase_ones)

elif user_num in range (921, 1000, 1):
    hundreds_phrase = str(hundreds)
    num_phrase_hundreds = hundred[hundreds_phrase]
    tens_phrase = str(tens)
    num_phrase_tens = hundred_ninety[tens_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_hundreds,num_phrase_tens,num_phrase_ones)

else:
    print('Number out of range.')

# Version 3 (optional)
# Convert a number to roman numerals.

# Version 4 (optional)
# Convert a time given in hours and minutes to a phrase.