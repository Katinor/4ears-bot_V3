import time, os, glob


LOG_PATH = "log/quadra_bot_log"
if not os.path.exists('log'):
    os.makedirs(os.path.join('log'))

fp = open(LOG_PATH+".txt", 'a')
fp.close()


def log_append(user = None, guild = None, category = None, text = None, level = 0):
    _now = time.localtime()

    if level == 1: temp_level = "[WARN]"
    elif level == 2: temp_level = "[EROR]"
    else: temp_level = "[INFO]"

    target = temp_level + "[%04d-%02d-%02d %02d:%02d:%02d]" % (_now.tm_year, _now.tm_mon, _now.tm_mday, _now.tm_hour, _now.tm_min, _now.tm_sec)
    if user:
        target += "triggered by : "+user.name + "#" + user.discriminator + " (id:"+str(user.id)+")"
    else:
        target += "triggered by System"

    print("#0 - " + target)
    text_target = target + " / "

    if guild:
        target = "from : " + guild.name + " (id:"+str(guild.id)+")"
        print("#1 - " + target)
        text_target += target + " / "
    else:
        print("#1 - from None")

    target = ""
    if category:
        target += "category = " + category
    target += " : "
    if text:
        target += text

    print("#2 - " + target)
    text_target += target

    if os.path.getsize(LOG_PATH+".txt") >= 102400:
        filelist = glob.glob("log/*.*")
        filenum = len(filelist)
        filename = LOG_PATH+"_"+str(filenum)+".txt"
        os.rename(LOG_PATH+".txt",filename)
    fp = open(LOG_PATH+".txt", 'a')
    fp.write(text_target+"\n")
    fp.close()

    return _now

    