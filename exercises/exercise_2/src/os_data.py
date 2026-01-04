import sys
import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('src/athlete_events.csv')
    print("CSV loaded successfully")
except FileNotFoundError:
    print("Error: Could not find athlete_events.csv in src/ folder.")
    sys.exit()

print("-" * 30)
print("DATA HEAD:")
print(df.head())
print("-" * 30)

if 'Age' in df.columns:
    df.hist(column='Age', bins=20, color='skyblue', edgecolor='black')
    plt.title('Age distribution of Athletes')
    plt.xlabel('Age')
    plt.ylabel('Frequency')

    output_path = 'src/age_plot.png'
    plt.savefig(output_path)
    print(f"Graph saved to {output_path}")
else:
    print("Column 'Age' not found in dataset.")