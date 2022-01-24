# Python program to store data in Excel File

import pandas as pd

marks_data = pd.DataFrame{['ID':{0:23},
                      'Name' : {0:'Siddharth'},
                      'Marks':{0:89},
                      'Grade':{0:'D'}
                    ])

file_name = 'MarksData.xlsx'
marks_data.to_excel(file_name)

print("DataFrame is written to Excel successfully...!")
