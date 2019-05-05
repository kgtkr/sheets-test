import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('auth.json', scope)
gc = gspread.authorize(credentials)
for sheet in gc.list_spreadsheet_files():
    wks = gc.open(sheet['name']).sheet1

    data=wks.get_all_values()

    s=json.dumps(data)

    with open(f'data/{sheet["name"]}.json', mode='w') as f:
        f.write(s)
