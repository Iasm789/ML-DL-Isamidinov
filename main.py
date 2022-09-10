import re
import numpy as np
import random

class Model(object):
    
    def fit(self):
        name_training = str(input('введите название файла train '))
        f = open('{}'.format(name_training))
        text = ''
        for line in f.readlines():
            text+=str(line)
        f.close()
        
        #форматирование текста
        text = text.lower()
        text = text.strip()
        text = re.split("[^a-zа-яё]+",text)
        
        
        dictionary = {}
        for i in range(len(text)-1):
            if dictionary.get(text[i],0):
                pointer = dictionary.get(text[i])
                pointer.append(text[i+1])
                dictionary[text[i]]=pointer
            else:
                dictionary[text[i]]=[text[i+1]]
                
        
        name_file = str(input('введите название модели сохранения '))
        np.save('{}.npy' .format(name_file), dictionary)

    def generate(self):
        
        
        name_file = str(input('введите название модели зарузки '))
        read_dictionary = np.load('{}.npy' .format(name_file)).item()
        
        
        sequence=''
        length_text=int(input('введите длину генерируемой последовательности '))
        for i in range(length_text):
            if i==0:
                elem_ahead = random.choice(list(read_dictionary.keys()))
                sequence += elem_ahead
                sequence += ' '
            else:
                elem_now = random.choice(read_dictionary.setdefault(elem_ahead))
                sequence += elem_now
                sequence += ' '
                elem_ahead = elem_now 
        return sequence
obj = Model()
print(obj.generate())
