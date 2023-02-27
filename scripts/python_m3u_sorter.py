import pandas as pd
import re

m3u = input("Enter the input file name: ")
sorted_m3u = input("Enter the output file name: ")

# m3u = '23_oct_65_ss_chaos.m3u'
# sorted_m3u = '23_oct_65_ss_chaos_sorted.m3u'

regex_section = "section_\d{1,3}_"
regex_topic = "topic_\d{1,3}"
regex_paragraph = "para_\d{1,3}"
regex_number = "\d{1,3}"

final_list = []

def parseSection(line):
    match =  re.search(regex_section, line)
    if (match):
        section = match.group(0)
        match_number = re.search(regex_number, section)
        return match_number.group(0)
    else:
        return 0

def parseTopic(line):
    match =  re.search(regex_topic, line)
    if (match):
        topic = match.group(0)
        match_number = re.search(regex_number, topic)
        return match_number.group(0)
    else:
        return 0

def parsePara(line):
    match =  re.search(regex_paragraph, line)
    if (match):
        para = match.group(0)
        match_number = re.search(regex_number, para)
        return match_number.group(0)
    else:
        return 0

with open(m3u) as m3u:
     line_string_list = m3u.readlines()

for line in line_string_list:
  line_list = []
  line_list.append(line)
  line_list.append(parseSection(line))
  line_list.append(parseTopic(line))
  line_list.append(parsePara(line))
  final_list.append(line_list)
    
df = pd.DataFrame(final_list)
df[1] = df[1].astype(int)
df[2] = df[2].astype(int)
df[3] = df[3].astype(int)
df_sort = df.sort_values(by=[1,2,3])
df_sort = df_sort.reset_index(drop=True)



with open(sorted_m3u, 'w') as m3u_sorted:
    for x in range(len(line_string_list)):
        print(df_sort.at[x,0], file=m3u_sorted)

# print(df_sort)
# print(df_sort[0])
