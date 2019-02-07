import requests
import re
import xlsxwriter

def getHTMLText(url):
    try:
        res = requests.get(url,timeout = 30)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text
    except:
        return ""

def fillinformation(ulist1,ulist2,ulist3,html):
    ulist1 = []
    ulist2 = []
    ulist3 = []
    plt = re.findall(r'\【..交易\】.*元',html)
    tlt = re.findall(r'1元=.*?万金币',html)
    blt = re.findall(r'0\..*元/万金币',html)
    print(len(plt))
    for i in range(len(plt)):
        ulist1.append(plt[i])
        ulist2.append(tlt[i])
        ulist3.append(blt[i])
    return ulist1,ulist2,ulist3


def printGoodinfo(ulist1,ulist2,ulist3):
    moban = ("{0:<15}\t{1:{3}^10}\t{2:{3}^10}")
    print(moban.format("交易类型","价格","单价",chr(12288)))
    for u in range(40):
        print(moban.format(ulist1[u],ulist2[u],ulist3[u],chr(12288)))

def main():
    workbook = xlsxwriter.Workbook('d:/5173.xlsx')  # 创建一个Excel文件
    worksheet = workbook.add_worksheet()  # 创建一个sheet
    title = [U'交易类型', U'价格', U'单价']  # 表格title
    worksheet.write_row('A1', title)  # title 写入Excel
    page = 1

    infolist1 = []
    infolist2 = []
    infolist3 = []
    depth = 1
    for i in range(depth):
        start_url = "http://s.5173.com/dnf-xptjnl-f10pkw-qrekgd-0-bx1xiv-0-0-0-a-a-a-a-a-0-0-0-" + str(page) + ".shtml"
        html1 = getHTMLText(start_url)
        page += 1
        infolist1,infolist2,infolist3 = fillinformation(infolist1,infolist2,infolist3,html1)
        printGoodinfo(infolist1,infolist2,infolist3)
        for j in range(len(infolist1)):
            num0 = j + 1
            row = 'A' + str(num0)
            data = [infolist1[j], infolist2[j],infolist3[j] ]
            worksheet.write_row(row, data)
            j += 1
    workbook.close()
main()