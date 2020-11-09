import os 
import getpass

os.system("tput setaf 3")
print("\t\t\t Welcome To my menu ")
os.system("tput setaf 7")
print("\t\t\t --------------- ")


passwd = getpass.getpass("enter ur password :" )

if passwd != "llw":
    print("password incorrect....")
    exit()


r = input("where u want to run this menu ? (local/remote) : ")
print(r)


while True:
       os.system("clear")
       os.system("tput setaf 3")
       print("""
       \n
       press 0 : To clear cache
       Press 1 : To run date
       press 2 : To cal 
       press 3 : To reboot
       press 4 : For docker functionalities
       press 5 : For Hadoop 
       press 6 : To create partition/info about disks
       press 7 : LVM
       press 8 : To configure web server
       press 9 : For AWS functionalities
       press 10 :To exit
       """)
       os.system("tput setaf 7")

       ch = input("enter your choice :")
       print(ch)
 
       if r == "local":
                if int(ch) == 0:
                        os.system("echo 3 > /proc/sys/vm/drop_caches")
                        os.system("free -m")
                elif int(ch) == 1:
                        os.system("date")
                elif int(ch) == 2:
                        os.system("cal")
                elif int(ch) == 3:
                        os.system("reboot")
                elif int(ch) == 4:
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

                elif int(ch) == 5:
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
                                

                elif int(ch) == 6:
                     while True:    
                         os.system("clear")
                         os.system("tput setaf 4")
                         print( """
                         \n
                          Press 1 : To partition
                          press 2 : To show all the available partitions
                          press 3 : To show detailed info about all the disks
                          press 4 : To exit
                          press 5 : To return to main menu
                         
                          """)
                         inn=input("enter your choice.... :")
                         if int(inn) == 1:
          
                               disk=input("enter the disk name : ")
                               os.system("fdisk {}".format(disk))
                               os.system("udevadm settle")
                               no=input("enter the partition number :")
                               os.system("mkfs.ext4 {}{}".format(disk,int(no)))
                               fil=input("enter file name to mount this partition? :") 
                               os.system("mount {} {}".format(disk,fil)) 
                               print("partition is created successfully.......")

                         elif int(inn) == 2:
                              os.system("lsblk")

                         elif int(inn) == 3:
                              os.system("fdisk-l")

                         elif int(inn) == 4:
                              exit()
                         elif int(inn) == 5:
                              break

                         else :
                              print("not supported")
                              continue

                elif int(ch) == 7:
                     while True:
                         os.system("clear")
                         os.system("tput setaf 2")
                         print( """
                         \n
                          Press 1 : To create Physical Volume
                          press 2 : To create Volume Group
                          press 3 : To create logical volume from volume group
                          press 4 : To extend the size of volume     group                          
                          press 5 : To exit
                          press 6 : To return to main menu
  
                          """)
                         os.system("tput setaf 7")
                         chh=input("enter your choice.... :")

                         if int(chh) == 1:
                                nos=int(input("How many physical volume would u like to create ?: "))
                                for i in range(0,nos):
                                         pv=input("enter disk name for Pysical Volume :")
                                         os.system("pvcreate {}".format(pv))
                                         os.system("pvdisplay {}".format(pv))

                         elif int(chh) == 2:

                                  nvg = input("enter the the name of Volume group :")
                                  t=int(input("How many physical volume would u like to add in this V.G ?: "))       
                                  for p in range(0,t):
                                           pvv=input("enter the name of  physical vol you want to add :")
                                           os.system("vgcreate {} {}".format(nvg,pvv))
                                           os.system("vgdisplay {}".format(nvg))
                                  print("Volume Group created successfully")

                         elif int(chh) == 3:
                                  size = input("enter the size of logical volume :")
                                  lv = input("enter the name of the lv you whould like to create :")
                           
                                  vn = input("enter the name of  volume group   :")
                                  os.system("lvcreate --size {} --name {} {}".format(size,lv,vn)) 
                                  os.system("lvdisplay {}/{}".format(vn,lv))

                                  print("lv created successfully....")

                                  input("\n enter to format this partition")

                                  os.system("mkfs.ext4  /dev/{}/{}".format(vn,lv))

                                  print("partition created successfully")

                                  input("\n enter to mount this partition")

                                  fn = input("enter the name of the folder you would like to mount into : ")
                                  os.system("mount /dev{}/{}  /{}".format(vn,lv,fn))


                         
                         elif int(chh) == 4:

                                  lvv = input("enter the name of LV you want to extend : ")
                                  ex = input("enter the size of logical volume you want to extend : ")
                                  os.system("lvextend --size +{} {}".format(ex,lvv))

                                  input("\n enter to format the extended partition ")

                                  os.system("resize2fs {}".format(lvv))

                         elif int(chh) == 5:
                                  exit()
                         elif int(chh) == 6:
                                  break 
                        
                         else:
                                  print("not supported")
                                  continue
                         input("\n plz enter to continue..")

                elif int(ch) == 8:
                         os.system("yum install httpd -y")
                         os.system("systemctl start httpd")
                         os.system("systemctl enable httpd")
                         os.system("cp index.html /var/www/html")

                elif int(ch) == 9:
                     while True:
                         os.system("clear")
                         os.system("tput setaf 2")
                         print( """
                         \n
                          Press 1 : To create key-pair
                          press 2 : To delete key pair
                          press 3 : To create security group
                          press 4 : To add ingress security rules for existing security group
                          press 5 : To launch instance
                          press 6 : To start existing instance
                          press 7 : To stop existing instance
                          press 8 : To terminate ec2 instance
                          press 9 : To describe EBS
                          press 10 : To create EBS volume
                          press 11 : To attach EBS volume
                          press 12 : To detach EBS volume
                          press 13 : To delete EBS volume
                          press 14 : To exit
                          press 15 : To return to the main menu
                          """)
                         os.system("tput setaf 7")
                         ch9 =input("enter your choice :")
                         if int(ch9) == 1:
                               keyn =input("enter key name to create") 
                               os.system('aws ec2 create-key-pair --key-name {}'.format(keyn)) 
                               print("key created successfully")
                         elif int(ch9) == 2: 
                               keyn =input("enter key name to delete")
                               os.system('aws ec2 delete-key-pair --key-name {}'.format(keyn))
                        
                         elif int(ch9) == 3:
                               sg = input("enter security group name")
                               os.system('aws ec2 create-security-group --group-name {} --description "SG Created" '.format(sg))
                       
                         elif int(ch9) == 4:
                               sgi = input("enter security group id")
                               os.system('aws ec2 authorize-security-group-ingress --group-id {} --ip-permissions IpProtocol=tcp,FromPort=22,ToPort=22,IpRanges=[{CidrIp=0.0.0.0/0}]'.format(sgi))
                               os.system('aws ec2 authorize-security-group-ingress --group-id {} --ip-permissions IpProtocol=tcp,FromPort=22,ToPort=22,IpRanges=[{CidrIp=0.0.0.0/0}]'.format(sgi))
                         
                         elif int(ch9) == 5:
                               aid = input("enter AMI_id:")
                               it  = input("enter instance type:")
                               n   = int(input("enter number of instances you want to launch:"))
                               s   = input("enter subnet id :")
                               sg  = input("enter sucurity group:")
                               k   = input("enter key name:")
                               os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}'.format(aid,it,n,s,sg,k))
                               print("OS launched successfully...")
         
                  
                         elif int(ch9) == 6 :
                               aid = input("enter AMI_id:")
                               os.system('aws ec2 start-instances --instance-ids {}'.format(aid))
                         elif int(ch9) == 7 :
                               aid = input("enter AMI_id:")
                               os.system('aws ec2 stop-instances --instance-ids {}'.format(aid))
                               print("intance stopped successfully")
                         elif int(ch9) == 8 :
                               aid = input("enter AMI_id:")
                               os.system('aws ec2 terminate-instances --instance-ids {}'.format(aid))
                               print("instance terminated successfully")
                         elif int(ch9) == 9 :
                               os.system('aws ec2 describe-volumes')
                         elif int(ch9) == 10 :
                                vt = input("enter volume type eg. gp2:")
                                s  = input("enter volume size:")
                                a  = input("enter availability zone eg. ap-south-1a: ")
                                os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(vt,s,a))
                                print("volume created successfully")

                         elif int(ch9) == 11:
                               aid = input("enter instance id:")
                               vid = input("enter volume id :")
                               dn  = input("enter device name :")
                               os.system('aws ec2 attach-volume --instance-id {} --volume-id {} --device {}'.format(aid,vid,dn))
                               print("ebs volume added successfully")

                         elif int(ch9) == 12:
                               vid = input("enter volume id :")
                               os.system('aws ec2 detach-volume  --volume-id {}'.format(aid,vid,dn))
                         elif int(ch9) == 13:
                               vid = input("enter volume id:")
                               os.system('aws ec2 delete-volume --volume-id {}'.format(vid))             
                         elif int(ch9) == 14 :
                                exit()
              
                         elif int(ch9) == 15 :
                                break
                         else :
                                print("not supported ")
                                continue

                        
                         input("\n plz enter to continue ....")
    

                elif int(ch) == 10:
                        exit()


                else:
                        print("not supported")


       elif r == "remote":
                ip = input("enter remote ip:")
                print(ip)


                if int(ch) == 1:
                        os.system("ssh  {} date".format(ip))


                elif int(ch) == 2:
                        os.system("ssh  {} cal".format(ip))
                elif int(ch) == 3:
                        os.system("ssh  {} reboot".format(ip))
                elif int(ch) == 8:
                        os.system("ssh  {} yum install httpd -y".format(ip))
                        os.system("ssh  {} systemctl start httpd".format(ip))
                        os.system("ssh  {} systemctl enable httpd".format(ip))
                        os.system("scp index.html {}: /var/www/html".format(ip))
                
                else:
                        print("not supported")
       else: 
                print("not supported login...")
       input("\n plz enter to continue ....")
                

