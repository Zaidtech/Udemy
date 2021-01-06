import requests
while True:
    url = 'https://docs.google.com/forms/d/100pn1VZwpT8adJamJR3gL26iIDYgwYaB2hchU_DT4z4/viewform?edit_requested=true&pli=1'
    
    
    responce = requests.get('https://docs.google.com/forms/d/100pn1VZwpT8adJamJR3gL26iIDYgwYaB2hchU_DT4z4/viewform?edit_requested=true&pli=1')
    x = requests.post(url, data = 'Test')
    print(x.text)
    print(responce.status_code)