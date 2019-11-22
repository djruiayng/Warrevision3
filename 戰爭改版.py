# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, ast, urllib, urllib.parse, timeit, _thread#, LineService

cl = LINE("npmzitpsk@inwebtm.com","djry9420")
print("機器壹登入成功")
k1 = LINE("uulcfd@iwebtm.com","djry9420")
print("機器貳登入成功")
k2 = LINE("nmkbyk@itymail.com","djry9420")
print("機器參登入成功")
k3 = LINE("oywvoq@resmail24.com","djry9420")
print("機器肆登入成功")
k4 = LINE("bfvtwkjrd@iwebtm.com","djry9420")
print("機器伍登入成功")
k5 = LINE("zilcerj@itymail.com","djry9420")
print("機器陸登入成功")
js = LINE("bcedfei@resmail24.com","djry9420")
print("js登入成功")
js2 = LINE("mttgbazpp@3mailapp.net","djry9420")
print("js2登入成功")
print("[ 登錄系統 ]成功(  -᷄ω-᷅ )")
print("登入所花時間為"+str(format_timespan(time.time())))

clMID = cl.profile.mid
k1MID = k1.profile.mid
k2MID = k2.profile.mid
k3MID = k3.profile.mid
k4MID = k4.profile.mid
k5MID = k5.profile.mid
jsMID = js.profile.mid
js2MID = js2.profile.mid
set = {
    "bot1":[k1,k2,k3,k4,k5],
    "bots1":[clMID,k1MID,k2MID,k3MID,k4MID,k5MID,jsMID,js2MID],
    "limit":False
}

oepoll = OEPoll(cl)
oepolls = OEPoll(js)
oepolls = OEPoll(js2)
ban = json.load(codecs.open("ban.json","r","utf-8"))

#========================================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def kick(x,param1,param2,bool):
    if bool:
        try:
            x.kickoutFromGroup(param1,[param2])
        except:
            pass
        ban["blacklist"][param2] = True
        json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
def split_by_k( seq, n ):
    out = []
    if len(seq)%n == 0: ti = len(seq)//n
    else: ti = len(seq)//n+1
    for x in range(ti):
        try: out.append(seq[n*x:n*(x+1)])
        except: out.append(seq[n*x:])
    return out
def backupData():
    try: 
        json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
        return True
    except Exception as error:
        logError(error)
        return False
def ismid(mid):
    try:
        cl.getContact(mid)
        return True
    except:
        return False
def cek(mid):
    if mid  in (ban["admin"] + ban["owners"] + set["bots1"]):
        return True
    else:
        return False
def banuser(param2):
    if not cek(param2):
        ban["blacklist"][param2] = True
        json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
def backGroup(to,bot,target):
    G = bot.getGroupWithoutMembers(to)
    G.preventedJoinByTicket = False
    bot.updateGroup(G)
    Ticket = bot.reissueGroupTicket(to)
    target.acceptGroupInvitationByTicket(to,Ticket)
    G.preventedJoinByTicket = True
    bot.updateGroup(G)
def killban(to):
    group = cl.getGroup(to)
    gMembMids = [contact.mid for contact in group.members]
    matched_list = []
    for tag in ban["blacklist"]:
        matched_list+=filter(lambda str: str == tag, gMembMids)
    if matched_list == []:
        return True
    else:
        for jj in matched_list:
            random.choice(set["bot1"]).kickoutFromGroup(to,[jj])
        cl.sendMessage(to, "黑名單以踢除")
        return False
def unsend(msgid):
    sleep(10)
    cl.unsendMessage(msgid)
def joinLink(x,to,on=False):
    G = cl.getGroupWithoutMembers(to)
    if G.preventedJoinByTicket != on:
        G.preventedJoinByTicket = on
        x.updateGroup(G)
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def helpmessage():
    helpMessage = """╔═══════════════════
╠🔥༺ʚ弒神༒防翻ɞ༻🔥
╠══════ Admin ══════
╠🔥 Gc-查詢自己剩餘票數
╠🔥 Test-機器報數
╠🔥 Speed-速度
╠🔥 bye-分身解防
╠🔥 Save-儲存設定
╠🔥 Banlist-黑單
╠🔥 Adminlist-權限者清單
╠🔥 mid @-查詢序號
╠🔥 踢 @-多標踢人
╠🔥 標記-全體標記
╠🔥 機器退-解防(含主機)
╚〘Created By ©弒神防翻系統™ 〙"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""╔═══════════════════
╠🔥༺ʚ弒神༒防翻ɞ༻🔥
╠══════ Owner ══════
╠🔥 Lg-所有群組列表
╠🔥 Rebot-重新啟動
╠🔥 Gc mid-MID查票
╠🔥 Add @-新增權限
╠🔥 Add-友資新增權限
╠🔥 Del @-刪除權限
╠🔥 Del-友資刪除權限
╠🔥 A mid (times)-加票
╠🔥 Ban:mid-MID黑單
╠🔥 Ban-友資黑單
╠🔥 Ban @-標注黑單
╠🔥 Unban:mid-MID黑單
╠🔥 Unban-友資黑單
╠🔥 Unban @-標注黑單
╠🔥 Gc-查詢自己剩餘票數
╠🔥 Test-機器報數
╠🔥 Speed-速度
╠🔥 Save-儲存設定
╠🔥 Banlist-黑單
╠🔥 Adminlist-權限者清單
╠🔥 Clear ban-清除黑單
╠🔥 Kg-全群掃黑
╠🔥 Kill ban-當前群組掃黑
╠🔥 mid @-查詢序號
╠🔥 踢 @-多標踢人
╠🔥 主機名子改:-換名
╠🔥 機器名子改:-換名
╠🔥 主機狀態改:-換狀態
╠🔥 機器狀態改:-換狀態
╠🔥 換主機圖片
╠🔥 換機器圖片
╠🔥 標記-全體標記
╠🔥 機器退-解防(含主機)
╚〘Created By ©弒神防翻系統™ 〙"""
    return helpMessageTag
def helpn():
    helpN = """╔═══════════════════
╠🔥༺ʚ弒神༒防翻ɞ༻🔥
╠══════ For All ══════
╠🔥 Gc-查詢自己剩餘票數
╠🔥 Test-機器報數
╠🔥 Speed-速度
╚〘Created By ©弒神防翻系統™ 〙"""
    return helpN
wait = {
    "ban" : False,
    "unban" : False,
    "add" : False,
    "del" : False,
    "mid" : {},
    "clp" : False,
    "botp" : False
}

if clMID not in ban["owners"]:
    ban["owners"].append(clMID)

