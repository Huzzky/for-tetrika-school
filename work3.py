n=16
def get_zeros(n):
	num,count,num_zeroes=1,0,0
	while n>=1:
		#Вычисление факториала
		num=num*n
		n=n-1
	for i in str(num):
		if i=="0":
			num_zeroes+=1
		elif i!='0' and num_zeroes>0:
			num_zeroes-=1
	return num_zeroes
print(get_zeros(n))