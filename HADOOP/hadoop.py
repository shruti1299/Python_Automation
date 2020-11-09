import os
while True:
                                 os.system("clear")
                                 os.system("tput setaf 2")
                                 print(""" 
                                 \n
                                 Press 1 : To start name node
                                 press 2 : To stop name node
                                 press 3 : To configure name node
                                 press 4 : To check status
                                 press 5 : To start datanode
                                 press 6 : To stop datanode
                                 press 7 : To exit
                                 press 8 : To return to main menu
                             
                                 
                                 """)
                                 os.system("tput setaf 7")
                                 il = input("enter your choice :")
                                 print(il)
                                 
                                 if int(il) == 1:
                                        os.system("hadoop-daemon.sh start namenode")
                                        print("namenode started successfully")
                                 elif int(il) == 2:
                                        os.system("hadoop-daemon.sh stop namenode")
                                        printf("namenode stopped successfully")
                                 elif int(il) == 3:
                                        ip = input("enter namenode ip :")
                                        os.system("rpm -ivh /root/jdk-8u171-linux-x64.rpm")
                                        os.system("rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")
                                        os.system("touch core-site.xml")
                                        os.system('echo \<?xml version="1.0"?\> >>core-site.xml')
                                        os.system('echo \<?xml-stylesheet type="text\/xsl" href="configuration.xsl"?\> >>core-site.xml')
                                        os.system("echo \<configuration\> >> core-site.xml")
                                        os.system("echo \<property\> >>core-site.xml")
                                        os.system("echo \<name\>fs.default.name\<\/name\> >>core-site.xml")
                                        
                                        os.system("echo \<value\>hdfs://{}:9001\<\/value\> >>core-site.xml".format(ip)) 
                                        os.system("echo \<\/properety\> >>core-site.xml")
                                        os.system("echo \<\/configuration\> >>core-site.xml")
                           
                                        os.system("cp core-site.xml /etc/hadoop/core-site.xml")
                                        os.system("rm core-site.xml")
                                        os.system("tput setaf 3")
                                        print("core-site.xml file is successfully configured")
                                        os.system("tput setaf 7")


                                 elif int(il) == 4:
                                        os.system("hadoop dfsadmin -report")

                                 elif int(il) == 5:
                                        os.system("hadoop-daemon.sh start datanode")
                                        print("datanode started successfully")
                                 elif int(il) == 6:
                                        os.system("hadoop-daemon.sh stop datanode")
                                        print("datanode stopped successfully")
                                 elif int(il) == 7:
                                        exit()
                                 elif int(il) == 8:
                                        break
                                 else :
                                        print("not supported")
                                 input("\n plz enter to continue...")