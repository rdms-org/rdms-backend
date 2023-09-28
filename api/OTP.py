from random import randint
import asyncio
import time

#otp 작업 저장해둘 딕셔너리, key = otp, value = info
otp_list = {}

#OTP생성
def generate(type, data):
    while True:
        otp = str(randint(0,9999)).zfill(4)
        if otp not in otp_list:
            break
    otp_info = {"expires":time.time()+180,"type":type,"data":data,"execute":False, "valid":False}
    otp_list[otp] = otp_info
    return otp

#OTP 인증여부 확인
async def valid_wait(otp):
    otp_info = otp_list[otp]
    while True:
        if time.time()> otp_info["expires"]:
            return False
        if otp_info["valid"]:
            return True
        await asyncio.sleep(0.1)
        

#OTP 실행
async def execute(otp):
    if otp in otp_list:
        otp_info = otp_list[otp]
        if otp_info["execute"] == False:
            if otp_info["expires"] >= time.time():
                otp_info["execute"] = True
                if await valid_wait(otp):
                    del(otp_list[otp])
                    return True
                else:
                    del(otp_list[otp])
                    return False
                
            else:
                del(otp_list[otp])
                return False
        else:
            return False
    else:
        return False

#OTP 인증
def valid(otp):
    if otp in otp_list:
        otp_info = otp_list[otp]
        if otp_info["expires"] >= time.time():
            if otp_info["execute"]:
                #작업수행
                res = "작업결과"
                otp_info["valid"]=True
                return res
            else:
                return False
        else:
            del(otp_list[otp])
            return False
    else:
        return False

#OTP 만료설정
def expire(otp):
    if otp in otp_list:
        otp_list[otp]["expires"] = 0
        return True
    else:
        return False