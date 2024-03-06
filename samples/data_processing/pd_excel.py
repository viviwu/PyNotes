# data processing

import pandas as pd

# Replace '登录日志.xlsx' with the actual file path
excel_file_path = r'C:\Users\wuxw\Downloads\登录日志.xlsx'

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Remove duplicates based on the '登录账号' column
df_unique = df.drop_duplicates(subset='登录账号')


# Print the unique data based on '登录账号' column
print("Unique data based on '登录账号' column:")
print(df_unique)

# Save the result to a new Excel file
output_file_path = r'C:\Users\wuxw\Downloads\unique_login_data.xlsx'
df_unique.to_excel(output_file_path, index=False)

print(f"Result saved to {output_file_path}")
