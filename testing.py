import requests

print('Testing this URL : http://localhost:5500/api/send-otp' )

obj = {'phone' : '9429653848' }
x = requests.get('http://localhost:5500/api/send-otp',json=obj, headers={"Content-Type":"application/json"})
assert 200 != x.status_code
print('Response Status : '  + str(x.status_code))


print('Testing this URL : http://localhost:5500/api/verify-otp' )

myobj = {'phone': '9429653848', 'otp' : '2024', 'hash' : 'f7d12afa2b335606f7727dcaeb9cd7a668ea03f0016a4f3ac5216f93cae70fd4.1652262892761'}

x = requests.post('http://localhost:5500/api/verify-otp', json=myobj, headers={"Content-Type":"application/json"})
print('Response Status : '  + str(x.status_code))


