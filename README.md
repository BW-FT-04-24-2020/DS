# DS

# Installing and running API app:

1) Install python 3.7

2) install pipenv with ```pip3 install pipenv``` or ```pip install pipenv``` (whichever works)

3) CD into DS directory

4) Install pipenv requirements with ```pipenv install```

5) Activate pipenv shell with ```pipenv shell```

6) Run app with ```flask run```

7) When done, exit pipenv shell with ```exit```

# Testing server status:

Go to http://localhost:5000/jsontest

# Getting all strains:

Go to http://localhost:5000/strains/all 

# Getting a strain by ID:

Go to http://localhost:5000/strains/id/[id]

Example: 'http://localhost:5000/strains/id/420'

# Getting strains by symptom:

Go to http://localhost:5000/strains/symptom/[symptom]

Example: 'http://localhost:5000/strains/symptom/insomnia', 'http://localhost:5000/strains/symptom/Eye Pressure'

Note: Not caps sensitive, and still accepts symptoms with spaces in the name.

# Getting strains by query:

Go to http://localhost:5000/strains/query/[query]

Example: 'http://localhost:5000/strains/query/My head hurts', "http://localhost:5000/strains/query/I can't go to sleep."

Note: Still accepts queries with spaces and special characters in them. Please let me know if you find any input that breaks things.