import os
import re
files_names='iteration0.txt'
provider_list=[]
cameraserver_list=[]
appcamera_list=[]
snap_list=[]
singletake_list=[]
provider = False
cameraserver = False
appcamera = False
snap = False
singletake = False

list_files=['Iteration0.txt','Iteration1.txt','Iteration2.txt','Iteration3.txt','Iteration4.txt']
for i in range(len(list_files)):
    string = open(list_files[i], 'r')
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


        else:
            pass




    provider_list=[]
    provider_list.append(temp_service)
    print(provider_list)













