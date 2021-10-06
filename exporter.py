import pylightxl as xl


database = xl.readxl('methods.xlsx')

func_list = []
func_values = []

for i in range(2, 10007):
    func_list.append(database.ws(ws='Worksheet').address(address=('A' + str(i))))

for i in range(2, 10007):
    func_values.append(database.ws(ws='Worksheet').address(address=('B' + str(i))))

print('[')
for i in range(10005):
    print('[\'', str(func_list[i]), '\', \'', func_values[i], '\'], ', sep='')
print(']')
