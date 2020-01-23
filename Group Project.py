from urllib import request
import urllib
from bs4 import BeautifulSoup
import re
from xlwt import Workbook

# default path C://Users//15659//Desktop
wb_Job_des = Workbook()
wb_database = Workbook()
sheet_des = wb_Job_des.add_sheet("Job_description")
sheet_data = wb_database.add_sheet("Specific data")
test_counter = 0


main_url = "https://www.indeed.com/"
data_scientist_url = "https://www.indeed.com/jobs?q=data+scientist&l=California&start="
page_number = 500
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
position_url_list = []
for page in range(0, page_number, 10):
    data_scientist_url += str(page)
    request_info = request.Request(analyst_url, headers=headers)
    response = request.urlopen(request_info)
    html = response.read().decode('utf-8')
    html_soup = BeautifulSoup(html, 'html.parser')
    # To get the position URL
    position_resource = html_soup.findAll(href=re.compile('/pagead/'))
    for each_url in position_resource:
        position_url_list.append(each_url['href'])
# print(position_url_list)
print("grab %d webs done, it's processing to find target information to database" % len(position_url_list))
# print(len(position_url_list))
'''
for titles in bs.find_all('a'):
    print (titles.get('title'))
'''


tools = ["Excel", "Python", "SQL", "SPSS", "R", "Java", "Scala", "C/C++", "Hadoop", "AWS", "SAS", "Linux", "Hive", "Matlab", "Tableau"]

skills = ["machine learning", "data mining", "data analysis", "data visualization", "modeling", "statistics", "communication skills"]

degree = ['no degree', "master's", "bachelor's", 'phd', 'high school']

majors = ['computer science', 'information system', 'mathematics', 'economics', 'statistics', 'quantitative',
          'analytics', 'data science']


data_holders = []
requirement_text_list = []  # To create a array to store the information of requirements
# data_analysts = html_soup.findAll(title=re.compile("Analyst"))

# To open every position URL to extract data

print("Start to grab the web content...")

try:
    for index in range(0, len(position_url_list)):
        position_url = main_url + position_url_list[index]
    # open position URL
        request_position = request.Request(position_url, headers=headers)
        response_position = request.urlopen(request_position)
        position_html = response_position.read().decode('utf-8')
        position_soup = BeautifulSoup(position_html, 'html.parser')
        requirements = position_soup.findAll('div', {"class": "jobsearch-jobDescriptionText"})
        for requirement in requirements:
            requirement_text_list.append(requirement.getText())
        test_counter += 1
        print("Done %d" % test_counter)
        # print("-------------------------------")
except:
   print("Error to open web..")

print("Done. Start to insert value into Excel file")
#print("the number in requirement text list: %d" % len(requirement_text_list))
count_excel = 0
count_python = 0
count_sql = 0
count_spss = 0
count_r = 0
count_java = 0
count_scala = 0
count_c = 0
count_hadoop = 0
count_aws = 0
count_sas = 0
count_linux = 0
count_hive = 0
count_matlab = 0
count_tableau = 0
count_ml = 0
count_data_mining = 0
count_data_analysis = 0
count_data_visuli = 0
count_modeling = 0
count_stat = 0
count_communication = 0
count_nd = 0
count_master = 0
count_bachelor = 0
count_phd = 0
count_high_sch = 0
count_cs = 0
count_is = 0
count_math = 0
count_econ = 0
count_engineer = 0
count_quanta = 0
count_data_ana = 0
count_data_science = 0

# Store the data into excel file
for row in range(0, len(requirement_text_list)):
    for column in range(0, 1):
        sheet_des.write(row, column, requirement_text_list[row])
wb_Job_des.save("C://Users//15659//Desktop//Description.xls")


