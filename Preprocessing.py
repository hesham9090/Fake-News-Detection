import re
def Preprocess_text(data):
    data['Title'] = data['Title'].apply(lambda x: re.sub(r'[^a-zA-Z0-9 ]',r' ',x))
    data['Title'] = data['Title'].apply(lambda x: x.lower())
    data['Title'] = data['Title'].apply(lambda x: re.sub(r'[0-9]+',r' NUM ',x))
    data['Article'] = data['Article'].apply(lambda x: re.sub(r'[^a-zA-Z0-9 ]',r' ',x))
    data['Article'] = data['Article'].apply(lambda x: x.lower())
    data['Article'] = data['Article'].apply(lambda x: re.sub(r'[0-9]+',r' NUM ',x))
    data['Author'] = data['Author'].apply(lambda x: re.sub(r'[^a-zA-Z0-9 ]',r' ',x))
    data['Author'] = data['Author'].apply(lambda x: x.lower())
    data['Author'] = data['Author'].apply(lambda x: re.sub(r'[0-9]+',r' NUM ',x))
    return data