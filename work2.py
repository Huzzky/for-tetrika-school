arrayForNames,strForName=[],""
#Чтение имен
f = open('names.txt', 'r')
read = f.read()
past_read = read.replace('"','')
f.close()

for i in past_read:
	#Убрали "" и поместили в массив
	if i!=',':
		strForName=strForName+i
	elif i==",":
		arrayForNames.append(strForName)
		strForName=""
#Отсортировали
sorted_read=sorted(arrayForNames)

arrayForWord= []
itORD = ord('a')
Word = ''.join([chr(i) for i in range(itORD,itORD+26)])
for i in Word:
	#Добавляем буквы англ алфавита
	arrayForWord.append(i.upper())

arrayNumberWord,fa=[],0
for i in sorted_read:
	#Считаем сумму порядковыъ номеров букв
	for j in i:
		for m in arrayForWord:
			if j==m:
				fa=fa+arrayForWord.index(m)+1
	arrayNumberWord.append(fa)
	fa=0

sumNumbWord = [] 
for i in arrayNumberWord:
	#Умножаем число на его индекс+1
	sumNumbWord.append(i*(arrayNumberWord.index(i)+1))
allSum=0
for i in sumNumbWord:
	#Считаем сумму произведений из пункта 3
	allSum+=i
#ВЫВОД СУММЫ
print(allSum)

