#! /usr/bin/env python 
#-*-coding:utf-8-*-
#Python 生成启动日志头
#
#使用方法：
#with open(__path__[0]+"/header.txt", 'r') as file:
#    header = file.readlines()
#    print("".join(header))
#
#
#需准备logo文件，像素200*200或其他尺寸为1：1的logo图，命名配置如下：
INPUT_IMG = "logo.jpg" #支持jpg，png格式图片，名字修改为对应名字
RESULT_TXT = "header.txt"

#修改如下配置项，每行显示30个中文（60个英文），description和remarks最多3行，总项不超过90个字符（90个中文和180个英文含标点）
INPUT = {
"company": "2014-2019 www.xxx.cn All Rights Reserved",  # 公司版权名
"name": "Project_name",                                 # 项目名
"author": "Xiao Dawei",                                 # 作者
"version": "2.0.0",                                     # 版本号
"description" :"--",                                    # 描述
"date":"2019-10-26",                                    # 日期
"remarks":"--"                                          # 备注        
}


from PIL import Image

WIDTH = 60
HEIGHT = 30
# ascii列表，将其与图片像素对应
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.  ")

# 将256个灰度值映射到字符列表中的字符
def get_char_from_pixel(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


# 使用PIL库对图片进行转换
def ascii_pic_from_pil(path):
    text = ""

    im = Image.open(path)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    for h in range(im.size[1]):     # 图片像素纵坐标
        for w in range(im.size[0]): # 图片像素横坐标
            text += get_char_from_pixel(*im.getpixel((w, h)))
        text += '\n'
    return text
    
# 保存txt文件
def save_to_file(filename, pic_str):
    with open(filename, 'w') as f:
        f.write(pic_str)


def readchar(path):
    result =""
    with open(path, 'r') as f:
        text_lines = f.readlines()
        for i in range(len(text_lines)):
            if i  in (2,27):
                blank_char = "#"*88
                result+=text_lines[i][0:-2]
                result+=blank_char
                result+= "\n"
            elif i  in (3,28):
                blank_char = "#"*88
                result+=text_lines[i][0:-2]
                result+=blank_char
                result+= "\n"
            elif 6 == i :
                result+=text_lines[i][0:-2]
                result+= "   Copyright (C) %s" % INPUT['company']
                result+= "\n"
            elif 9 == i :
                result+=text_lines[i][0:-2]
                result+= "   Name: %s" % INPUT['name']
                result+= "\n"                
            elif 12 == i :
                result+=text_lines[i][0:-2]
                result+= "   Author: %s" % INPUT['author']
                result+= "\n"
            elif 15 == i :
                result+=text_lines[i][0:-2]
                result+= "   Version: %s" % INPUT['version']
                result+= "\n"
            elif 18 == i :
                result+=text_lines[i][0:-2]
                result+= "   Descripiton: %s" % INPUT['description'][0:30]
                result+= "\n"
            elif 19 == i :
                result+=text_lines[i][0:-2]
                result+= "                %s" % INPUT['description'][30:60]
                result+= "\n"
            elif 20 == i :
                result+=text_lines[i][0:-2]
                result+= "                %s" % INPUT['description'][60:90]
                result+= "\n"
            elif 21 == i :
                result+=text_lines[i][0:-2]
                result+= "   Date: %s" % INPUT['date']
                result+= "\n"
            elif 24 == i :
                result+=text_lines[i][0:-2]
                result+= "   Remarks: %s" % INPUT['remarks'][0:30]
                result+= "\n"
            elif 25 == i :
                result+=text_lines[i][0:-2]
                result+= "            %s" % INPUT['remarks'][30:60]
                result+= "\n"
            elif 26 == i :
                result+=text_lines[i][0:-2]
                result+= "            %s" % INPUT['remarks'][60:90]
                result+= "\n"
            else:
                result+=text_lines[i]
            # print(result)
        return result


if __name__ == '__main__':
    img = ascii_pic_from_pil(INPUT_IMG)
    save_to_file('pil.txt', img)
    result = readchar('pil.txt')
    save_to_file(RESULT_TXT,result)