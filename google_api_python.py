import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from pprint import pprint
import epoch_converter
import sys

name=epoch_converter.Name
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
try:
    sheet = client.open("Admin_data").sheet1# Open the spreadhseet
    sheet1 = client.open("Admin_data").add_worksheet(title=name,rows=0,cols=0)
    data = sheet.get_all_records() # Get a list of all records
    print(data)
except:
    pass
    print("We think, already there is a sheet with name \"{}\" present. Please check that.".format(name))
    sys.exit()


def copy_to_google_sheet(row, index):
    sheet1.insert_row(row, index)
    print(row)
