
### importing project_model which helps in classifying the complaint letter

import Project_Model as Model


file  = open("Complaint_letter_IP.txt","r").read()
print("Laws Related to Given Compliant letter: ")
query = Model.Analayse(file)
print(query)


Dictionary = {'law_1':'IP83','law_2':'IP84','law_3':'IP85','law_4':'IP86','law_5':'IP87','law_6':'IP88','law_7':'IP89','law_8':'IP90'}
print('Applicable law is : ')
print(Dictionary[query])