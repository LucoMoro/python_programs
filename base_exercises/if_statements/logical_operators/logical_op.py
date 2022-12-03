high_income=True
good_credit= True
criminal_credit= True

if high_income and good_credit:
    print("Eligible for loan")

if good_credit and not criminal_credit: #need 2 True so i use not to turn False into True
    print("Eligible for loan")

if high_income or good_credit:
    print("Kinda eligible for loan")