text = []
for i in range(5):
	text.append(input())
print(text)

for i in range(max(len(e) for e in text)):
	print(i)
	for j in range(5):
		if i < len(text[j]):
			#print(text[j][i], end="")
			pass
