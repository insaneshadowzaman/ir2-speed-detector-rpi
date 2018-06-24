from zeep import Client

url = 'https://api2.onnorokomsms.com/sendsms.asmx?WSDL'
client = Client(url)

userName = '01676409085'
password = '27968'
recipientNumber = '01676409085'
smsText = 'Sms Check'
smsType = 'TEXT'

maskName = ''
campaignName = ''

client.service.OneToOne(userName,password,recipientNumber,smsText,smsType,maskName,campaignName)

