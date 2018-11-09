
### importing project_model which helps in classifying the complaint letter

import Project_Model as Model


file  = open("complaint letter 1.txt","r").read()
print("Laws Related to Given Compliant letter: ")
query = Model.Analayse(file)
print(query)

### Importing Database for querying out nedded case histories

import Data_base as db

print("Related Case/Judgement History :")
db.query_(query)


