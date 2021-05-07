def convtostr(org_list, seperator=' '):
    return seperator.join(org_list)



list = ['dit', 'is', 'een', 'move']
# strlist = ''
strlist = convtostr(list)
print(type(strlist))
print(strlist)
