# Strings
text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')#index of ':'
prnt = text[pos+1:]#store the elements of the string after ':'
value = float(prnt)#converting the string into floating point number
