def interviewee_screening(df):
    min_exp=4
    qual=["bachelors","masters","phd"]
    min_age=22
    exp_lang=["python","java"]
    selected=[]

    for cv in df.to_dict(orient='records'):
        if (cv["experience"]>=min_exp) and (cv["qualification"] in qual) and (cv["age"]>=min_age) and (set(exp_lang).issubset(set(cv["languages"].split(",")))):
            selected.append(cv["name"])
    print(selected)