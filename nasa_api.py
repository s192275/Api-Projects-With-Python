import requests   
from PIL import Image 
from io import BytesIO 

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos"
api_key = "YOUR_API_KEY"
response = requests.get(f"{url}?api_key={api_key}")
if response.status_code == 200:
    data = response.json()
    latest_photos = data["latest_photos"]
    if latest_photos is not None:
        for i in range(100):
            latest_photo = latest_photos[i]
            img_src = latest_photo['img_src']
            print("Last Mars Picture")
            print(f"Image Source : {img_src}")
        
            response = requests.get(img_src)
            img = Image.open(BytesIO(response.content))
            img.show()
    else:
        print(f"Error : {response.status_code}")    