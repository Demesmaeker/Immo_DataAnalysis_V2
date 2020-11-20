def print_unique_dtype(df, column):
    """Print unique and dtype of a given dataframe and given column"""

    unique = df[column].value_counts().nunique()
    dtype = df[column].dtype

    print(f"{unique} - {dtype}")


def set_surface(df):
    if df['surface_of_the_land'] < 2:
        if df['garden_area'] > 2:
            df['surface_of_the_land'] = df['house_area', 'garden_area', 'terrace_area'].sum(axis=1)



def get_region(province):
    if province == 'Bruxelles (19 communes)':
        return 'Région Bruxelles-capitale'
    elif province in ['Hainaut', 'Liège', 'Namur', 'Brabant wallon', 'Luxembourg']:
        return 'Région wallonne'
    else : 
        return 'Région flamande'
