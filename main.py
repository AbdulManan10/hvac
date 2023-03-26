from hvac import Client

client = Client(
    url='https://vault-cluster-public-vault-388d931b.043735e3.z1.hashicorp.cloud:8200',
    namespace='admin',
    verify=False
)


client.auth.approle.login(
    role_id='dc1922ba-d452-5672-9c12-eb7b5442c099',
    secret_id='1f9960f4-cebc-babd-b50a-de6a88a41d1f'
)

secret = client.read('secret/data/ingestion/dev/auth/decentraland')
print(secret)


