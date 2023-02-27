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

def parseColumn(line, regex):
    match =  re.search(regex, line)
    if (match):
        column = match.group(0)
        match_number = re.search(regex_number, column)
        return match_number.group(0)
    else:
        return 0

with open(m3u) as m3u:
     line_string_list = m3u.readlines()

for line in line_string_list:
  line_list = []
  line_list.append(line)
  line_list.append(parseColumn(line,regex_section))
  line_list.append(parseColumn(line,regex_topic))
  line_list.append(parseColumn(line,regex_paragraph))
  final_list.append(line_list)
    
df = pd.DataFrame(final_list)
df[1] = df[1].astype(int)
df[2] = df[2].astype(int)
df[3] = df[3].astype(int)
df_sort = df.sort_values(by=[1,2,3])
df_sort = df_sort.reset_index(drop=True)

with open(sorted_m3u, 'w') as m3u_sorted:
    for x in range(len(line_string_list)):
        print((df_sort.at[x,0]).strip('\n'), file=m3u_sorted)
