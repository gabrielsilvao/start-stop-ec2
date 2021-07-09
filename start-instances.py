import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
   
    filters = [{
        'Name': 'tag:START',
        'Values': ['EC2']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
    
   
    instances = ec2.instances.filter(Filters=filters)   
    
   
    RunningInstances = [instance.id for instance in instances]
    
 
    print(RunningInstances)

 
    if len(RunningInstances) > 0:
      
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).start()
        print("Startando as instâncias")
    else:
        print("Não foram encontradas instâncias STOPPED")

    return 'Código rodou corretamente'