import pandas as pd 

try:
    df=pd.read_csv('disease.csv',header=0,index_col=0,na_values=["NaN"])
    df.replace(pd.NA,"NO",inplace=True)
except Exception:
    df=pd.DataFrame()

while True:
    print("Menu\n1 : Add new disease\n2 : Run diagnosis\n3 : Exit")
    option=input("Enter your choice:")

    if option=='1':
        name=input("Enter the name of the disease:").strip().lower()
        num=int(input("Enter the number of symptoms:"))
        for i in range(num):
            symptom=input(f"Enter the symptom {i+1} for {name}:").strip().lower()
            df.loc[name,symptom]="YES"
        df.to_csv("disease.csv")
        print("New disease added successfully")

    elif option=='2':
        symptoms={}
        for i in df.columns:
            symptoms[i] = input(f"Do you have {i} as a symptom? (yes/no) -").strip().upper()
        found=False
        for i in df.index:
            for j in df.columns:
                d=dict(df.loc[i])
                if d==symptoms:
                    found=True
                    print(f"Diagnosis: {i}")
                    break
        if not found:
            print("No diagnosis could be made")

    elif option=='3':
        exit(0)

    else:
        print("Invalid option try again")