#=========================================================================
def lineBot(op):
    try:
        if op.type == 0:
            return
        elif op.type == 13:
            if not cek(op.param2):
                random.choice(set["bot1"]).kickoutFromGroup(op.param1,[op.param2])
                for x in op.param3.split('\x1e'):
                    try:
                        random.choice(set["bot1"]).cancelGroupInvitation(op.param1,[x])
                    except:
                        random.choice(set["bot1"]).kickoutFromGroup(op.param1,[x])
                ban["blacklist"][op.param2] = True
                json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                return
        elif op.type == 19:
            if not cek(op.param2):
                random.choice(set["bot1"]).kickoutFromGroup(op.param1,[op.param2])
                ban["blacklist"][op.param2] = True
                json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                return
        elif op.type == 11:
            if not cek(op.param2):
                G = cl.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js.acceptGroupInvitation(op.param1)
                                        G = js.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js.updateGroup(G)
                                        Ticket = js.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js.updateGroup(G)
                                        js.leaveGroup(op.param1)
                                        cl.findAndAddContactsByMid(jsMID)
                                        cl.inviteIntoGroup(op.param1,[jsMID])
            elif not cek(op.param2):
                G = k1.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js.acceptGroupInvitation(op.param1)
                                        G = js.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js.updateGroup(G)
                                        Ticket = js.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js.updateGroup(G)
                                        js.leaveGroup(op.param1)
                                        k1.findAndAddContactsByMid(jsMID)
                                        k1.inviteIntoGroup(op.param1,[jsMID])
            elif not cek(op.param2):
                G = k2.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js.acceptGroupInvitation(op.param1)
                                        G = js.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js.updateGroup(G)
                                        Ticket = js.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js.updateGroup(G)
                                        js.leaveGroup(op.param1)
                                        k2.findAndAddContactsByMid(jsMID)
                                        k2.inviteIntoGroup(op.param1,[jsMID])
            elif not cek(op.param2):
                G = k3.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js.acceptGroupInvitation(op.param1)
                                        G = js.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js.updateGroup(G)
                                        Ticket = js.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js.updateGroup(G)
                                        js.leaveGroup(op.param1)
                                        k3.findAndAddContactsByMid(jsMID)
                                        k3.inviteIntoGroup(op.param1,[jsMID])
            elif not cek(op.param2):
                G = k4.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js.acceptGroupInvitation(op.param1)
                                        G = js.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js.updateGroup(G)
                                        Ticket = js.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js.updateGroup(G)
                                        js.leaveGroup(op.param1)
                                        k4.findAndAddContactsByMid(jsMID)
                                        k4.inviteIntoGroup(op.param1,[jsMID])
            elif not cek(op.param2):
                G = k5.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js.acceptGroupInvitation(op.param1)
                                        G = js.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js.updateGroup(G)
                                        Ticket = js.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js.updateGroup(G)
                                        js.leaveGroup(op.param1)
                                        k5.findAndAddContactsByMid(jsMID)
                                        k5.inviteIntoGroup(op.param1,[jsMID])
            elif not cek(op.param2):
                G = cl.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js2.acceptGroupInvitation(op.param1)
                                        G = js2.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js2.updateGroup(G)
                                        Ticket = js2.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js2.updateGroup(G)
                                        js2.leaveGroup(op.param1)
                                        cl.findAndAddContactsByMid(js2MID)
                                        cl.inviteIntoGroup(op.param1,[js2MID])
            elif not cek(op.param2):
                G = k1.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js2.acceptGroupInvitation(op.param1)
                                        G = js2.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js2.updateGroup(G)
                                        Ticket = js2.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js2.updateGroup(G)
                                        js2.leaveGroup(op.param1)
                                        k1.findAndAddContactsByMid(js2MID)
                                        k1.inviteIntoGroup(op.param1,[js2MID])
            elif not cek(op.param2):
                G = k2.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js2.acceptGroupInvitation(op.param1)
                                        G = js2.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js2.updateGroup(G)
                                        Ticket = js2.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js2.updateGroup(G)
                                        js2.leaveGroup(op.param1)
                                        k2.findAndAddContactsByMid(js2MID)
                                        k2.inviteIntoGroup(op.param1,[js2MID])
            elif not cek(op.param2):
                G = k3.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js2.acceptGroupInvitation(op.param1)
                                        G = js2.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js2.updateGroup(G)
                                        Ticket = js2.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js2.updateGroup(G)
                                        js2.leaveGroup(op.param1)
                                        k3.findAndAddContactsByMid(js2MID)
                                        k3.inviteIntoGroup(op.param1,[js2MID])
            elif not cek(op.param2):
                G = k4.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js2.acceptGroupInvitation(op.param1)
                                        G = js2.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js2.updateGroup(G)
                                        Ticket = js2.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js2.updateGroup(G)
                                        js2.leaveGroup(op.param1)
                                        k4.findAndAddContactsByMid(js2MID)
                                        k4.inviteIntoGroup(op.param1,[js2MID])
            elif not cek(op.param2):
                G = k5.getGroupWithoutMembers(op.param1)
                threading.Thread(target=banuser,args=(op.param2,)).start()
                try:
                    threading.Thread(target=k5.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                except:
                    try:
                        threading.Thread(target=k4.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                        G.preventedJoinByTicket = True
                        k5.updateGroup(G)
                    except:
                        try:
                            threading.Thread(target=k3.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                            G.preventedJoinByTicket = True
                            k4.updateGroup(G)
                        except:
                            try:
                                threading.Thread(target=k2.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                try:
                                    threading.Thread(target=k1.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                    G.preventedJoinByTicket = True
                                    k2.updateGroup(G)
                                except:
                                    try:
                                        threading.Thread(target=cl.kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                                        G.preventedJoinByTicket = True
                                        k1.updateGroup(G)
                                    except:
                                        js2.acceptGroupInvitation(op.param1)
                                        G = js2.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js2.updateGroup(G)
                                        Ticket = js2.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js2.updateGroup(G)
                                        js2.leaveGroup(op.param1)
                                        k5.findAndAddContactsByMid(js2MID)
                                        k5.inviteIntoGroup(op.param1,[js2MID])
            return
        elif op.type == 32:
            if cek(op.param3) and not cek(op.param2) and op.param3 not in jsMID:
                try:
                    threading.Thread(target=banuser,args=(op.param2,)).start()
                    bot = random.choice(set["bot1"])
                    bot.kickoutFromGroup(op.param1,[op.param2])
                    bot.findAndAddContactsByMid(op.param3)
                    bot.inviteIntoGroup(op.param1,[op.param3])
                except:
                    pass
            return
        elif op.type == 5:
            cl.sendMessage(op.param1, "你好 {} 謝謝你加我為好友  \n此機器為戰爭機器人\n對防翻機器有興趣者可以私以下友資購買".format(str(cl.getContact(op.param1).displayName)))
            cl.sendContact(op.param1,'u56d30ff9392a9dddbe7fcdec518d1894')
        if op.type == 13:
            if clMID in op.param3:
                if op.param2 in set["bots1"]:
                    pass
                elif op.param2 in ban["owners"]:
                    cl.acceptGroupInvitation(op.param1)
                    try:
                        cl.inviteIntoGroup(op.param1,[k1MID,k2MID,k3MID,k4MID,k5MID,jsMID,js2MID])
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        cl.sendMessage(op.param1,"弒神天下防翻系統")
                    except:
                        G = cl.getGroupWithoutMembers(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        js.acceptGroupInvitationByTicket(op.param1,Ticket)
                        js2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        cl.sendMessage(op.param1,"弒神天下防翻系統")
                        cl.updateGroup(G)
                elif op.param2 in ban["user"]:
                    if "gid" in ban["user"][op.param2] :
                        ban["user"][op.param2].remove("gid")
                        ban["user"][op.param2].append(op.param1)
                        text = "你還擁有{}張票".format(str(ban["user"][op.param2].count("gid")))
                    elif op.param1 in ban["user"][op.param2]:
                        text = "票卷擁有者邀請入群\n輸入join機器便會入群防護"
                    else:
                        return
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,text)
                    try:
                        cl.inviteIntoGroup(op.param1,[k1MID,k2MID,k3MID,k4MID,k5MID,jsMID,js2MID])
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                    except:
                        G = cl.getGroupWithoutMembers(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        js.acceptGroupInvitationByTicket(op.param1,Ticket)
                        js2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                    backupData()
                else:
                    cl.sendMessage(op.param2,"票卷不夠喔!!請訊作者給票!!")
                    cl.sendMessage(op.param2,"u56d30ff9392a9dddbe7fcdec518d1894")
        elif op.type == 24 or op.type == 21 or op.type ==22:
            cl.leaveRoom(op.param1)
        elif (op.type == 25 or op.type == 26) and op.message.contentType == 0:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in sender:
                if ".kickall" in text.lower() or text.lower() == "kick on" or "kickall" in text.lower():
                    if sender not in ban["owners"]:
                        random.choice(set["bot1"]).kickoutFromGroup(to,[sender])
                        cl.sendMessage(to, "{} 嘗試使用翻群指令\n有破壞群組規定 暫時踢出".format(str(cl.getContact(sender).displayName)))
                elif text.lower() == 'gc':
                    if sender in ban["user"]:
                        cl.sendMessage(to,"你還擁有{}張票".format(str(ban["user"][sender].count("gid"))))
                    elif sender in ban["owners"]:
                        cl.sendMessage(to,"作者無須票卷~")
                    else:
                        cl.sendMessage(to,"沒有票了!歡迎購買邀請票券")
                elif text.lower() =='test':
                    a=1
                    cl.sendMessage(to,str(a))
                    try:
                        for x in set["bot1"]:
                            a+=1
                            x.sendMessage(to,str(a))
                    except:
                        pass
                elif text.lower().startswith("ticket ") or text.lower().startswith("票卷轉移 "):
                    try:
                        num = int(text.split(' ')[1])
                    except:
                        cl.sendMessage(to,"請輸入欲轉移的\"數字\"")
                    if sender in ban["owners"] :
                        wait["mid"][sender] = num
                        cl.sendMessage(to,"您將轉移 {} 張票卷,請傳送欲轉移的對象友資".format(str(num)))
                    elif sender in ban["user"] and ban["user"][sender].count("gid") >= num :
                        wait["mid"][sender] = num
                        cl.sendMessage(to,"您將轉移 {} 張票卷,請傳送欲轉移的對象友資".format(str(num)))
                        cl.sendMessage(to,"您還剩下 {} 張票卷".format(str(ban["user"][sender].count("gid")-num)))
                    elif sender in ban["user"]:
                        cl.sendMessage(to,"您的票卷不夠了!")
                        cl.sendMessage(to,"您還剩下 {} 張票卷,歡迎再次購買票卷w".format(str(ban["user"][sender].count("gid"))))
                    else:
                        cl.sendMessage(to,"沒有票了!歡迎購買邀請票券")
#                elif text.lower() =='test':
#                    cl.sendMessage(to,"運行中......")
#                    k1.sendMessage(to,"運行中......")
#                    k2.sendMessage(to,"運行中......")
#                    k3.sendMessage(to,"運行中......")
#                    k4.sendMessage(to,"運行中......")
#                    k5.sendMessage(to,"運行中......")
#                    k6.sendMessage(to,"運行中......")
                elif text.lower() == 'speed':
                    start = time.time()
                    cl.sendMessage(to, "計算中...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'help':
                    if sender in ban["admin"]:
                        helpMessage = helpmessage()
                        cl.sendMessage(to, str(helpMessage))
                    elif sender in ban["owners"]:
                        helpMessageTag = helpmessagetag()
                        cl.sendMessage(to, str(helpMessageTag))
                    else:
                        helpN = helpn()
                        cl.sendMessage(to, str(helpN))
            if sender in ban["admin"] or sender in ban["owners"]:
                if text.lower() == 'save':
                    backupData()
                    cl.sendMessage(to,'儲存設定成功!')
                elif text.lower() == 'runtime':
                    cl.sendMessage(to, "系統已運作 {}".format(str(format_timespan(time.time() - botStart))))
                elif text.lower() == 'unlimit':
                    set["limit"] = False
                    cl.sendMessage(to,"unblocked limit mode")
                elif text.lower() == 'adminlist':
                    if ban["admin"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[🔥 權限清單 🔥]══"
                        for mi_d in ban["admin"]:
                            try:
                                mc += "\n╠ "+cl.getContact(mi_d).displayName
                            except:
                                pass
                        cl.sendMessage(to,mc + "\n╚══════════════")
                elif text.lower() == '主控權限':
                    if ban["owners"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[🔥 權限清單 🔥]══"
                        for mi_d in ban["owners"]:
                            try:
                                mc += "\n╠ "+cl.getContact(mi_d).displayName
                            except:
                                pass
                        cl.sendMessage(to,mc + "\n╚══════════════")
                elif text.lower() == 'banlist':
                    if ban["blacklist"] == {}: cl.sendMessage(to,"無黑單成員!")
                    else:
                        a = []
                        for z in ban["blacklist"]:
                            a.append(z)
                        no = 1
                        re = []
                        for baner in split_by_k(a,50):
                            mc = "[ 黑單成員 ]"
                            for mi_d in baner:
                                try:
                                    mc += "\n✗ {}.|{}\n {} ".format(no,cl.getContact(mi_d).displayName,mi_d)
                                    no += 1
                                except: re.append(mi_d)
                            cl.sendMessage(to,mc + "\n[ 共 {} 名黑單 ]".format(no-1))
                        if re != []:
                            for r in re:
                                del ban["blacklist"][r]
                elif text.lower() == '標記':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "總共 {} 人".format(str(len(nama))))
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = (r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif text.lower().startswith("踢 "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in ban["owners"] or target in set["bots1"]:
                            pass
                        try:
                            random.choice(set["bot1"]).kickoutFromGroup(to,[target])
                        except:
                            pass        
                if text.lower() =='機器退':
                    try:
                        cl.sendMessage(to,'Bye~Bye~')
                        for x in set["bot1"]:
                            x.leaveGroup(msg.to)
                        try:
                            cl.cancelGroupInvitation(to,[jsMID])
                            cl.cancelGroupInvitation(to,[js2MID])
                        except:
                            js.leaveGroup(to)
                            js2.leaveGroup(to)
                    except:
                        pass
                    if sender in ban["user"] and to in ban["user"][sender]:
                        ban["user"][sender].remove(to) 
                        ban["user"][sender].append("gid")   
                    cl.leaveGroup(msg.to)                    
            if sender in ban["owners"]:
                if text.lower() == 'lg':
                    groups = cl.getGroupIdsJoined()
                    ret_ = "[群組列表]"
                    no = 1
                    for gid in groups:
                        group = cl.getGroup(gid)
                        ret_ += "\n {}. {} | {}\n{}".format(str(no), str(group.name), str(len(group.members)),gid)
                        no += 1
                    ret_ += "\n[總共 {} 個群組]".format(str(len(groups)))
                    cl.sendMessage(to, str(ret_))
                elif text.lower() == 'gclist':
                    user1 = ""
                    for x in ban["user"]:
                        user1 += "[user]\n-> "+cl.getContact(x).displayName+"\n[ticket] {}\n[group]\n".format(str(ban["user"][x].count("gid")))
                        for y in ban["user"][x]:
                            if y != "gid":
                                try:
                                    user1 += "-> "+cl.getGroupWithoutMembers(y).name+"\n"+str(y)+"\n"
                                except:
                                    user1 += "-> #Can't not relate to that group#\n"
                        user1 += "\n-----------------\n"
                    cl.sendMessage(to,user1+"[finish]")
                elif text.lower().startswith("gout "):
                    try:
                        gid =  cl.getGroupIdsJoined()[int(text[5:])-1]
                    except:
                        cl.sendMessage(to,"not in range.")
                        return
                    for x in set["bot1"]:
                        x.leaveGroup(gid)
                    try:
                        cl.cancelGroupInvitation(gid,[jsMID])
                    except:
                        js.leaveGroup(gid)
                    cl.sendMessage(gid,"已由遠端退出群組，各位再見")
                    cl.leaveGroup(gid)
                    for x in ban["user"]:
                        if gid in ban["user"][x]:
                            ban["user"][x].remove(gid)
                            break
                    cl.sendMessage(to,"成功退出該群組!")
                elif text.lower().startswith("gjoin "):
                    try:
                        gid = cl.getGroupIdsJoined()[int(text[6:])-1]
                    except:
                        cl.sendMessage(to,"not in range.")
                        return
                    try:
                        G = cl.getGroupWithoutMembers(gid)
                        if G.preventedJoinByTicket == True:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                        cl.sendMessage(to,"https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(gid))))
                    except:
                        cl.sendMessage(to,"not found")
                elif text.lower().startswith("joinall:https://line.me/r/ti/g/"):
                    ticket_id = text[31:]
                    group = cl.findGroupByTicket(ticket_id)
                    cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                    try:
                        cl.inviteIntoGroup(group.id,[jsMID])
                    except:
                        js.acceptGroupInvitationByTicket(group.id,ticket_id)
                    k1.acceptGroupInvitationByTicket(group.id,ticket_id)
                    k2.acceptGroupInvitationByTicket(group.id,ticket_id)
                    k3.acceptGroupInvitationByTicket(group.id,ticket_id)
                    k4.acceptGroupInvitationByTicket(group.id,ticket_id)
                    k5.acceptGroupInvitationByTicket(group.id,ticket_id)
                    group.preventedJoinByTicket = True
                    cl.updateGroup(group)
                    cl.sendMessage(to,"successed join {} !!".format(group.name))
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "重新啟動中...")
                    cl.sendMessage(to, "重啟成功")
                    restartBot()
                elif text.lower().startswith("主機名子改:"):
                    name = text[7:]
                    c = cl.profile
                    c.displayName = name
                    cl.updateProfile(c)
                elif text.lower().startswith("機器名子改:"):
                    name = text[8:]
                    for x in set["bot1"]:
                        c = x.profile
                        c.displayName = name
                        x.updateProfile(c)
                elif text.lower().startswith("主機狀態改:"):
                    name = text[6:]
                    c = cl.getProfile()
                    c.statusMessage = name
                    cl.updateProfile(c)
                elif text.lower().startswith("機器狀態改:"):
                    name = text[7:]
                    for x in set["bot1"]:
                        c = x.getProfile()
                        c.statusMessage = name
                        x.updateProfile(c)
                elif text.lower() == '換主機圖片':
                    wait["clp"] = True
                    cl.sendMessage(to,"send Pic")
                elif text.lower() == '換機器圖片':
                    wait["botp"] = 6
                    cl.sendMessage(to,"send Pic")
#=======================================================================================                    
                elif text.lower() == 'clear ban':
                    ban["blacklist"].clear()
                    cl.sendMessage(to, "已清空黑名單")
                    json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                elif text.lower() == 'kg':
                    gid = cl.getGroupIdsJoined() 
                    for i in gid:
                        killban(i)
                    cl.sendMessage(to,"success kill all groups ban user")
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        if killban(to):
                            cl.sendMessage(to, "沒有黑名單")
                elif text.lower().startswith("add "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ban["admin"]:
                        ban["admin"].append(str(inkey))
                        cl.sendMessage(to, "已獲得權限！")
                    else:
                        cl.sendMessage(to,"already")
                    json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                elif text.lower().startswith("del "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ban["admin"]:
                        ban["admin"].remove(str(inkey))
                        cl.sendMessage(to, "已取消權限！")
                    else:
                    	cl.sendMessage(to,"user is not in admin")
                    json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                elif text.lower().startswith("新增主控權 "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ban["owners"]:
                        ban["owners"].append(str(inkey))
                        cl.sendMessage(to, "已獲得主權限！")
                    else:
                        cl.sendMessage(to,"already")
                    json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                elif text.lower().startswith("取消主控權 "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ban["owners"]:
                        ban["owners"].remove(str(inkey))
                        cl.sendMessage(to, "已取消權限！")
                    else:
                    	cl.sendMessage(to,"user is not in admin")
                    json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                elif text.lower().startswith("rmticket:"):
                    num = int(text.lower().split(':')[2])
                    user = str(text.lower().split(':')[1])
                    if ban["user"][user].count('gid') >= num:
                        for a in range(num):
                            ban["user"][user].remove("gid")
                elif text.lower() == 'add':
                    wait["add"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'del':
                    wait["del"] = True
                    cl.sendMessage(to,"Please send a Contact")
                elif text.lower() == '新增主控權':
                    wait["新增主控權"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == '取消主控權':
                    wait["取消主控權"] = True
                    cl.sendMessage(to,"Please send a Contact")
                elif text.lower().startswith("ban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    a = 0
                    for target in targets:
                        if target not in ban["owners"] and target not in ban["admin"] and target not in set["bots1"]:
                            ban["blacklist"][target] = True
                            a += 1
                    cl.sendMessage(msg.to,"已加入黑單共" + str(a) + "人")
                elif text.lower() == 'logout-y':
                    cl.sendMessage(to,"[warn]\nsystem will stop !!")
                    os._exit(0)
                elif text.lower().startswith("clname:"):
                    name = text[7:]
                    c = cl.profile
                    c.displayName = name
                    cl.updateProfile(c)
                elif text.lower().startswith("botname:"):
                    name = text[8:]
                    for x in set["bot1"]:
                        c = x.profile
                        c.displayName = name
                        x.updateProfile(c)
                elif text.lower().startswith("clbio:"):
                    name = text[6:]
                    c = cl.getProfile()
                    c.statusMessage = name
                    cl.updateProfile(c)
                elif text.lower().startswith("botbio:"):
                    name = text[7:]
                    for x in set["bot1"]:
                        c = x.getProfile()
                        c.statusMessage = name
                        x.updateProfile(c)
                elif text.lower() == 'cclp':
                    wait["clp"] = True
                    cl.sendMessage(to,"send Pic")
                elif text.lower() == 'cbotp':
                    wait["botp"] = 6
                    cl.sendMessage(to,"send Pic")
                elif text.lower().startswith("ban:"):
                    txt = text[4:].split(' ')
                    for mid in txt:
                        if not ismid(mid):
                            continue
                        if mid not in ban["owners"] and mid not in ban["admin"] and mid not in set["bots1"]:
                            ban["blacklist"][mid] = True
                            cl.sendMessage(msg.to,"已加入黑單!")
                elif text.lower().startswith("unban:"):
                    txt = text[6:].split(' ')
                    a = 0
                    for mid in txt:
                        try:
                            del ban["blacklist"][mid]
                            a+=1
                        except:
                            cl.sendMessage(msg.to,"刪除" + str(mid) + "失敗 !")
                    cl.sendMessage(msg.to,"已刪除黑單共" + str(a) + "人")
                elif text.lower().startswith("unban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    a = 0
                    for target in targets:
                        try:
                            ban["blacklist"][target] =False
                            a += 1
                        except:
                            cl.sendMessage(msg.to,"刪除" + str(target) + "失敗 !")
                    cl.sendMessage(msg.to,"已刪除黑單共" + str(a) + "人")
                elif text.lower() == 'ban':
                    wait["ban"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'unban':
                    wait["unban"] = True
                    cl.sendMessage(to,"Please send a Contact")
        if op.type == 25 or op.type ==26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 1:
                if msg._from in ban["owners"]:
                    if wait["clp"] == True:
                        path1 = cl.downloadObjectMsg(msg.id)
                        wait["clp"] = False
                        cl.updateProfilePicture(path1)
                        cl.sendMessage(to, "Succes change pic")
                    elif wait["botp"]:
                        path1 = cl.downloadObjectMsg(msg.id)
                        wait["botp"] -= 1
                        all = set["bot1"]+[js]
                        all[wait["botp"] ].updateProfilePicture(path1)
                        cl.sendMessage(to, "Succes change pic")
            elif msg.contentType == 13:
                mid = msg.contentMetadata["mid"]
                if wait["ban"] == True:
                    if msg._from in ban["owners"]:
                        if mid in ban["blacklist"]:
                           cl.sendmessage(to,"already")
                           wait["ban"] = False
                        elif mid not in ban["owners"] and mid not in ban["admin"] and mid not in set["bots1"]:
                           ban["blacklist"][mid] = True
                           wait["ban"] = False
                           cl.sendMessage(to,"成功新增黑單")
                elif wait["unban"] == True:
                    if msg._from in ban["owners"]:
                        if mid not in ban["blacklist"]:
                           cl.sendmessage(to,"使用者並非黑單")
                           wait["unban"] = False
                        else:
                           del ban["blacklist"][mid]
                           wait["unban"] = False
                           cl.sendMessage(to,"成功移除黑單")
                elif wait["add"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] in ban["admin"]:
                           cl.sendmessage(to,"already")
                           wait["add"] = False
                        elif msg.contentMetadata["mid"] not in ban["admin"]:
                           ban["admin"].append(str(msg.contentMetadata["mid"]))
                           wait["add"] = False
                           cl.sendMessage(to,"成功新增權限")
                        else:
                           cl.sendMessage(to,"使用者於黑單中無法新增權限")
                        json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                elif wait["del"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] not in ban["admin"]:
                           cl.sendmessage(to,"使用者不在權限中")
                           wait["del"] = False
                        else:
                           ban["admin"].remove(str(msg.contentMetadata["mid"]))
                           wait["del"] = False
                           cl.sendMessage(to,"成功移除權限")
                        json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                elif wait["新增主控權"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] in ban["owners"]:
                           cl.sendmessage(to,"already")
                           wait["新增主控權"] = False
                        elif msg.contentMetadata["mid"] not in ban["owners"]:
                           ban["owners"].append(str(msg.contentMetadata["mid"]))
                           wait["新增主控權"] = False
                           cl.sendMessage(to,"成功新增權限")
                        else:
                           cl.sendMessage(to,"使用者於黑單中無法新增權限")
                        json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                elif wait["取消主控權"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] not in ban["owners"]:
                           cl.sendmessage(to,"使用者不在權限中")
                           wait["取消主控權"] = False
                        else:
                           ban["owners"].remove(str(msg.contentMetadata["mid"]))
                           wait["取消主控權"] = False
                           cl.sendMessage(to,"成功移除權限")
                        json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                if sender in wait["mid"] and mid not in ban["owners"]:
                    if sender not in ban["owners"]:
                        for a in range(wait["mid"][sender] ):
                            ban["user"][sender].remove("gid")
                    if mid not in ban["user"]:
                        ban["user"][mid] = []
                    ban["user"][mid] += ["gid"]*wait["mid"][sender]
                    cl.sendMessage(to,"成功轉移!")
                    json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                    del wait["mid"][sender]
    except Exception as error:
        print(error)
#=====================================================================================
def lineBot2II(op):
    try:
        if op.type ==0:
            return
        elif op.type == 32:
            if op.param2 == clMID:
                pass
            elif op.param3 == jsMID:
                try:
                    cl.inviteIntoGroup(op.param1,[jsMID])
                except:
                    try:
                        k1.inviteIntoGroup(op.param1,[jsMID])
                    except:
                        try:
                            k2.inviteIntoGroup(op.param1,[jsMID])
                        except:
                            try:
                                k3.inviteIntoGroup(op.param1,[jsMID])
                            except:
                                try:
                                   k4.inviteIntoGroup(op.param1,[jsMID])
                                except:
                                    try:
                                        k5.inviteIntoGroup(op.param1,[jsMID])
                                    except:
                                        G = cl.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        random.choice(set["bot1"]).updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        js.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        random.choice(set["bot1"]).updateGroup(G)
            if op.param2 == clMID:
                pass
            elif op.param3 == js2MID:
                try:
                    cl.inviteIntoGroup(op.param1,[js2MID])
                except:
                    try:
                        k1.inviteIntoGroup(op.param1,[js2MID])
                    except:
                        try:
                            k2.inviteIntoGroup(op.param1,[js2MID])
                        except:
                            try:
                                k3.inviteIntoGroup(op.param1,[js2MID])
                            except:
                                try:
                                   k4.inviteIntoGroup(op.param1,[js2MID])
                                except:
                                    try:
                                        k5.inviteIntoGroup(op.param1,[js2MID])
                                    except:
                                        G = cl.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        random.choice(set["bot1"]).updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        js2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        random.choice(set["bot1"]).updateGroup(G)
                if not cek(op.param2):
                    threading.Thread(target=banuser,args=(op.param2,)).start()
                    random.choice(set["bot1"]).kickoutFromGroup(op.param1,[op.param2])
        elif op.type == 17:
            if op.param2 in ban["blacklist"]: 
                threading.Thread(target=random.choice(set["bot1"]).kickoutFromGroup,args=(op.param1,[op.param2],)).start()
                G = cl.getGroupWithoutMembers(op.param1)
                G.preventedJoinByTicket = True
                random.choice(set["bot1"]).cancelGroupInvitation(op.param1,[op.param2])
                random.choice(set["bot1"]).updateGroup(G)
        elif op.type ==19:
            kickk = not cek(op.param2)
            if set["limit"]:
                for x in set["bot1"]:
                    try:
                        G = x.getGroupWithoutMembers(op.param1)
                        G.preventedJoinByTicket = True
                        x.updateGroup(G)
                        Ticket = x.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                    except:
                        continue
                    else:
                        break
                return
            if op.param3 in clMID:
                try:
                    threading.Thread(target=kick,args=(k3,op.param1,op.param2,kickk,)).start()
                    k1.inviteIntoGroup(op.param1,[clMID])
                    cl.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k4,op.param1,op.param2,kickk,)).start()
                        k2.inviteIntoGroup(op.param1,[clMID])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k5,op.param1,op.param2,kickk,)).start()
                            k3.inviteIntoGroup(op.param1,[clMID])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k1,op.param1,op.param2,kickk,)).start()
                                k4.inviteIntoGroup(op.param1,[clMID])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    threading.Thread(target=kick,args=(k2,op.param1,op.param2,kickk,)).start()
                                    k5.inviteIntoGroup(op.param1,[clMID])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k5.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js.acceptGroupInvitation(op.param1)
                                            kick(js,op.param1,op.param2,kickk)
                                            G = js.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js.updateGroup(G)
                                            Ticket = js.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js.updateGroup(G)
                                            js.leaveGroup(op.param1)
                                            cl.findAndAddContactsByMid(jsMID)
                                            cl.inviteIntoGroup(op.param1,[jsMID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k1,cl)
            elif op.param3 in k1MID:
                try:
                    threading.Thread(target=kick,args=(k4,op.param1,op.param2,kickk,)).start()
                    k2.inviteIntoGroup(op.param1,[k1MID])
                    k1.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k5,op.param1,op.param2,kickk,)).start()
                        k3.inviteIntoGroup(op.param1,[k1MID])
                        k1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k2,op.param1,op.param2,kickk,)).start()
                            k4.inviteIntoGroup(op.param1,[k1MID])
                            k1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k3,op.param1,op.param2,kickk,)).start()
                                k5.inviteIntoGroup(op.param1,[k1MID])
                                k1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    js.acceptGroupInvitation(op.param1)
                                    js.inviteIntoGroup(op.param1,[c1MID,k1MID,k2MID,k3MID,k4MID,k5MID,js2MID])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    js.leaveGroup(op.param1)
                                    k2.inviteIntoGroup(op.param1,[jsMID])
                                except:
                                    try:
                                        k5.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js.acceptGroupInvitation(op.param1)
                                            G = js.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js.updateGroup(G)
                                            Ticket = js.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js.updateGroup(G)
                                            js.leaveGroup(op.param1)
                                            k2.findAndAddContactsByMid(jsMID)
                                            k2.inviteIntoGroup(op.param1,[jsMID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k2,k1)
                random.choice(set["bot1"]).cancelGroupInvitation(op.param1,[op.param2])
            elif op.param3 in k2MID:
                try:
                    threading.Thread(target=kick,args=(k5,op.param1,op.param2,kickk,)).start()
                    k3.inviteIntoGroup(op.param1,[k2MID])
                    k2.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k1,op.param1,op.param2,kickk,)).start()
                        k4.inviteIntoGroup(op.param1,[k2MID])
                        k2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k3,op.param1,op.param2,kickk,)).start()
                            k5.inviteIntoGroup(op.param1,[k2MID])
                            k2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k4,op.param1,op.param2,kickk,)).start()
                                k1.inviteIntoGroup(op.param1,[k2MID])
                                k2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    js.acceptGroupInvitation(op.param1)
                                    js.inviteIntoGroup(op.param1,[c1MID,k1MID,k2MID,k3MID,k4MID,k5MID,js2MID])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    js.leaveGroup(op.param1)
                                    k3.inviteIntoGroup(op.param1,[jsMID])
                                except:
                                    try:
                                        k1.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js.acceptGroupInvitation(op.param1)
                                            kick(js,op.param1,op.param2,kickk)
                                            G = js.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js.updateGroup(G)
                                            Ticket = js.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js.updateGroup(G)
                                            js.leaveGroup(op.param1)
                                            k3.findAndAddContactsByMid(jsMID)
                                            k3.inviteIntoGroup(op.param1,[jsMID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k3,k2)
            elif op.param3 in k3MID:
                try:
                    kthreading.Thread(target=kick,args=(k1,op.param1,op.param2,kickk,)).start()
                    k4.inviteIntoGroup(op.param1,[k3MID])
                    k3.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k2,op.param1,op.param2,kickk,)).start()
                        k5.inviteIntoGroup(op.param1,[k3MID])
                        k3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k4,op.param1,op.param2,kickk,)).start()
                            k1.inviteIntoGroup(op.param1,[k3MID])
                            k3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k5,op.param1,op.param2,kickk,)).start()
                                k2.inviteIntoGroup(op.param1,[k3MID])
                                k3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    js.acceptGroupInvitation(op.param1)
                                    js.inviteIntoGroup(op.param1,[c1MID,k1MID,k2MID,k3MID,k4MID,k5MID,js2MID])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    js.leaveGroup(op.param1)
                                    k4.inviteIntoGroup(op.param1,[jsMID])
                                except:
                                    try:
                                        k2.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js.acceptGroupInvitation(op.param1)
                                            kick(js,op.param1,op.param2,kickk)
                                            G = js.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js.updateGroup(G)
                                            Ticket = js.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js.updateGroup(G)
                                            js.leaveGroup(op.param1)
                                            k4.findAndAddContactsByMid(jsMID)
                                            k4.inviteIntoGroup(op.param1,[jsMID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k4,k3)
            elif op.param3 in k4MID:
                try:
                    threading.Thread(target=kick,args=(k2,op.param1,op.param2,kickk,)).start()
                    k5.inviteIntoGroup(op.param1,[k4MID])
                    k4.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k3,op.param1,op.param2,kickk,)).start()
                        k1.inviteIntoGroup(op.param1,[k4MID])
                        k4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k5,op.param1,op.param2,kickk,)).start()
                            k2.inviteIntoGroup(op.param1,[k4MID])
                            k4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k1,op.param1,op.param2,kickk,)).start()
                                k3.inviteIntoGroup(op.param1,[k4MID])
                                k4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    js.acceptGroupInvitation(op.param1)
                                    js.inviteIntoGroup(op.param1,[c1MID,k1MID,k2MID,k3MID,k4MID,k5MID,js2MID])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    js.leaveGroup(op.param1)
                                    k5.inviteIntoGroup(op.param1,[jsMID])
                                except:
                                    try:
                                        k3.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js.acceptGroupInvitation(op.param1)
                                            kick(js,op.param1,op.param2,kickk)
                                            G = js.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js.updateGroup(G)
                                            Ticket = js.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js.updateGroup(G)
                                            js.leaveGroup(op.param1)
                                            k5.findAndAddContactsByMid(jsMID)
                                            k5.inviteIntoGroup(op.param1,[jsMID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k5,k4)
            elif op.param3 in k5MID:
                try:
                    threading.Thread(target=kick,args=(k3,op.param1,op.param2,kickk,)).start()
                    k1.inviteIntoGroup(op.param1,[k5MID])
                    k5.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k4,op.param1,op.param2,kickk,)).start()
                        k2.inviteIntoGroup(op.param1,[k5MID])
                        k5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k1,op.param1,op.param2,kickk,)).start()
                            k3.inviteIntoGroup(op.param1,[k5MID])
                            k5.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k2,op.param1,op.param2,kickk,)).start()
                                k4.inviteIntoGroup(op.param1,[k5MID])
                                k5.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    js.acceptGroupInvitation(op.param1)
                                    js.inviteIntoGroup(op.param1,[c1MID,k1MID,k2MID,k3MID,k4MID,k5MID,js2MID])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    js.leaveGroup(op.param1)
                                    k1.inviteIntoGroup(op.param1,[jsMID])
                                except:
                                    try:
                                        k4.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js.acceptGroupInvitation(op.param1)
                                            kick(js,op.param1,op.param2,kickk)
                                            G = js.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js.updateGroup(G)
                                            Ticket = js.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js.updateGroup(G)
                                            js.leaveGroup(op.param1)
                                            k1.findAndAddContactsByMid(jsMID)
                                            k1.inviteIntoGroup(op.param1,[jsMID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k1,k5)
            if op.param3 in clMID:
                try:
                    threading.Thread(target=kick,args=(k3,op.param1,op.param2,kickk,)).start()
                    k1.inviteIntoGroup(op.param1,[clMID])
                    cl.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k4,op.param1,op.param2,kickk,)).start()
                        k2.inviteIntoGroup(op.param1,[clMID])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k5,op.param1,op.param2,kickk,)).start()
                            k3.inviteIntoGroup(op.param1,[clMID])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k1,op.param1,op.param2,kickk,)).start()
                                k4.inviteIntoGroup(op.param1,[clMID])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    threading.Thread(target=kick,args=(k2,op.param1,op.param2,kickk,)).start()
                                    k5.inviteIntoGroup(op.param1,[clMID])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k5.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js2.acceptGroupInvitation(op.param1)
                                            kick(js2,op.param1,op.param2,kickk)
                                            G = js2.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js2.updateGroup(G)
                                            Ticket = js2.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js2.updateGroup(G)
                                            js2.leaveGroup(op.param1)
                                            cl.findAndAddContactsByMid(js2MID)
                                            cl.inviteIntoGroup(op.param1,[js2MID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k1,cl)
            elif op.param3 in k1MID:
                try:
                    threading.Thread(target=kick,args=(k4,op.param1,op.param2,kickk,)).start()
                    k2.inviteIntoGroup(op.param1,[k1MID])
                    k1.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k5,op.param1,op.param2,kickk,)).start()
                        k3.inviteIntoGroup(op.param1,[k1MID])
                        k1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k2,op.param1,op.param2,kickk,)).start()
                            k4.inviteIntoGroup(op.param1,[k1MID])
                            k1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k3,op.param1,op.param2,kickk,)).start()
                                k5.inviteIntoGroup(op.param1,[k1MID])
                                k1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    js2.acceptGroupInvitation(op.param1)
                                    js2.inviteIntoGroup(op.param1,[c1MID,k1MID,k2MID,k3MID,k4MID,k5MID,jsMID])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    js2.leaveGroup(op.param1)
                                    k2.inviteIntoGroup(op.param1,[js2MID])
                                except:
                                    try:
                                        k5.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js2.acceptGroupInvitation(op.param1)
                                            kick(js2,op.param1,op.param2,kickk)
                                            G = js2.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js2.updateGroup(G)
                                            Ticket = js2.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js2.updateGroup(G)
                                            js2.leaveGroup(op.param1)
                                            k2.findAndAddContactsByMid(js2MID)
                                            k2.inviteIntoGroup(op.param1,[js2MID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k2,k1)
                random.choice(set["bot1"]).cancelGroupInvitation(op.param1,[op.param2])
            elif op.param3 in k2MID:
                try:
                    threading.Thread(target=kick,args=(k5,op.param1,op.param2,kickk,)).start()
                    k3.inviteIntoGroup(op.param1,[k2MID])
                    k2.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k1,op.param1,op.param2,kickk,)).start()
                        k4.inviteIntoGroup(op.param1,[k2MID])
                        k2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k3,op.param1,op.param2,kickk,)).start()
                            k5.inviteIntoGroup(op.param1,[k2MID])
                            k2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k4,op.param1,op.param2,kickk,)).start()
                                k1.inviteIntoGroup(op.param1,[k2MID])
                                k2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    js2.acceptGroupInvitation(op.param1)
                                    js2.inviteIntoGroup(op.param1,[c1MID,k1MID,k2MID,k3MID,k4MID,k5MID,jsMID])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    js2.leaveGroup(op.param1)
                                    k3.inviteIntoGroup(op.param1,[js2MID])
                                except:
                                    try:
                                        k1.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js2.acceptGroupInvitation(op.param1)
                                            kick(js2,op.param1,op.param2,kickk)
                                            G = js2.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js2.updateGroup(G)
                                            Ticket = js2.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js2.updateGroup(G)
                                            js2.leaveGroup(op.param1)
                                            k3.findAndAddContactsByMid(js2MID)
                                            k3.inviteIntoGroup(op.param1,[js2MID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k3,k2)
            elif op.param3 in k3MID:
                try:
                    kthreading.Thread(target=kick,args=(k1,op.param1,op.param2,kickk,)).start()
                    k4.inviteIntoGroup(op.param1,[k3MID])
                    k3.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k2,op.param1,op.param2,kickk,)).start()
                        k5.inviteIntoGroup(op.param1,[k3MID])
                        k3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k4,op.param1,op.param2,kickk,)).start()
                            k1.inviteIntoGroup(op.param1,[k3MID])
                            k3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k5,op.param1,op.param2,kickk,)).start()
                                k2.inviteIntoGroup(op.param1,[k3MID])
                                k3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    js2.acceptGroupInvitation(op.param1)
                                    js2.inviteIntoGroup(op.param1,[c1MID,k1MID,k2MID,k3MID,k4MID,k5MID,jsMID])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    js2.leaveGroup(op.param1)
                                    k4.inviteIntoGroup(op.param1,[js2MID])
                                except:
                                    try:
                                        k2.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js2.acceptGroupInvitation(op.param1)
                                            kick(js2,op.param1,op.param2,kickk)
                                            G = js2.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js2.updateGroup(G)
                                            Ticket = js2.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js2.updateGroup(G)
                                            js2.leaveGroup(op.param1)
                                            k4.findAndAddContactsByMid(js2MID)
                                            k4.inviteIntoGroup(op.param1,[js2MID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k4,k3)
            elif op.param3 in k4MID:
                try:
                    threading.Thread(target=kick,args=(k2,op.param1,op.param2,kickk,)).start()
                    k5.inviteIntoGroup(op.param1,[k4MID])
                    k4.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k3,op.param1,op.param2,kickk,)).start()
                        k1.inviteIntoGroup(op.param1,[k4MID])
                        k4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k5,op.param1,op.param2,kickk,)).start()
                            k2.inviteIntoGroup(op.param1,[k4MID])
                            k4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k1,op.param1,op.param2,kickk,)).start()
                                k3.inviteIntoGroup(op.param1,[k4MID])
                                k4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    js2.acceptGroupInvitation(op.param1)
                                    js2.inviteIntoGroup(op.param1,[c1MID,k1MID,k2MID,k3MID,k4MID,k5MID,jsMID])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    js2.leaveGroup(op.param1)
                                    k5.inviteIntoGroup(op.param1,[js2MID])
                                except:
                                    try:
                                        k3.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js2.acceptGroupInvitation(op.param1)
                                            kick(js2,op.param1,op.param2,kickk)
                                            G = js2.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js2.updateGroup(G)
                                            Ticket = js2.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js2.updateGroup(G)
                                            js2.leaveGroup(op.param1)
                                            k5.findAndAddContactsByMid(js2MID)
                                            k5.inviteIntoGroup(op.param1,[js2MID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k5,k4)
            elif op.param3 in k5MID:
                try:
                    threading.Thread(target=kick,args=(k3,op.param1,op.param2,kickk,)).start()
                    k1.inviteIntoGroup(op.param1,[k5MID])
                    k5.acceptGroupInvitation(op.param1)
                except:
                    try:
                        threading.Thread(target=kick,args=(k4,op.param1,op.param2,kickk,)).start()
                        k2.inviteIntoGroup(op.param1,[k5MID])
                        k5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            threading.Thread(target=kick,args=(k1,op.param1,op.param2,kickk,)).start()
                            k3.inviteIntoGroup(op.param1,[k5MID])
                            k5.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                threading.Thread(target=kick,args=(k2,op.param1,op.param2,kickk,)).start()
                                k4.inviteIntoGroup(op.param1,[k5MID])
                                k5.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    js2.acceptGroupInvitation(op.param1)
                                    js2.inviteIntoGroup(op.param1,[c1MID,k1MID,k2MID,k3MID,k4MID,k5MID,jsMID])
                                    cl.acceptGroupInvitation(op.param1)
                                    k1.acceptGroupInvitation(op.param1)
                                    k2.acceptGroupInvitation(op.param1)
                                    k3.acceptGroupInvitation(op.param1)
                                    k4.acceptGroupInvitation(op.param1)
                                    k5.acceptGroupInvitation(op.param1)
                                    js2.leaveGroup(op.param1)
                                    k1.inviteIntoGroup(op.param1,[js2MID])
                                except:
                                    try:
                                        k4.sendMessage(op.param1,"limit")
                                        set["limit"]=True
                                    except:
                                        try:
                                            js2.acceptGroupInvitation(op.param1)
                                            kick(js2,op.param1,op.param2,kickk)
                                            G = js2.getGroupWithoutMembers(op.param1)
                                            G.preventedJoinByTicket = False
                                            js2.updateGroup(G)
                                            Ticket = js2.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G.preventedJoinByTicket = True
                                            js2.updateGroup(G)
                                            js2.leaveGroup(op.param1)
                                            k1.findAndAddContactsByMid(js2MID)
                                            k1.inviteIntoGroup(op.param1,[js2MID])
                                        except:
                                            pass
                                    else:
                                        backGroup(op.param1,k1,k5)
            elif op.param3 in ban["owners"]:
                try:
                    k5.findAndAddContactsByMid(op.param3)
                    k5.inviteIntoGroup(op.param1,[op.param3])
                except:
                    try:
                        k4.findAndAddContactsByMid(op.param3)
                        k4.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            k3.findAndAddContactsByMid(op.param3)
                            k3.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                k2.findAndAddContactsByMid(op.param3)
                                k2.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    k1.findAndAddContactsByMid(op.param3)
                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        pass                                        
        elif op.type == 13:
            if not cek(op.param2) and clMid in op.param3:
                js.rejectGroupInvitation(op.param1)
    except Exception as error:
        print(error)
def bot1run():
    while 1:
        try:
            ops = oepoll.singleTrace(count=50)
            if ops is not None:
                for op in ops:
                    lineBot(op)
                    oepoll.setRevision(op.revision)
        except:
            pass
def bot2IIrun():
    while 1:
        try:
            ops = oepolls.singleTrace(count=50)
            if ops is not None:
                for op in ops:
                    lineBot2II(op)
                    oepolls.setRevision(op.revision)
        except:
            pass
print("系統開始執行~")
threading.Thread(target=bot1run).start()
threading.Thread(target=bot2IIrun).start()
