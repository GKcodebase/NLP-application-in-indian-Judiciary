
### importing project_model which helps in classifying the complaint letter

import Project_Model as Model


file  = open("Compliant_letter_NGT.txt","r").read()
print("Laws Related to Given Compliant letter: ")
query = Model.Analayse(file)
print(query)


Dictionary = {'law_1':'NGT16','law_2':'NGT17','law_3':'NGT18','law_4':'NGT19','law_5':'NGT20','law_6':'NGT21','law_7':'NGT22','law_8':'NGT23'}
print('Applicable law is : ')
print(Dictionary[query])