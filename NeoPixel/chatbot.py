import requests

response = requests.get('https://api.cai.tools.sap/connect/v1/conversations/1944808e-da15-4970-a86e-0da554686a6445688',
  headers={'Authorization': 'Token 12c08098620ef11045d829e3841eae35'}
)

print(response.text)
