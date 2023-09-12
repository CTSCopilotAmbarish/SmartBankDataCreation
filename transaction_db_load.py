from faker import Faker
import datetime
import pandas as pd
import random
fake = Faker()

 

data = {'User ID':[],
        'Transaction ID':[],
        'Transaction Clustering Type':[],
        'Transaction Type':[],
        'Transaction Datetime':[],
        'Transaction Text':[],
        'Amount':[],
        'Debit/Credit':[]}

 

salary_month = 6
salary_year = 2023
prev_user = ''
#prev_user_salary = 100000

 

cluster_choice = ['Food','Travel','Medical','Credit Repayments','Investments','Salary Credit','Bank Interest']
payment_choice = ['Cash','Debit Card','Credit Card','UPI']
trans_text_food = ['Lunch Ordered from Zomato','Dinner Ordered from Zomato','Lunch Ordered from Swiggy',
                   'Dinner Ordered from Swiggy','Lunch with Family','Dinner with Family','Office Snacks','Office Lunch']
trans_text_travel = ['Office Commute','Family Vacation']
trans_text_medical = ['Medicine Purchase','Visit to Doctor','Hospital Admition']
trans_text_loans = ['Home Loan Payment', 'Car Loan Payment','Personal Loan Payment']
trans_text_invest = ['Stocks Purchase', 'Investments in Mutual Funds','Investment in Fixed Deopsit']

 

for i in range(1,3):
    username = 'USER_' + str(i)
    prev_user_salary = random.randrange(100000,250000)
    for j in range(random.randrange(150,250)):
        #User ID generation
        data['User ID'].append(username)

        #Transaction ID generation for each User ID
        if j < 10:
            data['Transaction ID'].append(str(i) + '0000000' + str(j))
        elif j < 100:
            data['Transaction ID'].append(str(i) + '000000' + str(j))
        elif j < 1000:
            data['Transaction ID'].append(str(i) + '00000' + str(j))
        elif j < 10000:
            data['Transaction ID'].append(str(i) + '0000' + str(j))
        else:
            data['Transaction ID'].append(str(i) + '000' + str(j))

        #Cluster Type generation
        cluster_type = random.choices(cluster_choice,weights=(25,20,20,10,15,5,5),k=1)
        cluster_type = cluster_type[0]
        data['Transaction Clustering Type'].append(cluster_type)

        #Transaction Type generation
        if (cluster_type == 'Salary Credit' or cluster_type == 'Bank Interest'):
            data['Transaction Type'].append('NEFT')
        else:
            data['Transaction Type'].append(random.choice(payment_choice))

        #Transaction Datetime generation
        data['Transaction Datetime'].append((fake.date_time_between(datetime.datetime(2023, 1, 1,00,00,00))))

        #Transaction Text generation based on Cluster
        if cluster_type == 'Food':
            trans_text = random.choice(trans_text_food)
            data['Transaction Text'].append(trans_text)
        elif cluster_type == 'Travel':
            trans_text = random.choice(trans_text_travel)
            data['Transaction Text'].append(trans_text)
        elif cluster_type == 'Medical':
            trans_text = random.choice(trans_text_medical)
            data['Transaction Text'].append(trans_text)
        elif cluster_type == 'Credit Repayments':
            trans_text = random.choice(trans_text_loans)
            data['Transaction Text'].append(trans_text)
        elif cluster_type == 'Investments':
            trans_text = random.choice(trans_text_invest)
            data['Transaction Text'].append(trans_text)
        elif cluster_type == 'Salary Credit':
            data['Transaction Text'].append('Salary Credited to Account')
        elif cluster_type == 'Bank Interest':
            data['Transaction Text'].append('Interest Credited to Account')

        #Amount generation based on Transaction Text
        if (cluster_type == 'Food') & ('Family' in trans_text):
            data['Amount'].append(random.randrange(3000,6000))
        elif (cluster_type == 'Food') & ('Family' not in trans_text):
            data['Amount'].append(random.randrange(1000,2000))
        elif (cluster_type == 'Travel') & ('Office' in trans_text):
            data['Amount'].append(random.randrange(500,1000))
        elif (cluster_type == 'Travel') & ('Office' not in trans_text):
            data['Amount'].append(random.randrange(10000,40000))
        elif (cluster_type == 'Medical') & ('Medicine' in trans_text):
            data['Amount'].append(random.randrange(1000,3000))
        elif (cluster_type == 'Medical') & ('Doctor' in trans_text):
            data['Amount'].append(random.randrange(2000,5000))
        elif (cluster_type == 'Medical') & ('Hospital' in trans_text):
            data['Amount'].append(random.randrange(40000,100000))
        elif (cluster_type == 'Credit Repayments') & ('Car' in trans_text):
            data['Amount'].append(random.randrange(5000,round((0.15*prev_user_salary))))
        elif (cluster_type == 'Credit Repayments') & ('Car' not in trans_text):
            data['Amount'].append(random.randrange(15000,round((0.35*prev_user_salary))))
        elif (cluster_type == 'Investments') & ('Fixed' in trans_text):
            data['Amount'].append(random.randrange(10000,round((0.30*prev_user_salary))))
        elif (cluster_type == 'Investments') & ('Fixed' not in trans_text):
            data['Amount'].append(random.randrange(5000,round((0.1*prev_user_salary))))
        elif (cluster_type == 'Salary Credit'):            
            data['Amount'].append(prev_user_salary)                 
        elif (cluster_type == 'Bank Interest'):
            data['Amount'].append(random.randrange(5000,20000))

        #Debit/Credit generation
        if (cluster_type == 'Salary Credit' or cluster_type == 'Bank Interest'):
            data['Debit/Credit'].append('Credit')
        else:
            data['Debit/Credit'].append('Debit')

        df = pd.DataFrame(data)

df.to_csv('C:\\Users\\689867\\OneDrive - Cognizant\\Desktop\\python_new\\TransactionDB_Output1.csv')
print('File generated successfully!!')