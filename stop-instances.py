import boto3


ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    
    filters = [{
        'Name': 'tag:STOP',
        'Values': ['instance']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    
    
    instances = ec2.instances.filter(Filters=filters)   
    
   
    RunningInstances = [instance.id for instance in instances]
    
   
    print(RunningInstances)

    
    if len(RunningInstances) > 0:
        
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
        print("Stoppando as instâncias")
    else:
        print("Não foram encontradas instâncias em RUNNING")

    return 'Comando rodou corretamente!'