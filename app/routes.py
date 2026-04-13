from flask import request, jsonify
from processor import process_clean_data, duration_analiser
from app import app

df_netflix = process_clean_data()

@app.route('/', methods=['GET'])
def get_statistics():
    country = request.args.get('country')
    
    df_filtered = df_netflix
    if country:
        df_filtered = df_netflix[df_netflix['country'].str.contains(
            country, case=False, na=False)]
    
    result = duration_analiser(df_filtered)

    return jsonify({
            "country_analysed": country if country else "Global",
            "metrics": result
        })
    