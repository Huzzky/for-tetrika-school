array = [1,2,3,4,5,6,7,8,9,12,41,431,513,351,325,3,5,15,3,51,51,3,13,132,6,876,69,6548,35,34,75,3,26,9]
k = 15
def search_pairs(array, k):
	for i in range(len(array)):
		try:
			if (array[i]+array[i+1])==k:
				return array[i], array[i+1]
				break
			else:
				return "Пусто."
		except IndexError:
			pass

print(search_pairs(array,k))