# Test exercises here
import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    return pd.read_csv(file)

def exercise_1(df):
    return df.columns.tolist()

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(n=k)
def exercise_4(df):
    return df['type'].unique().tolist()

def exercise_5(df):
    return df['nameDest'].value_counts().head(10)

def exercise_6(df):
    return df[df['isFraud'] == 1]
df = exercise_0('transactions.csv')
print(exercise_1(df))
print("\n")
print("\n")
print(exercise_2(df,4))
print("\n")
print("\n")
print(exercise_3(df,5))
print("\n")
print("\n")
print(exercise_4(df))
print("\n")
print("\n")
print(exercise_5(df))
print("\n")
print("\n")
print(exercise_6(df))
print("\n")
print("\n")



transaction_type_counts = df['type'].value_counts()

plt.bar(transaction_type_counts.index, transaction_type_counts.values)
plt.xlabel('Transaction Types')
plt.ylabel('Count')
plt.title('Transaction Types Bar Chart')
plt.xticks(rotation=90)
plt.show()



fraud_transaction_counts = df[df['isFraud'] == 1]['type'].value_counts()
legitimate_transaction_counts = df[df['isFraud'] == 0]['type'].value_counts()


fraud_transaction_counts = fraud_transaction_counts.reindex(legitimate_transaction_counts.index, fill_value=0)

fig, ax = plt.subplots()
width = 0.4
x = range(len(fraud_transaction_counts))

ax.bar(x, fraud_transaction_counts.values, width, label='Fraud')
ax.bar([i + width for i in x], legitimate_transaction_counts.values, width, label='Legitimate')

ax.set_xlabel('Transaction Types')
ax.set_ylabel('Count')
ax.set_title('Transaction Types Split by Fraud Bar Chart')
ax.set_xticks([i + width/2 for i in x])
ax.set_xticklabels(fraud_transaction_counts.index, rotation=90)
ax.legend()

plt.show()





cash_out_transactions = df[df['type'] == 'CASH_OUT']

plt.scatter(cash_out_transactions['newbalanceOrig'] - cash_out_transactions['oldbalanceOrg'],cash_out_transactions['newbalanceDest'] - cash_out_transactions['oldbalanceDest'])
plt.xlabel('Origin Account Balance Delta')
plt.ylabel('Destination Account Balance Delta')
plt.title('Origin Account Balance Delta v. Destination Account Balance Delta (Cash Out)')
plt.show()
