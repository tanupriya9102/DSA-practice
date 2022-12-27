s="A man, a plan, a canal: Panama"
s= [i.lower() for i in s if i.isalnum()]
print(s)
return s == s[::-1]
