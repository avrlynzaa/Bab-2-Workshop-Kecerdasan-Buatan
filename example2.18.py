# Example 2.18
# Jalankan di Terminal bila belum terpasang:
# /opt/homebrew/bin/python3.11 -m pip install XlsxWriter

import pandas as pd

data = {
    'Name': ['Tony', 'Robert', 'John', 'Alice'],
    'Age': [18, 24, 19, 21],
}

df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

writer = pd.ExcelWriter("test.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="Sheet1", index=False)
writer.close()