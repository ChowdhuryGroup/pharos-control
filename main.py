'''
Utility functions for controlling the PHAROS using the REST Server in the
PHAROS User Application
'''
import requests

base_url = "http://localhost:20020/v1/"
headers = {'Content-Type': 'application/json; charset=utf-8'}

def get_pp():
    response = requests.get(base_url+'Basic/TargetPpDivider')
    if response.status_code == 200:
        print(f"PP Divider is set to {response.text}")
        return int(response.text)

def set_pp(pp: int):
    response = requests.put(base_url+'Basic/TargetPpDivider', data=str(pp), headers=headers)
    if response.status_code == 200:
        print(f"PP Divider successfully changed to {pp}")
    elif response.status_code == 400:
        print("Data is formatted incorrectly")

def close_shutter():
    response = requests.post(base_url+"Basic/CloseOutput")
    if response.status_code == 200:
        print("Closing the shutter.")
    elif response.status_code == 403:
        print("Shutter is already closed, not closing.")

def open_shutter():
    response = requests.post(base_url+"Basic/EnableOutput")
    if response.status_code == 200:
        print("Opening the shutter.")
    elif response.status_code == 403:
        print("Shutter is already open, not opening.")

if __name__ == "__main__":
    get_pp()