import pickle
from os.path import join
from os import getcwd

def symptom_from_query(query):
    path = getcwd()
    model_filepath = join(path, "data", "model.p")
    count_vect_filepath = join(path, "data", "count_vect.p")
    clf = pickle.load(open(model_filepath, "rb"))
    count_vect = pickle.load(open(count_vect_filepath, "rb"))

    symptom = clf.predict(count_vect.transform([query])) 
    symptom = str(symptom[0])
    return(symptom)



if __name__ == "__main__":
    print(symptom_from_query("My head hurts."))