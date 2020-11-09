import os
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
