strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for i in range(6):
    sentence += strings[i] + ' '
print(sentence[:-1])

print(' '.join(strings))
