import os

while True: 
                         os.system("clear")
                         os.system("tput setaf 4")
                         print("""
                         
                         Press 1 : To start docker
                         press 2 : To start the closed OS
                         press 3 : To get inside the OS terminal
                         press 4 : To launch new OS
                         press 5 : To delete OS
                         press 6 : To show present images
                         press 7 : To remove image
                         press 8 : To download new image
                         press 9 : To show all the running OS 
                         press 10 : To see the process going inside the other OS from base OS
                         press 11 : To configure web server on the top of docker
                         press 12 : To exit
                         press 13 : To return to the main menu 
                         """)
                         os.system("tput setaf 7")
                         ch4= input("enter your choice :")
                         print(ch4)
                         if int(ch4) == 1 :
                                os.system("systemctl start docker")
                                print("docker has been started successfully")
                         elif int(ch4) == 2 :
                                osname = input("Please enter OS name :")
                                os.system("systemctl start docker")
                                os.system("docker start {}".format(osname))
                                print("your OS has been started successfully")
                         elif int(ch4) == 3 :
                                osname = input("please enter OS name :")
                                os.system("systemctl start docker")
                                os.system("docker start {}".format(osname)) 
                                os.system("docker attach {}".format(osname))
                         elif int(ch4) == 4 :
                                iname = input("enter image name :")
                                osname = input("enter OS name :")
                                os.system("systemctl start docker") 
                                os.system("docker run -it --name {} {}".format(osname,iname))
                         elif int(ch4) == 5 :
                                osname = input("enter OS name :")
                                os.system("systemctl start docker")
                                os.system("docker rm {}".format(osname))
                                os.system("docker ps -a")
                                print("OS deleted successfully.....")
                      
                         elif int(ch4) == 6 :
                                os.system("systemctl start docker")
                                os.system("docker images")

                         elif int(ch4) == 7 :
                                os.system("systemctl start docker")
                                os.system("docker images")
                                iname = input("enter image name :")
                                os.system("docker -rmi {} -f".format(iname))
                                os.system("docker images")
                                print("image deleted successfully")

                         elif int(ch4) == 8 :
                                os.system("systemctl start docker")
                                iname = input("enter image name :")
                                os.system("docker pull {}".format(inmae))
                                print("image downloaded successfully")
                         elif int(ch4) == 9 :
                                os.system("systemctl start docker")
                                os.system("docker ps")
                         elif int(ch4) == 10:
                                os.system("systemctl start docker")
                                osname = input("enter OS name :")
                                os.system("docker logs {}".format(osname))
                         elif int(ch4) == 11 :
                                os.system("systemctl start firewalld")
                                os.system("systemctl stop firewalld")
                                os.system("systemctl disable firewalld")
                                os.system("systemctl restart docker")
                                osname=("enter OS name :")
                                os.system("docker start {}".format(osname))
                                os.system("yum install httpd")
                                os.system("/usr/sbin/httpd")
                                os.system("docker cp  index.html {}:/root".format(osname))
                        
                         elif int(ch4) == 12 :
                                exit()
              
                         elif int(ch4) == 13 :
                                break
                         else :
                                print("not supported ")
                                continue

                        
                         input("\n plz enter to continue ....")