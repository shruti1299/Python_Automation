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

                         input("click enter to continue")