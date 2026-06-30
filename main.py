import pandas as pd

def calculate_grade(percentage):
    if(100>=percentage>=90):
        return 'A'
    elif(percentage>=80):
        return 'B'
    elif(percentage>=70):
        return 'C'
    elif(percentage>=60):
        return 'D'
    else:
        return 'F'

df = pd.read_csv("students.csv")

df['Total_marks'] = df['Maths']+df['Science']+df['English']
df['Percentage'] = (df['Total_marks']/300)*100
df['Grade'] = df['Percentage'].apply(calculate_grade)
print(df)

topper = df.loc[df['Total_marks']==df['Total_marks'].max()]
print("\n=== Topper ===")
print(f"Name:{topper['Name'].iloc[0]}\nTotal marks:{topper['Total_marks'].iloc[0]}\nPercentage:{topper['Percentage'].iloc[0]:.2f}%")

lowest = df.loc[df['Total_marks']==df['Total_marks'].min()]
print("\n=== Lowest scorer ===")
print(f"Name:{lowest['Name'].iloc[0]}\nTotal marks:{lowest['Total_marks'].iloc[0]}\nPercentage:{lowest['Percentage'].iloc[0]:.2f}%")

average_math = df['Maths'].mean()
average_science = df['Science'].mean()
average_english = df['English'].mean()
print("\n=== Average marks of each subject ===")
print(f"Maths : {average_math}\nScience : {average_science}\nEnglish : {average_english}")

highest_math = df['Maths'].idxmax()
highest_science = df['Science'].idxmax()
highest_english = df['English'].idxmax()
print("\n=== Highest Marks in Each Subject ===")
print(f"Maths -> {df.loc[highest_math,'Name']}({df.loc[highest_math,'Maths']})")
print(f"Science -> {df.loc[highest_science,'Name']}({df.loc[highest_science,'Science']})")
print(f"English -> {df.loc[highest_english,'Name']}({df.loc[highest_english,'English']})")

lowest_math = df['Maths'].idxmin()
lowest_science = df['Science'].idxmin()
lowest_english = df['English'].idxmin()
print("\n=== Lowest Marks in Each Subject ===")
print(f"Maths -> {df.loc[lowest_math,'Name']}({df.loc[lowest_math,'Maths']})")
print(f"Science -> {df.loc[lowest_science,'Name']}({df.loc[lowest_science,'Science']})")
print(f"English -> {df.loc[lowest_english,'Name']}({df.loc[lowest_english,'English']})")

passed_students = df[(df['Maths']>=40) & (df['English']>=40) & (df['Science']>=40)]
print("\n=== Passed Students ===")
print(passed_students)

failed_students = (df[(df['Maths']<40) | (df['English']<40) | (df['Science']<40)])
print("\n=== Failed Students ===")
print(failed_students)

top_3 = df.sort_values('Percentage',ascending=False).head(3)
print("\n=== Top-3 Students ===")
print(top_3)

print("\n=== Students Performance Report ===")
print(f"Total Students : {len(df)}\n")
print(f"Passed Students : {len(passed_students)}\n")
print(f"Failed Students : {len(failed_students)}\n")
print(f"Topper : {topper['Name'].iloc[0]}({topper['Total_marks'].iloc[0]})\n")
print(f"Average Percentage : {df['Percentage'].mean():.2f}%")



