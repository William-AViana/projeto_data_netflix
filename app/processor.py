import pandas as pd
import numpy as np
import zipfile
import os

def load_data() -> pd.DataFrame | None:
    all_data = []
    directory = './data'
    
    for item in os.listdir(directory):
        if item.endswith('.zip'):
            path_zip = os.path.join(directory, item)
            with zipfile.ZipFile(path_zip, 'r') as unzip_file:
                for file in unzip_file.namelist():
                    if file.endswith('.csv'):
                        with unzip_file.open(file) as f:
                            df = pd.read_csv(f)
                            all_data.append(df)
                        
    if all_data:
        all_data_frame = pd.concat(all_data, ignore_index=True)
        return all_data_frame
    return None
    
def validade_datas(df=load_data()):

    if df is not None:
        total_titles = len(df)
        years = df['release_year'].unique()
        return {
                "total_titles": total_titles,
                "period": f"{np.min(years)} - {np.max(years)}"
            }
    return {"error": "Datas is not find"}