for index_require in range(0, len(requirement_text_list)):  # These are attributes and we can store the result as True or False into array
    for index_tools in range(0, len(tools)):
        if requirement_text_list[index_require].find(tools[index_tools]) is not -1:
            if index_tools is 0:
                count_excel += 1
            elif index_tools is 1:
                count_python += 1
            elif index_tools is 2:
                count_sql += 1
            elif index_tools is 3:
                count_spss += 1
            elif index_tools is 4:
                count_r += 1
            elif index_tools is 5:
                count_java += 1
            elif index_tools is 6:
                count_scala += 1
            elif index_tools is 7:
                count_c += 1
            elif index_tools is 8:
                count_hadoop += 1
            elif index_tools is 9:
                count_aws += 1
            elif index_tools is 10:
                count_linux += 1
            elif index_tools is 11:
                count_hive += 1
            elif index_tools is 12:
                count_matlab += 1
            elif index_tools is 13:
                count_tableau += 1
    requirement_text_list[index_require] = requirement_text_list[index_require].lower()
    for index_skills in range(0, len(skills)):
        if requirement_text_list[index_require].find(skills[index_skills]) is not -1:
            if index_skills is 0:
                count_ml += 1
            elif index_skills is 1:
                count_data_mining += 1
            elif index_skills is 2:
                count_data_analysis += 1
            elif index_skills is 3:
                count_data_visuli += 1
            elif index_skills is 4:
                count_modeling += 1
            elif index_skills is 5:
                count_stat += 1
            elif index_skills is 6:
                count_communication += 1
    for index_degree in range(0, len(degree)):
        if requirement_text_list[index_require].find(degree[index_degree]) is not -1:
            if index_degree is 0:
                count_nd += 1
            elif index_degree is 1:
                count_master += 1
            elif index_degree is 2:
                count_bachelor += 1
            elif index_degree is 3:
                count_phd += 1
            elif index_degree is 4:
                count_high_sch += 1
    for index_major in range(0, len(majors)):
        if requirement_text_list[index_require].find(majors[index_major]) is not -1:
            if index_major is 0:
                count_cs += 1
            elif index_major is 1:
                count_is += 1
            elif index_major is 2:
                count_math += 1
            elif index_major is 3:
                count_econ += 1
            elif index_major is 4:
                count_engineer += 1
            elif index_major is 5:
                count_quanta += 1
            elif index_major is 6:
                count_data_ana += 1
            elif index_major is 7:
                count_data_science += 1
    data_holders.append(count_excel)
    data_holders.append(count_python)
    data_holders.append(count_sql)
    data_holders.append(count_spss)
    data_holders.append(count_r)
    data_holders.append(count_java)
    data_holders.append(count_scala)
    data_holders.append(count_c)
    data_holders.append(count_hadoop)
    data_holders.append(count_aws)
    data_holders.append(count_linux)
    data_holders.append(count_hive)
    data_holders.append(count_matlab)
    data_holders.append(count_tableau)
    data_holders.append(count_ml)
    data_holders.append(count_data_mining)
    data_holders.append(count_data_analysis)
    data_holders.append(count_data_visuli)
    data_holders.append(count_modeling)
    data_holders.append(count_stat)
    data_holders.append(count_communication)
    data_holders.append(count_nd)
    data_holders.append(count_master)
    data_holders.append(count_bachelor)
    data_holders.append(count_phd)
    data_holders.append(count_high_sch)
    data_holders.append(count_cs)
    data_holders.append(count_is)
    data_holders.append(count_math)
    data_holders.append(count_econ)
    data_holders.append(count_engineer)
    data_holders.append(count_quanta)
    data_holders.append(count_data_ana)
    data_holders.append(count_data_science)

    print("tools: ")
    print(count_excel, count_python, count_sql, count_spss, count_r, count_java, count_scala, count_c, count_hadoop,
          count_aws, count_linux, count_hive, count_matlab, count_tableau)
    print("skills: ")
    print(count_ml, count_data_mining, count_data_analysis, count_data_visuli, count_modeling, count_stat, count_communication)
    print("Degree: ")
    print(count_nd, count_master, count_bachelor, count_phd, count_high_sch)
    print("majors: ")
    print(count_cs, count_is, count_math, count_econ, count_engineer, count_quanta, count_data_ana, count_data_science )

    # insert and save data into excel file
    for column_data in range(0, len(data_holders)):
        sheet_data.write(index_require, column_data, data_holders[column_data])
    print(data_holders)

    # tools default
    count_excel = 0
    count_python = 0
    count_sql = 0
    count_spss = 0
    count_r = 0
    count_java = 0
    count_scala = 0
    count_c = 0
    count_hadoop = 0
    count_aws = 0
    count_sas = 0
    count_linux = 0
    count_hive = 0
    count_matlab = 0
    count_tableau = 0
    # skills default
    count_ml = 0
    count_data_mining = 0
    count_data_analysis = 0
    count_data_visuli = 0
    count_modeling = 0
    count_stat = 0
    count_communication = 0
    # degree default
    count_nd = 0
    count_master = 0
    count_bachelor = 0
    count_phd = 0
    count_high_sch = 0
    # major default
    count_cs = 0
    count_is = 0
    count_math = 0
    count_econ = 0
    count_engineer = 0
    count_quanta = 0
    count_data_ana = 0
    count_data_science = 0
    data_holders = []

wb_database.save("C://Users//15659//Desktop//data.xls")

# print(count_nd, count_master, count_bachelor, count_phd, count_high_sch)






