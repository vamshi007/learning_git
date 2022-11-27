import os
import re
import time
start=time.time()
list_process=['camera.provider','cameraserver','app.camera','snap','singletake']
list_selected_process=[]
list_selected_pids=[]
files_names=[]
overall_result=[]
provider=False
cameraserver=False
appcamera=False
snap=False
singletake=False
with os.popen('adb shell dumpsys meminfo --oom ') as f1:
    meminfo=f1.read()
    meminfo=meminfo.split('\n')
    for j in range(len(list_process)):
        for i in range(0, len(meminfo)):
            meminfo[i] = meminfo[i].strip()
            if list_process[j] in meminfo[i]:
                temp_var=meminfo[i]
                temp_var=temp_var.split(' ')
                if temp_var[1] in list_selected_process:
                    break
                else:
                    list_selected_process.append(temp_var[1])
                    regexr='\d+'
                    camera_pid=re.findall(regexr,temp_var[2]+""+temp_var[3])
                    list_selected_pids.append(camera_pid)

print(list_selected_process)
print(list_selected_pids)


'''
code to create log files for both PSS and ION values
for each preview log are created minimum logs are around 10
'''
data=''
for j in range(10):
    for i in range(len(list_selected_pids)):
        cmd=f'adb shell dumpsys meminfo {list_selected_pids[i][0]} | grep "TOTAL PSS:\|mtrack" '
        data=data+list_selected_process[i]+"\n"
        data=data+os.popen(cmd).read()
        cmd=f'adb shell dmabuf_dump {list_selected_pids[i][0]} | grep "dmabuf total:\|dmabuf info not found"'
        data=data+os.popen(cmd).read()
    file_01=open(f'Iteration{j}.txt','w')
    files_names.append(f'iteration{j}.txt')
    file_01.write(data)
    file_01.close()
    data=''


