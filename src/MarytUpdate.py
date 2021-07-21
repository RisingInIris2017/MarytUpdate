import wget
import os
homePath = os.path.abspath('.')
downloadFrom = [
    r'http://mc.maryt.world:3513/version.txt',
    r'http://dovealliance.club:3513/version.txt',
    r'http://whoisdove.club:3513/version.txt'
]
updateDownloadFail = False
tryTime = 0
# if os.path.exists(filename):
#         

def changeDownloadFlag():
    global updateDownloadFail
    updateDownloadFail = True
def currentVersionNumber(serverVersionList):
    for i in range(len(serverVersionList)):
        if clientVersionNumber == serverVersionList[i]:
            diffNumber = len(serverVersionList) - (i + 1)
            if diffNumber:
                print('你的客户端版本为第'+ str(i + 1) +'个版本，落后服务端'+ str(diffNumber) + '个版本。')
                return (i + 1)
            else:
                print('你的客户端已经为最新版本！')
                return len(serverVersionList)

for url in downloadFrom:
    try:
        versionFile = wget.download(url, os.path.join(homePath, 'version.txt'))
    except:
        print('从'+url+'获取版本列表失败。')
        tryTime += 1
    else:
        # 读取服务端发来的版本列表
        serverVersionFile = open(versionFile, 'r')
        serverVersionList = serverVersionFile.readlines()
        serverVersionFile.close()
        os.remove(os.path.join(homePath, 'version.txt'))
        # 处理版本号列表
        for i in range(len(serverVersionList)):
            serverVersionList[i] = serverVersionList[i].strip()
        # 打开客户端配置文件
        clientVersionConfig = open(os.path.join(homePath, 'MyUpdateConfig.txt'), 'r')
        clientVersionText = (clientVersionConfig.readlines())[1]
        for i in range(len(clientVersionText)):
            if clientVersionText[i] == '=':
                break
        clientVersionNumber = clientVersionText[(i + 1) : (len(clientVersionText) - 1)]     
        for i in range(currentVersionNumber(serverVersionList), len(serverVersionList)):
            try:
                os.system(r'.\wget.exe "mc.maryt.world:3513/'+ serverVersionList[i] +r'.exe"')
                os.system('.\\'+ serverVersionList[i] +r'.exe')
                os.remove(os.path.join(homePath, (serverVersionList[i] + '.exe')))
            except:
                print('从'+ url +'获取更新文件失败。')
                changeDownloadFlag()
                break
        print('更新已完成。')
        break
if updateDownloadFail or (tryTime >= len(downloadFrom)):
    print('更新失败，程序将退出。')
