import requests
import re
import xlsxwriter
import time

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
    for i in range(5):
        ulist1.append(plt[i])
        ulist2.append(tlt[i])
        ulist3.append(blt[i])
    return ulist1,ulist2,ulist3



def main():
    workbook = xlsxwriter.Workbook('d:/'+time.strftime("%Y-%m-%d")+'.xlsx')  # 创建一个Excel文件
    worksheet = workbook.add_worksheet()  # 创建一个sheet
    #title = [U'交易类型', U'价格',U'单价','日期']  # 表格title
    #worksheet.write_row('A1',title)  # title 写入Excel
    infolist1 = []
    infolist2 = []
    infolist3 = []
    start_url = "http://s.5173.com/dnf-xptjnl-f10pkw-qrekgd-0-bx1xiv-0-0-0-a-a-a-a-a-0-itemprice_asc-0-0.shtml"
    html1 = getHTMLText(start_url)
    infolist1, infolist2, infolist3 = fillinformation(infolist1, infolist2, infolist3, html1)
    #for j in range(1, len(infolist1) + 1):
    for j in range(0, len(infolist1)):
        num0 = j + 1
        row = 'A' + str(num0)
        data = [infolist1[j], infolist2[j], infolist3[j],time.strftime("%Y-%m-%d")]
        worksheet.write_row(row, data)
        j += 1
    workbook.close()
main()