'''
collecting the data from log files and and formatting them into a list
'''
for i in range(len(files_names)):
    string = open(files_names[i], 'r')
    string_values = string.readlines()
    temp_service=[]
    counter=0
    for i in range(len(string_values)):
        string_values[i] = string_values[i].strip()
        if "camera.provider" in string_values[i]:
            counter=1
            provider = True
            cameraserver = False
            appcamera = False
            snap = False
            singletake = False
            continue
        elif "cameraserver" in string_values[i]:
            counter = 1
            provider = False
            cameraserver = True
            appcamera = False
            snap = False
            singletake = False
            continue
        elif "app.camera" in string_values[i]:
            counter = 1
            provider = False
            cameraserver = False
            appcamera = True
            snap = False
            singletake = False
            continue
        elif "snap" in string_values[i]:
            counter = 1
            provider = False
            cameraserver = False
            appcamera = False
            snap = True
            singletake = False
            continue
        elif "singletake" in string_values[i]:
            counter = 1
            provider = False
            cameraserver = False
            appcamera = False
            snap = False
            singletake = True
            continue

        if provider == True:
            if "EGL mtrack" in string_values[i] or counter == 1:
                if "EGL mtrack" in string_values[i]:
                    temp_local=[]
                    temp_string=string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i]!='':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter=counter+1
                    continue
                else:
                    temp_service.append(0)
                    counter=counter+1

            if "GL mtrack" in string_values[i] or counter==2:
                if "GL mtrack" in string_values[i]:
                    temp_local = []
                    temp_string=string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i]!='':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter=counter+1

            if "Other mtrack" in string_values[i] or counter==3:
                if "Other mtrack" in string_values[i]:
                    temp_local = []
                    temp_string=string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i]!='':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1


            if "TOTAL PSS:" in string_values[i] or counter == 4:
                if "TOTAL PSS:" in string_values[i]:
                    temp_local = []
                    GL_mtrack=0
                    temp_string=string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i]!='':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1


            if "dmabuf total:" in string_values[i] or counter == 5:
                if "dmabuf total:" in string_values[i]:
                    temp_local = []
                    GL_mtrack=0
                    temp_string=string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i]!='':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

        elif cameraserver == True:
            if "EGL mtrack" in string_values[i] or counter == 1:
                if "EGL mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "GL mtrack" in string_values[i] or counter == 2:
                if "GL mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "Other mtrack" in string_values[i] or counter == 3:
                if "Other mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "TOTAL PSS:" in string_values[i] or counter == 4:
                if "TOTAL PSS:" in string_values[i]:
                    temp_local = []
                    GL_mtrack = 0
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "dmabuf total:" in string_values[i] or counter == 5:
                if "dmabuf total:" in string_values[i]:
                    temp_local = []
                    GL_mtrack = 0
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

        elif appcamera == True:
            if "EGL mtrack" in string_values[i] or counter == 1:
                if "EGL mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "GL mtrack" in string_values[i] or counter == 2:
                if "GL mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "Other mtrack" in string_values[i] or counter == 3:
                if "Other mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "TOTAL PSS:" in string_values[i] or counter == 4:
                if "TOTAL PSS:" in string_values[i]:
                    temp_local = []
                    GL_mtrack = 0
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "dmabuf total:" in string_values[i] or counter == 5:
                if "dmabuf total:" in string_values[i]:
                    temp_local = []
                    GL_mtrack = 0
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

        elif snap == True:
            if "EGL mtrack" in string_values[i] or counter == 1:
                if "EGL mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "GL mtrack" in string_values[i] or counter == 2:
                if "GL mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "Other mtrack" in string_values[i] or counter == 3:
                if "Other mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "TOTAL PSS:" in string_values[i] or counter == 4:
                if "TOTAL PSS:" in string_values[i]:
                    temp_local = []
                    GL_mtrack = 0
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "dmabuf total:" in string_values[i] or counter == 5:
                if "dmabuf total:" in string_values[i]:
                    temp_local = []
                    GL_mtrack = 0
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

        elif singletake == True:
            if "EGL mtrack" in string_values[i] or counter == 1:
                if "EGL mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "GL mtrack" in string_values[i] or counter == 2:
                if "GL mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "Other mtrack" in string_values[i] or counter == 3:
                if "Other mtrack" in string_values[i]:
                    temp_local = []
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "TOTAL PSS:" in string_values[i] or counter == 4:
                if "TOTAL PSS:" in string_values[i]:
                    temp_local = []
                    GL_mtrack = 0
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1

            if "dmabuf total:" in string_values[i] or counter == 5:
                if "dmabuf total:" in string_values[i]:
                    temp_local = []
                    GL_mtrack = 0
                    temp_string = string_values[i].split(' ')
                    for i in range(len(temp_string)):
                        if temp_string[i] != '':
                            temp_local.append(temp_string[i])
                    temp_service.append(temp_local[2])
                    counter = counter + 1
                    continue
                else:
                    temp_service.append(0)
                    counter = counter + 1


    overall_result.append(temp_service)
for i in range(len(overall_result)):
    print(overall_result[i],end="\n")


'''
calculation of pss and ion values
'''

for i in range(len( overall_result)):
    for j in range(len( overall_result[i])):
         overall_result[i][j]=int( overall_result[i][j])
results=[]
for i in range(len(overall_result)):
    cnt=0
    final_result = []
    while cnt  < len( overall_result[i]):
        EGL_Mtract= overall_result[i][cnt]
        print(EGL_Mtract,end=" ")
        GL_Mtract= overall_result[i][cnt+1]
        print(GL_Mtract,end=' ')
        Other_Mtract= overall_result[i][cnt+2]
        print(Other_Mtract,end=' ')
        total_mtract=EGL_Mtract+GL_Mtract+Other_Mtract
        PSS= overall_result[i][cnt+3]-total_mtract
        final_result.append(PSS/1024)
        final_result.append(overall_result[i][cnt+4]/1024)
        cnt=cnt+5
    results.append(final_result)

for i in range(len(results)):
    print(results[i])
end=time.time()
print(end-start)







