import requests
import tkinter as tk
from urllib import parse
import os, sys
from PIL import ImageTk		# pip install --upgrade Pillow
from base64 import b64decode

def download_file(result, num):
    cookie = {
        "Cookie": "Hm_lvt_7d2469592a25c577fe82de8e71a5ae60=1650630029,1650632573,1650762170,1650771418; Hm_lpvt_7d2469592a25c577fe82de8e71a5ae60=1650771423"}
    head = {
        "Web-Agent": "web",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    '''header中有一条参数必须要，不确定，（懒得去试了，）不然会被屏蔽请求'''
    print(parse.quote(result), type(parse.quote(result)))
    url = 'https://www.dbbqb.com/api/search/json??start={100}&w={%s}' % parse.quote(result)
    url_img = "http://image.dbbqb.com/"  # 202204241523/04ba69bd460aaf922256711e5912b2ff/DGyoE
    '''图片的数据库加上请求到的100条path就直接能拿到100张jpg'''
    param = {"size": "%d" % int(num)}
    resp = requests.get(url, headers=head, params=param).json()  # 拿到的是一个列表，列表里面的有100条字典转载数据
    path = []
    id_ = []
    j = 1
    print(resp)
    for i in resp:
        # path.append(i.get("path"))
        # print(path)
        #    id_.append(i.get("id"))
        imgresp = requests.get(url_img + i.get("path")).content
        # print(imgresp)
        # title = (i.get("id"))
        path = "./表情包/" + result + "/"
        if not os.path.isdir(path):
            os.makedirs(path)
        with open("{}{}.gif".format(path, str(j) + "_" + result), "wb") as f:
            f.write(imgresp)
            print("保存成功")
            f.close()
        j+=1
    sys.exit(0)

def enter():
   root=tk.Tk()
   root.title("表情包仓库")
   icon_img = b'AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAA4lcP/PpG6/0uUuv9Kkbn/Ro61/1Sqz/9Vocb/VqfM/1aqzv+p3PD/nsnf/3Cju/+FrMP/dZau/1GAl/9LkLD/XpOr/4+xxv+Hs8r/irHM/56/1f+dxtv/oc3k/4TA1P9VrNH/Uq3U/0miyP8+l8L/T7rk/1C55f8xgan/OZXA/z2Wxf9Elbz/QZa8/02cw/9MlLv/VqnN/1Kjxv9Tq8//YLLT/7Db7f+UxNn/Zpu3/2aOo/9ijKT/apGj/2WqxP9qnrX/k7vP/4DL5f9/q8X/mL3U/6bN5P+Fzuf/aLDI/1CnzP9SqM3/TrXa/z2x3f9Josv/Sa7Z/z6Zw/9Gq9b/S6bR/0iWvf9InML/VazS/02bwf9Rpsr/XbXW/06dwP9fttj/n9fp/6DN1/97tsv/gaq+/2mZsf9rl6n/dJqt/3OYrv+Ossf/i8Xe/2Wguf+exNr/ps3k/5jJ3f9cutj/S7LZ/1Okyv9PveH/TLrf/1Ox1f8+qNL/P5O//0So0v9EnMX/S6TM/0+jyf9dsdb/UZ/E/1qmyP9mvdz/UJ/C/1642v91yOH/uOnu/4e2xP+Nt8n/apWs/2KQpP+Cq7//aZew/5O4z/+fw9j/h7PK/53A1/+01ez/mc7g/1av0v9Yud//SZi9/0SZwv9BpdD/RazX/0qv2P8/rtn/O6/c/1Oix/9ZrND/SqzS/2Cr0f9iq8//XKzP/1+qzf9Xp8v/YLzg/1my1/9wuM//k7/O/467z/92n7X/YY6j/5G1yf91tND/hcfh/5G+1f+Uu9P/ocXd/7bZ7v99u9L/XLDU/2C52P9SrdD/TafO/1Cq0P9UsNr/SrTd/0Ov1v9IptH/abXR/1WozP9NpMf/WK3S/1uqzf9Vt97/UKjM/1mu0v9Ut9z/Y7rd/1uoyv+Husz/jbrO/3mkuv9tl63/j7HE/3mtx/+Txd3/ncDZ/421zv+exd3/pM3f/2uzzv9WsdT/ZLbV/1iz2f9Nps7/RZe8/1yy1v9Uq8//UJ/D/1Ww1f9Nud//UKbM/1uw1P9VrNH/WabI/1i12P9Xs9f/UrDX/1G64v9iut3/WKXG/3+4zv+Quc7/i7PJ/22ds/+MtMn/i7HG/5y+1f+kwNj/ncHY/5vB1/+JwNP/WbfV/1q73/9pv+D/V7rg/1S24P9Sq9L/WLfd/1Ky2v9Locj/V7XY/1Wr0P9YrtP/Vbnh/2Osz/9kq8r/Xa/R/1yv1v9esdP/V7jd/2G73v9bp8r/fL3Y/4u70v94q8b/dqK4/4u0y/+SuNH/hKvE/4m20v+QxOH/ksPd/3nJ3v9ar8//ZLnc/1u63f9artX/W6/V/1Cpzf9QtNv/Q7vm/1epzv9Rqs3/YLDS/1+rzf9StNn/aLbZ/1qv0v9Xvt7/Vsjr/1i73f9dsdT/XLjc/1is0f94vNf/isDU/3irxP9/oLn/hae+/5e4zf97nsD/bI68/4fC4/+Qw9b/Y7LM/1qryv9httr/YLfb/1uoy/9cqsz/WrHV/1S23P9TrtT/WajN/1qt0f9fqs//X77j/0q33v9huNz/Yrja/2HD4f9Pvt7/Tbrf/1yz1v9gu9//X7XY/1+32v+Ewtj/bqXA/1WFq/9llLD/ganA/3agwv9bmMP/erba/3670v9Wo8H/ZLrb/1611/9YvuP/VbDW/1ijxP9fstP/W7LV/1ax1P9XpMr/XazR/12v1/9buOL/UrPY/13E4/9dtt3/Vq/T/1m83f9Xv+T/XLne/2e32/9rudv/V6/W/1yw0/9Ym8D/XJrI/1yjyP9wpsP/nsbe/3ityv+ayeT/eLPO/2Sv0P9cuN3/X7fb/1mz1f9MveL/WK7S/1Wgxf9PtNr/Tq3R/1GmzP9QoMb/UqnS/1er0P9hsdX/Wrne/1rC7P9gvN7/Z7bY/1O22v9Vut//XLLW/1TF7f9Xu+H/fLjY/3+qx/+BstT/bqzN/4O31P+axNv/g7fT/3ux0P+Z0OX/arPR/1mu1P9ft9z/WqDC/1av0f9audv/W6rQ/0y02/9Jstj/T63S/1Ot0v9Xs9f/YLjb/1602v9nwuH/aLXU/2a42/9ks9b/X7rc/1q12P9hsdX/XLfZ/2e21/97vN3/cqzN/3y21f9uwuD/hb7Y/5vJ4/+BttT/a7jb/5bJ4f9hr8//Xq7Q/2Gt0f9epcn/YazQ/16pzP9jttn/W7PY/1O63v9Xs9b/XrLU/1nK6v9YueD/Ua/V/0rP9P9YwOf/Xbvf/2Gx1f9jt9v/Xrba/13B4f9ZvuD/abvd/3S84P9jt9r/iLfT/4/J4/9vvt//j8fi/4Wvyv92udr/eL7e/1erz/9Yqs7/XKLH/2Ov0/9apcn/YqrN/1qpzf9cr9P/VKfL/1qszf9js9P/V7PY/2G+4P9Zs9f/VrPb/1G02f9ZvuH/Yrjc/2PA4v9lt9r/V63S/1i/4P9msdL/iL7f/3m94f+MvtT/nMPa/2nA4v9/zej/jb7a/3iw1P+Eyef/YLfb/1ux1f9bpcn/XavR/1Gq0P9dpsj/XKzQ/1yr0P9aqs3/VK3P/13A3/9cvuP/aLzg/1u43v9iv+L/arjb/2LA4/9iwej/XK/W/2e73/9duN3/V6bJ/2mt0P+TweP/Zo+2/3vA3P+Txt//nMbc/5zS6f9whqb/Y5i+/5LQ7v9esdT/ZK3R/2Gr0P9ittX/YsHf/1iq0f9frdX/XqjQ/2C83/9avN7/VrLW/1S64f9Tven/XL/p/2DA6f9gvOP/XLPZ/1y44v9guOX/YcDr/1jB8P9UueT/arrf/4qz2P9JRmn/kqC7/5XB3f+At9L/g5u6/110kP99x9v/gMvq/1elzf9ir9L/Zbvf/1m64f9as9//W7Db/1ez3v9VtuH/YL3l/12x2f9OrNj/Vbnk/1i04f9Vsd//WbPg/2i83/9es93/W7Pa/1i64/9dvub/Urrm/1Wy3f9dvub/ebTc/z0zVv80J0X/ZXal/3ur0/9ScZL/Pj5i/4S21P9nzvX/XbDZ/1u64f9Tst3/Vbbl/1e25P9it9f/WrDW/1i94v9Ts+D/VqfW/1K04v9SvOr/VrXi/1iv3v9Us+L/X8nv/1265f9bsNr/Yb/j/2C+5P9WtOD/WbLd/1vE8/9yvub/MyNB/y01Vv9hjsH/bIC4/0paff9Zbo3/jsTo/2fH7/9ewev/Vb/u/1K87v9UsuP/XLjm/1y85/9Zsd3/V7bj/06p2/9Qq9r/Vq7e/1K05P9hveP/W7zi/1fE8P9Qwuz/Vbnn/1XF8v9byfD/W8Ht/1W56v9avu//VL/t/2vC6/8rIUH/aoqz/3Gv3v+Dm83/cISr/zk7XP+ExOv/Xbrl/1W56v9Ovuf/VLji/1e44/9WtuX/Tr/x/1S87/9UsOH/UKbT/1Ks2v9Ot+j/TL/z/1jF7/9Qrdv/TIy2/1SdxP9On8r/T5/G/0+gy/9au+r/VKfX/1em0/9Wrt7/ZLTk/zk9Zf9WWov/bnmq/25/rP9ocp//REdv/3TA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'
   # 这里替换成你自己图标文件的二进制数据
   icon_img = b64decode(icon_img)
   icon_img = ImageTk.PhotoImage(data=icon_img)
   root.tk.call('wm', 'iconphoto', root._w, icon_img)
   lab_1=tk.Label(root,text="欢迎来到表情包的世界, 接下来请尽情驰骋吧！")
   but_dr=tk.Button(root,text="确定",command=root.destroy)
   lab_1.grid(row=0,column=0)
   but_dr.grid(row=1,column=1)
   root.mainloop()


def get_result():
    # 第1步，建立窗口window
    window = tk.Tk()  # 建立窗口window

    # 第2步，给窗口起名称
    window.title('表情包仓库')  # 窗口名称

    # 第3步，设定窗口的大小(长＊宽)
    window.geometry("400x240")  # 窗口大小(长＊宽)

    icon_img = b'AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAA4lcP/PpG6/0uUuv9Kkbn/Ro61/1Sqz/9Vocb/VqfM/1aqzv+p3PD/nsnf/3Cju/+FrMP/dZau/1GAl/9LkLD/XpOr/4+xxv+Hs8r/irHM/56/1f+dxtv/oc3k/4TA1P9VrNH/Uq3U/0miyP8+l8L/T7rk/1C55f8xgan/OZXA/z2Wxf9Elbz/QZa8/02cw/9MlLv/VqnN/1Kjxv9Tq8//YLLT/7Db7f+UxNn/Zpu3/2aOo/9ijKT/apGj/2WqxP9qnrX/k7vP/4DL5f9/q8X/mL3U/6bN5P+Fzuf/aLDI/1CnzP9SqM3/TrXa/z2x3f9Josv/Sa7Z/z6Zw/9Gq9b/S6bR/0iWvf9InML/VazS/02bwf9Rpsr/XbXW/06dwP9fttj/n9fp/6DN1/97tsv/gaq+/2mZsf9rl6n/dJqt/3OYrv+Ossf/i8Xe/2Wguf+exNr/ps3k/5jJ3f9cutj/S7LZ/1Okyv9PveH/TLrf/1Ox1f8+qNL/P5O//0So0v9EnMX/S6TM/0+jyf9dsdb/UZ/E/1qmyP9mvdz/UJ/C/1642v91yOH/uOnu/4e2xP+Nt8n/apWs/2KQpP+Cq7//aZew/5O4z/+fw9j/h7PK/53A1/+01ez/mc7g/1av0v9Yud//SZi9/0SZwv9BpdD/RazX/0qv2P8/rtn/O6/c/1Oix/9ZrND/SqzS/2Cr0f9iq8//XKzP/1+qzf9Xp8v/YLzg/1my1/9wuM//k7/O/467z/92n7X/YY6j/5G1yf91tND/hcfh/5G+1f+Uu9P/ocXd/7bZ7v99u9L/XLDU/2C52P9SrdD/TafO/1Cq0P9UsNr/SrTd/0Ov1v9IptH/abXR/1WozP9NpMf/WK3S/1uqzf9Vt97/UKjM/1mu0v9Ut9z/Y7rd/1uoyv+Husz/jbrO/3mkuv9tl63/j7HE/3mtx/+Txd3/ncDZ/421zv+exd3/pM3f/2uzzv9WsdT/ZLbV/1iz2f9Nps7/RZe8/1yy1v9Uq8//UJ/D/1Ww1f9Nud//UKbM/1uw1P9VrNH/WabI/1i12P9Xs9f/UrDX/1G64v9iut3/WKXG/3+4zv+Quc7/i7PJ/22ds/+MtMn/i7HG/5y+1f+kwNj/ncHY/5vB1/+JwNP/WbfV/1q73/9pv+D/V7rg/1S24P9Sq9L/WLfd/1Ky2v9Locj/V7XY/1Wr0P9YrtP/Vbnh/2Osz/9kq8r/Xa/R/1yv1v9esdP/V7jd/2G73v9bp8r/fL3Y/4u70v94q8b/dqK4/4u0y/+SuNH/hKvE/4m20v+QxOH/ksPd/3nJ3v9ar8//ZLnc/1u63f9artX/W6/V/1Cpzf9QtNv/Q7vm/1epzv9Rqs3/YLDS/1+rzf9StNn/aLbZ/1qv0v9Xvt7/Vsjr/1i73f9dsdT/XLjc/1is0f94vNf/isDU/3irxP9/oLn/hae+/5e4zf97nsD/bI68/4fC4/+Qw9b/Y7LM/1qryv9httr/YLfb/1uoy/9cqsz/WrHV/1S23P9TrtT/WajN/1qt0f9fqs//X77j/0q33v9huNz/Yrja/2HD4f9Pvt7/Tbrf/1yz1v9gu9//X7XY/1+32v+Ewtj/bqXA/1WFq/9llLD/ganA/3agwv9bmMP/erba/3670v9Wo8H/ZLrb/1611/9YvuP/VbDW/1ijxP9fstP/W7LV/1ax1P9XpMr/XazR/12v1/9buOL/UrPY/13E4/9dtt3/Vq/T/1m83f9Xv+T/XLne/2e32/9rudv/V6/W/1yw0/9Ym8D/XJrI/1yjyP9wpsP/nsbe/3ityv+ayeT/eLPO/2Sv0P9cuN3/X7fb/1mz1f9MveL/WK7S/1Wgxf9PtNr/Tq3R/1GmzP9QoMb/UqnS/1er0P9hsdX/Wrne/1rC7P9gvN7/Z7bY/1O22v9Vut//XLLW/1TF7f9Xu+H/fLjY/3+qx/+BstT/bqzN/4O31P+axNv/g7fT/3ux0P+Z0OX/arPR/1mu1P9ft9z/WqDC/1av0f9audv/W6rQ/0y02/9Jstj/T63S/1Ot0v9Xs9f/YLjb/1602v9nwuH/aLXU/2a42/9ks9b/X7rc/1q12P9hsdX/XLfZ/2e21/97vN3/cqzN/3y21f9uwuD/hb7Y/5vJ4/+BttT/a7jb/5bJ4f9hr8//Xq7Q/2Gt0f9epcn/YazQ/16pzP9jttn/W7PY/1O63v9Xs9b/XrLU/1nK6v9YueD/Ua/V/0rP9P9YwOf/Xbvf/2Gx1f9jt9v/Xrba/13B4f9ZvuD/abvd/3S84P9jt9r/iLfT/4/J4/9vvt//j8fi/4Wvyv92udr/eL7e/1erz/9Yqs7/XKLH/2Ov0/9apcn/YqrN/1qpzf9cr9P/VKfL/1qszf9js9P/V7PY/2G+4P9Zs9f/VrPb/1G02f9ZvuH/Yrjc/2PA4v9lt9r/V63S/1i/4P9msdL/iL7f/3m94f+MvtT/nMPa/2nA4v9/zej/jb7a/3iw1P+Eyef/YLfb/1ux1f9bpcn/XavR/1Gq0P9dpsj/XKzQ/1yr0P9aqs3/VK3P/13A3/9cvuP/aLzg/1u43v9iv+L/arjb/2LA4/9iwej/XK/W/2e73/9duN3/V6bJ/2mt0P+TweP/Zo+2/3vA3P+Txt//nMbc/5zS6f9whqb/Y5i+/5LQ7v9esdT/ZK3R/2Gr0P9ittX/YsHf/1iq0f9frdX/XqjQ/2C83/9avN7/VrLW/1S64f9Tven/XL/p/2DA6f9gvOP/XLPZ/1y44v9guOX/YcDr/1jB8P9UueT/arrf/4qz2P9JRmn/kqC7/5XB3f+At9L/g5u6/110kP99x9v/gMvq/1elzf9ir9L/Zbvf/1m64f9as9//W7Db/1ez3v9VtuH/YL3l/12x2f9OrNj/Vbnk/1i04f9Vsd//WbPg/2i83/9es93/W7Pa/1i64/9dvub/Urrm/1Wy3f9dvub/ebTc/z0zVv80J0X/ZXal/3ur0/9ScZL/Pj5i/4S21P9nzvX/XbDZ/1u64f9Tst3/Vbbl/1e25P9it9f/WrDW/1i94v9Ts+D/VqfW/1K04v9SvOr/VrXi/1iv3v9Us+L/X8nv/1265f9bsNr/Yb/j/2C+5P9WtOD/WbLd/1vE8/9yvub/MyNB/y01Vv9hjsH/bIC4/0paff9Zbo3/jsTo/2fH7/9ewev/Vb/u/1K87v9UsuP/XLjm/1y85/9Zsd3/V7bj/06p2/9Qq9r/Vq7e/1K05P9hveP/W7zi/1fE8P9Qwuz/Vbnn/1XF8v9byfD/W8Ht/1W56v9avu//VL/t/2vC6/8rIUH/aoqz/3Gv3v+Dm83/cISr/zk7XP+ExOv/Xbrl/1W56v9Ovuf/VLji/1e44/9WtuX/Tr/x/1S87/9UsOH/UKbT/1Ks2v9Ot+j/TL/z/1jF7/9Qrdv/TIy2/1SdxP9On8r/T5/G/0+gy/9au+r/VKfX/1em0/9Wrt7/ZLTk/zk9Zf9WWov/bnmq/25/rP9ocp//REdv/3TA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'
  # 这里替换成你自己图标文件的二进制数据
    icon_img = b64decode(icon_img)
    icon_img = ImageTk.PhotoImage(data=icon_img)
    window.tk.call('wm', 'iconphoto', window._w, icon_img)

    # 第4步，在图形化界面上设定一个文本框
    textExample = tk.Text(window, height=5)  # 创建文本输入框

    # 第5步，安置文本框
    textExample.pack()  # 把Text放在window上面，显示Text这个控件

    def1 = "请输入您要查找的表情包类型:"
    textExample.insert(tk.END, def1)

    textExample2 = tk.Text(window, height=5)  # 创建文本输入框

    # 第5步，安置文本框
    textExample2.pack()  # 把Text放在window上面，显示Text这个控件

    def2 = "请输入您要下载的表情包数量:"
    textExample2.insert(tk.END, def2)

    # 第6步，获取文本框输入
    def getTextInput():
        result = textExample.get("1.0", "end")  # 获取文本输入框的内容
        num = textExample2.get("1.0", "end")  # 获取文本输入框的内容
        result = result.split(":")[1]
        num = num.split(":")[1]
        download_file(result.strip(), num.strip())

    # Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
    # "end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。

    # 第7步，在图形化界面上设定一个button按钮（#command绑定获取文本框内容的方法）
    btnRead = tk.Button(window, height=1, width=10, text="确定", command=getTextInput)  # command绑定获取文本框内容的方法

    # 第8步，安置按钮
    btnRead.pack()  # 显示按钮

    # 第9步，
    window.mainloop()  # 显示窗口

if __name__ == '__main__':
    enter()
    get_result()

    # import base64
    #
    # with open('1.ico', 'rb') as open_icon:
    #     b64str = base64.b64encode(open_icon.read())
    #     print(b64str)