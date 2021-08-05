from requests import get
from os.path import abspath, join
from os import system, remove
homePath = abspath('.')
downloadFrom = [
    r'http://mc.maryt.world:3513/',
    r'http://dovealliance.club:3513/',
    r'http://whoisdove.club:3513/'
]
updateDownloadFail = False
tryTime = 0    

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
        downloadVersionFile = get((url + 'version.txt'))
        versionFile = open(join(homePath, 'version.txt'), 'wb').write(downloadVersionFile.content)
    except:
        print('从'+ url +'获取版本列表失败。')
        tryTime += 1
    else:
        # 读取服务端发来的版本列表
        serverVersionFile = open(join(homePath, 'version.txt'), 'r')
        serverVersionList = serverVersionFile.readlines()
        serverVersionFile.close()
        remove(join(homePath, 'version.txt'))
        # 处理版本号列表
        for i in range(len(serverVersionList)):
            serverVersionList[i] = serverVersionList[i].strip()
        # 打开客户端配置文件
        clientVersionConfig = open(join(homePath, 'MyUpdateConfig.txt'), 'r')
        clientVersionText = (clientVersionConfig.readlines())[1]
        for i in range(len(clientVersionText)):
            if clientVersionText[i] == '=':
                break
        clientVersionNumber = clientVersionText[(i + 1) : (len(clientVersionText) - 1)]     
        for i in range(currentVersionNumber(serverVersionList), len(serverVersionList)):
            try:
                # system(r'.\wget.exe "'+ url + serverVersionList[i] +r'.exe"')
                updatePackage = open(join(homePath, (serverVersionList[i] + '.exe')), 'wb').write(get((url + (serverVersionList[i] + '.exe'))).content)
                system('.\\'+ serverVersionList[i] +r'.exe')
                remove(join(homePath, (serverVersionList[i] + '.exe')))
            except:
                print('从'+ url +'获取更新文件失败。')
                changeDownloadFlag()
                break
        print('更新已完成。')
        system('.\\' + 'start.exe')
        break
if updateDownloadFail or (tryTime >= len(downloadFrom)):
    print('更新失败，程序将退出。')
    system("pause")
