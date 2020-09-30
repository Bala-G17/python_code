def sentance(phrase):
    pack=("how","why","what")
    caps=phrase.capitalize()
    if phrase.startswith(pack):
        return('{}?'.format(caps))
    else:
        return('{}.'.format(caps))
result=[]
while True:
    user_input = input("say something: ")
    if user_input == '\end':
        break
    else:
        result.append(sentance(user_input))
print(" ".join(result))