from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
    "type": "service_account",
    "project_id": "prime-heuristic-344223",
    "private_key_id": "55a762783d2270a567e2d0157adf67d5d5cdaa13",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC+hmrOxs/WYVdW\nUyb14cTJ4FIuo9NT00i7xyaWVcoGlSPIKZw58ZCdhCT9LCX7dL7BJXm4TWk2pVrp\nCObtVJ02L/Pnl+0tLBzWpv5JOd80hWnrEByM1xNMu1zIfFjO2gNembQBvE7MWHq0\nHwlcRxKnYEUcUEDnQ3h2unhdf/2OwYDJdVUqdbZsT5bko5Lh5BKOwbHb9rho6Nh5\nuVIpkTt1Im5FbS3uJOi+wbWHX9TQ+Oz979VxbZSyE7WIvEAPpipEM/64d/WGnVTT\n3Q/fXpE+OZAkpSaT3G6MP+OSega6zVazRvIVn35UXa8WTbbG4msbv4hZtWs5r5kw\nP/L0TvJrAgMBAAECggEAT+xLOdqkrSXAYXIYUeUXjCgR0Ybfy7ZCOKNeSIpMaV5+\n2CS8aIIxTCJ28c1nUYizzIpP+URf8pCDBma5mK16FZUgF/Lfh6eNoW4EFeu0+m9M\n81Ka52oBqpqeXWvsRTmnWDPaEzBPTeF/97ddUdxuss/rrejskRb4nbWzcGWUlCFV\nGG/2nPZHht0r+7Fu9WZuv0I8vy/QrKwNeChJsfrupGTB8RGKRYw/0RyJzSijIQoj\nPFjkWFATfxrLWDKAL44KiMp2HSQ9m891hSKaUwPQWUZmREe67VYvPWvKpWSCGDYY\n6q0zgz+Lt0pVpMjVeT2ff3oraQoTXupRs1PrTIVIgQKBgQD+0vWI5kCgAP+frg2y\nyJpB1BZdmHvd86Fb/JTFIuU1wCfBmElxIgEOCOBrBlOTSgYoKM4amjMrR3p7BZkN\nAbmgsqaXWrlwalMfa6Q2Qt1EVOW5O8CBpeVUJIptc5u9Phl1J7KBrbRGXG5OalLn\nsdkyuvDkUEDKDFRri6qbdo20ewKBgQC/Z39Skjtgt3n0ObN2U91/xneq0BU1AGQI\n8jHBop7BqZ/YFu0tLkNQxXu6YP4ZbvyP9KRGW4a7qnTHKsUcBDgOJGimpyLzNnb3\npU5r1CtzmeQQnjGkP8l4Txjys5EnI3TisVQq0vBUxXu3ZDfyokkqsrxJy1nFQq7d\n9K/f4umu0QKBgQCk3Jc+Grl0yzCWfmUeZepm7HAL3btFvXmHqcIWSJ1CSS9vcLcT\nGozUJ6oJk+4+PIX/NWcijuDL/1KehOCgKZ2O+gYNpgSTVjaw/VMgR+Ifc02sqZvC\nRTI5XeqxJTp9FNAjm6tBesBHRUWYNfGtNMLwr0FqdQF1tsRnT9Tw/6JuQQKBgQCh\nOqhowJ9d4A/NpxFB+nEZoe/JphBHHjYlxwYcq0R5s83es6lEJrUzg7auj+dbOz9q\nb9Q1JAIBcRt/bcqtx+wEFa1FvIJXRyi9gLTnZcjYTuhrCyabydOHEXHdd18tDdP2\n5RMWI6uobNXC7JuoOgXR/s9WhgHvhTVR6DyCJl1cEQKBgDHbr7OdyODMqnvMBgH2\nXHIza5i8/f2jkJpGiG5dWjktU5nG4SkFtauUKRj6DluX9wcWBbt5aSoQgeY7tLjT\nZRN3BNfgghLztORyLPPQ95TpYtblXoTFC/XR02ZADG+Mi0Tj47tCv8OBtu5ohjX2\nd7424tqi7vXOUusTIHwJe5AN\n-----END PRIVATE KEY-----\n",
    "client_email": "757109128701-compute@developer.gserviceaccount.com",
    "client_id": "105449407764909999968",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/757109128701-compute%40developer.gserviceaccount.com"
}

try:
    res = requests.get(
        f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    
    print("Loading...")

    soup = BeautifulSoup(res.text, 'html.parser')
    
    info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()
    
    print(info)

    """Uploads a file to the bucket."""
    credentials = service_account.Credentials.from_service_account_info(credentials_dict)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket('weather-espm')
    blob = bucket.blob('weather_info.txt')

    blob.upload_from_string(info + '\n')
    
    print('File uploaded.')
    
    print("Finished.")

except Exception as ex:
    print(ex)
