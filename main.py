from hvac import Client

client = Client(
    url='Your-Cluster-URL',
    namespace='admin',
    verify=False
)


client.auth.approle.login(
    role_id='Your-Role-Id',
    secret_id='Your-Secret-Id'
)

secret = client.read('Your-Secret-Path')
print(secret)


