import pandas as pd
from os.path import join
from os import getcwd

def strain_from_symptom(symptom):
    path = getcwd()
    filepath = join(path, "data", "medcabinet_dataset.csv")
    df = pd.read_csv(filepath)

    column_name = "symptom_" + symptom.lower().replace(" ", "_")

    df = df[df[column_name]]

    df = df.drop(columns=df.columns[8:])
    df = df.reset_index()
    df = df.rename(columns={'index':'id'})

    return df.to_json(orient='records', indent=1)