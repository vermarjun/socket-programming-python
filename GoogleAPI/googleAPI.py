import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

file = os.getcwd()
file = file+""
print(file)

# Define the scope and credentials for accessing Google Sheets API
scope = []
credentials_json = {
    # google api creds
}
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_json, scope)

# Authenticate with Google Sheets API
gc = gspread.authorize(credentials)

# Open the spreadsheet (by title or URL)
spreadsheet_url = ""
# or spreadsheet_title = 'YOUR_SPREADSHEET_TITLE_HERE'
# spreadsheet = gc.open(spreadsheet_title)

spreadsheet = gc.open_by_url(spreadsheet_url)

# Select the worksheet you want to read from
worksheet = spreadsheet.sheet1  # Assuming you're reading from the first worksheet

# Read data from the worksheet
new_row_values = ["New Value 1", "New Value 2", "New Value 3"]
worksheet.append_row(new_row_values)
data = worksheet.get_all_values()

# Print the read data
for row in data:
    print(row)
