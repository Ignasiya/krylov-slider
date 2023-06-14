old_name = ['<div>', '<img data-u="image" src="img/1.jpg" />', '<img data-u="thumb" src="img/1.jpg" />', '</div>']

with open('name.txt', 'w') as txt_file:
    for i in range(1, 224):
        print(old_name[0], file=txt_file)
        print('\t' + str(old_name[1]).replace('1', str(i)), file=txt_file)
        print('\t' + str(old_name[2]).replace('1', str(i)), file=txt_file)
        print(old_name[3], file=txt_file)