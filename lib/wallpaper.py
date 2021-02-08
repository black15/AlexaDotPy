import os
import random
import ctypes
import platform
import requests
import pwd

wallpapers_list = ['dark','flower','linux','python','hacking'] # Just Testing

user = pwd.getpwuid(os.getuid()).pw_name # Getting Pc Username For Later Use

def pick_wall(query):
    rand_wall = random.randint(0,1) # Pixels Page To Search In
    headers = {'Authorization': '563492ad6f917000010000013d47f0a298eb47b6ba68417d71b9cd2f'} # Dict Contains Api Key

    #Seting Up Pexels Api
    url = f'https://api.pexels.com/v1/search?per_page=1&page={str(rand_wall)}&query={query}'

    #Response From API After Request is Sent Contains The Api key
    response= requests.get(url, headers=headers)

    if response.status_code == 200:
        image = response.json().get('photos')[0]['src']['original']

        #Making a Request Again Using API key to Get The Image
        image = requests.get(image)

        #Save The Content Of The Image To the PC
        with open('wallpaper.jpg','wb') as wallpaper:
            wallpaper.write(image.content)
            if not os.path.exists(f'/home/{user}/Wallpapers/'):
                os.mkdir('/home/{user}/Wallpapers/')
            os.system(f'mv wallpaper.jpg /home/{user}/Wallpapers 2>/dev/null')

            return f'/home/{user}/Wallpapers/wallpaper.jpg'

    # If Any Error Occurred
    else:
        return "No Wallpapers"

def apply_wall():

    picker = pick_wall(query=random.choice(wallpapers_list))
    system_is = platform.system().lower()

    if system_is == "linux" and 'wallpaper' in picker:
        command = f"gsettings set org.gnome.desktop.background picture-uri file://{picker}"
        try:
            os.system(command)
            print('Wallpaper Succefuly Changed !')

        except Exception as err:
            print(err)
            return False
    
    if picker == "No Wallpapers":
        return False

if __name__ == '__main__':
    apply_wall()
