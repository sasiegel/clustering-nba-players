from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd

SAVE_PATH = 'C:/Projects/CS6140/nba_clustering/data/'
f = open('nba_urls.txt', 'r')
#  Begin (again) here
line = f.readline()
parameters = line.split()

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#  Scrape data from NBA.com into list of strings where string is row of data 
url = parameters[0]
Xpaths = parameters[1:]

path_to_chromedriver = 'C:/Program Files (x86)/Google/Chrome/bin/chromedriver.exe' # Path to access a chrome driver
driver = webdriver.Chrome(executable_path=path_to_chromedriver)
driver.get(url)

"""To make changes on the NBA menu you need to find the Xpath to the element 
(drop-down) that you want to change.
"""
wait = WebDriverWait(driver, 10)

for path in Xpaths:
    dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, path)))
    dropdown.click()

select_all_xpath = '/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/select/option[1]'
select_all = wait.until(EC.visibility_of_element_located((By.XPATH, select_all_xpath)))
select_all.click()

table = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'nba-stat-table__overflow')))
table = driver.find_element_by_class_name('nba-stat-table__overflow')
raw_data = table.text
row_data = raw_data.splitlines()

driver.quit()

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#  Get pandas Dataframe from row data (list of strings)
print(row_data[:13])
start_idx = 12
row_data_ = row_data[start_idx:]
m = 2  # items per row
data = []
for i in range(int(len(row_data_)/m)):
    row = [row_data_[m*i]]  # Player name
    split_vals = row_data_[m*i+1].split(' ')  # Player Stats
    row.extend(split_vals)
    data.append(row)
df = pd.DataFrame(data)

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#  Get list of headers from row data (list of strings)
rows_with_headers = [0]
headers = []
for i in rows_with_headers:
    headers.append(row_data[i])
headers = headers[0].split(' ')

df.columns = headers
df = df.set_index('PLAYER')

df = df.loc[:,['TOUCHES', 'FRONT CT TOUCHES', 'TIME OF POSS', 'AVG SEC/TOUCH', 'AVG DRIB/TOUCH', 'ELBOW TOUCHES', 'POST UPS', 'PAINT TOUCHES']]
df = df[np.invert(df.index.duplicated())]
df.to_csv(SAVE_PATH + 'bios.csv')
df = df.rename(columns={'FREQ':'POST-UP %'})

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#  Master pandas dataframe
master = pd.concat([master, df], axis=1)
