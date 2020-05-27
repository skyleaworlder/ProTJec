import jwt
import time
from flask import Flask
import traceback

app = Flask(__name__)
DAY_TIME=86400
PRIVATE_KEY='-----BEGIN PRIVATE KEY-----\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgGCNeXy/dowpT/i9m\nr9sejwtvuF3kHHIKbyMMlNWcikShRANCAATzsmuWXiq6Fi62eXEB8+rZI9TFOxyo\n3zZg86I4l/5t+cOY0l9gS/95LNpyTmpo1ILoaL6fd5UmZ96j2aOyJ3J3\n-----END PRIVATE KEY-----'
PUBLIC_KEY='-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE87Jrll4quhYutnlxAfPq2SPUxTsc\nqN82YPOiOJf+bfnDmNJfYEv/eSzack5qaNSC6Gi+n3eVJmfeo9mjsidydw==\n-----END PUBLIC KEY-----'

def generateJWT(info):
    roles = 'admin' if info['level'] == 0 else 'client'
    header={
        "typ":"JWT",
        "alg":"HS256"
    }
    payload = {
        "iss": "protjec.com",  #issuer
        "iat": time.time(),     #issue at
        "exp": time.time() + DAY_TIME*3,
        "no": info['no'],
        "level": roles,
        "avatar": info['avatar'],
        "inst": info['inst'],
        "grade": info['grade'],
        "name": info['name'],
        "id": info['id'],
        "document": info['document'],
        "chat": info['chat']
    }
    token = jwt.encode(
        payload=payload,
        key=PRIVATE_KEY,
        algorithm="HS256",
        headers=header
    ).decode('utf-8')
    return token

def checkJWT(token):
    try:
        data=jwt.decode(token, PRIVATE_KEY, algorithms='HS256')
        res={'is_login':1, 'no':data['no'], 'level':data['level']}
        if data['exp']-time.time() < DAY_TIME:
            res.update({'reset':True})
        return res
    except jwt.ExpiredSignatureError:
        traceback.print_exc()
        return {'is_login': 0, 'expired': 1}
    except Exception as e:
        traceback.print_exc()
        return {'is_login': 0, 'expired': 0}
