import pandas as pd
from os.path import join
from os import getcwd

def strain_from_id(strain_id):
    path = getcwd()
    filepath = join(path, "data", "medcabinet_dataset.csv")
    df = pd.read_csv(filepath)
    df = df.drop(columns=df.columns[8:])
    df = df.reset_index()
    df = df.rename(columns={'index':'id'})

    df = df[df['id'] == strain_id]
    
    return df.to_json(orient='records')