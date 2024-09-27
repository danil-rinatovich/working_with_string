my_dict = {'Anastasia': 2000, 'Danil': 2001}
print('Dict:', my_dict)
print('Existing value:', my_dict['Anastasia'])
print('Not existing value:', my_dict.get('Silva'))
my_dict.update({'Trisha': 2010, 'Luffy': 2013})
print('complete_dictionary:', my_dict)
my_dict.pop('Danil')
print('Deleted value:', my_dict, '\n')

my_set = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1}
print('Set:', my_set)
my_set.add('String')
my_set.add(7.1)
print('Modified set', my_set)
my_set.discard(7.1)
my_set.remove('String')
print('result', my_set)