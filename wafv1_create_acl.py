import boto3
import time

#Getting Token

client_waf = boto3.client('waf')

def get_change_token():
    return client_waf.get_change_token()['ChangeToken']

#Creating new custom WebACL


print(' WAF Classic Helper: Create Custom WebACL')
print('...')
time.sleep(2)
waf_name = input('ACL Name:')
print('')
time.sleep(1)
waf_metric = input('Metric Name:')
print('')
time.sleep(1)
waf_default = input('Default Action (BLOCK, ALLOW or COUNT):')
print('')
time.sleep(1)

print('WAF ACL creating with default base settings...')

response_waf_create = client_waf.create_web_acl(
    Name=waf_name,
    MetricName=waf_metric,
    DefaultAction={
        'Type': waf_default
    },
    ChangeToken=get_change_token()
)

time.sleep(1)

if response_waf_create['ResponseMetadata']['HTTPStatusCode'] == 200:
    print('Success')
else:
    print(response_waf_create)
