import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the KBO hitter statistics page
url = 'https://www.koreabaseball.com/Record/Player/PitcherBasic/BasicTotal.aspx'

# Send a request to fetch the content of the page
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the hitter statistics
table = soup.find('table', {'class': 'tData'})

# Extract the headers from the table
headers = [header.text.strip() for header in soup.find('thead').find_all('th')]

# Extract the rows from the table
rows = []
for row in soup.find('tbody').find_all('tr'):
    cols = [col.text.strip() for col in row.find_all('td')]
    rows.append(cols)

# Create a DataFrame from the extracted data
df = pd.DataFrame(rows, columns=headers)

# Save the DataFrame to a CSV file
csv_file_path = 'kbo_pitcher_stats.csv'
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

print(f"Data has been saved to {csv_file_path}")
