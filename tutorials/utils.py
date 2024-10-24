import requests, base64

def download_file(url, username, password):
    ## Get Access Token of OIDC
    tokens = get_user_access_token(username, password)
    access_token = tokens["access_token"]
    params = {
        "access_token": access_token,
    }
    ##import pdb; pdb.set_trace()
    ret = send_request(url, method="get", **params)
    if ret.status_code==200:
        outfile = url.split("/")[-1]
        with open(outfile, mode="wb") as f:
            f.write(ret.content)
        return outfile
    else:
        return ret


def get_user_access_token(username, password):

    url = f'https://keycloak.dev.services.eodc.eu/auth/realms/eodc-dev/protocol/openid-connect/token'
    headers = {
       "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "password",
        "client_id": "sdk-login",
        "scope":  "offline_access",
        "username" : username,
        "password": password,
    }
    ret = requests.post(url, headers=headers, data=data)
    return ret.json()


def send_request(url, access_token=None, username=None, password=None, method="get", data=None):
    
    headers = {}
    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"
    elif username and password:
        b64_userpass = base64.b64encode(f"{username}:{password}".encode("ascii")).decode("ascii")
        headers["Authorization"] = f"Basic {b64_userpass}"
    else:
        raise RuntimeError("Either access token or username and password need be provided")
    pass
    
    method = method.lower()
    ret = None
    if method == "get":
        ret = requests.get(url, headers=headers, data=data)
    elif method == "post":
        ret = requests.post(url, headers=headers, data=data) 
    return ret
