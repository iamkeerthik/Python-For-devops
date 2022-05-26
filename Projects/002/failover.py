import boto3

region=input("Please enter the region code us-east-1 / eu-west-1 : ")

client = boto3.client('rds', region_name=region)

inputs= ""
while inputs != "exit": 

    print('1 -  DB cluster failover \n')

    print('2 -  global cluster failover \n')

    choice = int(input('Enter your choice: '))

    if (choice == 1):
        DB_Id= input("Please enter DB_Cluster_Identifier : ")
        Target_id= input("Please eneter Target_DB_Instance_Identifier: ")
        response = client.failover_db_cluster(
        DBClusterIdentifier=DB_Id,
        TargetDBInstanceIdentifier=Target_id
    )


    elif (choice == 2):
        DB_Id= input("Please enter  Global_Cluster_Identifier : ")
        Target_id= input("Please eneter Target_DB_Cluster_Identifier: ")
        response = client.failover_global_cluster(
        GlobalClusterIdentifier=DB_Id,
        TargetDbClusterIdentifier=Target_id
    )
 
    else:
        print("invalid choise, try again")