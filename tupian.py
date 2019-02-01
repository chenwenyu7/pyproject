import requests
import os
url = "http://img.bimg.126.net/photo/ZZ5EGyuUCp9hBPk6_s4Ehg==/5727171351132208489.jpg"
root = "D://1tu//"
path = root + url.split("/")[-1]
try:
    if not os.path .exists (root):
        os.mkdir(root)
    if not os.path.exists(path ):
        r = requests.get(url )
        with open(path,'wb') as f:
            f.write(r.content )
            f.close()
            print ("保存完成")
    else:
        print("文件已存在")
except:
    print("捕捉错误")
