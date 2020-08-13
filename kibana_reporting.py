import json
import time
import datetime
import requests
import subprocess
import google_api_python
host_target_info = []
with open('downloaded_data.json', 'r') as i:
    json_data = i.read()
sheet_name=str(datetime.datetime.now())
print(sheet_name)
data = json.loads(json_data)
data_info = data['aggregations']['2']['buckets']

for i in data_info:
    data2 = i['3']['buckets']
    for k in data2:
        data3 =k['4']['buckets']
        for l in data3:
            list_of_hostnames = l['5']['buckets']
            for hosts in range(len(list_of_hostnames)):
                y = list_of_hostnames[hosts]['doc_count']
                try:
                    p = subprocess.Popen(["nslookup " + list_of_hostnames[hosts]['key']], stdout=subprocess.PIPE,
                                         shell=True)
                    returned_data = p.communicate()[0].decode("utf-8").split("\n")[0].split("=")[1].split(".internal")[
                        0]
                except:
                    pass
                    returned_data = "Not_Found"
                x = (l['key'],list_of_hostnames[hosts]['key'],y , returned_data)
                host_target_info.append(x)
print(host_target_info)

number=0
label= "Machine,IP_used_to_login,number_of_logins_by_IP,hostname"
google_api_python.copy_to_google_sheet(str(label).split(','), index=1)

time.sleep(5)
for names in host_target_info:
    number=number+1
    last=len(host_target_info)
    print(last)
    print("api_number:{}".format(number))
    if (number%30)==0:
        time.sleep(100)
    print(str(names).strip('[]').strip('()').split(','))
    google_api_python.copy_to_google_sheet(str(names).strip('[]').strip('()').split(','), index=number+1)





