"""
Utility functions for controlling the PHAROS using the REST Server in the
PHAROS User Application
"""

import requests

BASE_URL = "http://localhost:20020/v1/"
headers = {"Content-Type": "application/json; charset=utf-8"}


def get_pp() -> int:
    """
    Get the pulse picker divider value
    """
    response = requests.get(BASE_URL + "Basic/TargetPpDivider", timeout=10)
    if response.status_code == 200:
        print(f"PP Divider is set to {response.text}")
        return int(response.text)

    # If -1, that means the pulse picker setting wasn't retrieved
    return -1


def set_pp(pp: int):
    """
    Set the pulse picker divider value
    """
    response = requests.put(
        BASE_URL + "Basic/TargetPpDivider", data=str(pp), headers=headers, timeout=10
    )
    if response.status_code == 200:
        print(f"PP Divider successfully changed to {pp}")
    elif response.status_code == 400:
        print("Data is formatted incorrectly")


def close_shutter():
    """
    Close the laser shutter
    """
    response = requests.post(BASE_URL + "Basic/CloseOutput", timeout=10)
    if response.status_code == 200:
        print("Closing the shutter.")
    elif response.status_code == 403:
        print("Shutter is already closed, not closing.")


def open_shutter():
    """
    Open the laser shutter
    """
    response = requests.post(BASE_URL + "Basic/EnableOutput", timeout=10)
    if response.status_code == 200:
        print("Opening the shutter.")
    elif response.status_code == 403:
        print("Shutter is already open, not opening.")


if __name__ == "__main__":
    get_pp()
