def king(a,b):
    first= a.split(" ")
    second = b.split(" ")
    common = []
    for i in first:
        for j in second:
            if(i == j):
                common +=[j]      #common=common+[j]  can be written in this form also
    return common

print(king("sujal is here","king is here"))

