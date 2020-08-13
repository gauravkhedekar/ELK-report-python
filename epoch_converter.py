import datetime
import calendar, time
import subprocess

print("startdt_epoch ie lte_new",calendar.timegm(time.strptime(datetime.datetime.now().strftime("%Y-%m-%d")+' 00:00:00','%Y-%m-%d %H:%M:%S'))*1000)
lte_n=calendar.timegm(time.strptime(datetime.datetime.now().strftime("%Y-%m-%d")+' 00:00:00','%Y-%m-%d %H:%M:%S'))*1000
print(lte_n)

start_date = (calendar.timegm(time.strptime(datetime.datetime.now().strftime("%Y-%m-%d")+' 00:00:00','%Y-%m-%d %H:%M:%S'))*1000)-604799999
print("end dt epoch ie gte_new" ,start_date)

gte_n=calendar.timegm(time.strptime(datetime.datetime.now().strftime("%Y-%m-%d")+' 00:00:00','%Y-%m-%d %H:%M:%S'))*1000-604799999
print(gte_n)

#subprocess.Popen(["/bin/sh replace.sh"],"abc","dcs",stdout=subprocess.PIPE)

#subprocess.Popen(["sed", "-i \"s/`less test2.sh| grep -w \"gte\"|awk {'print $2'}`/from_python_change,/\" test2.sh"],stdout=subprocess.PIPE)
print(calendar.day_name)

x = datetime.datetime.now()
print(x.strftime("%b"))

s, ms = divmod(start_date , 1000)
start_date = '%s.%03d' % (time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(s)), ms)
print(start_date)
lte_new = str(datetime.datetime.now().strftime("%Y-%m-%d").split("-")[2])
gte_new = str(start_date.split("-")[2][0:2])
print("{0} -{1} {2}".format(gte_new ,lte_new,x.strftime("%b")))
Name = gte_new + "-" + lte_new + " " + x.strftime("%b")
print(type(Name))


