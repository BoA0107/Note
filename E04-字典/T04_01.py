phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
a = "Cecil's phone number is {Cecil}".format_map(phonebook)

print(a)
