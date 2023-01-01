from PIL import Image

I = Image.open('2.jpg')  # 2不需要修改
I1 = Image.open('1.jpg')  # 1.jpg是别人的集赞截图
I2 = Image.open('1.jpg')  # 需要复制粘贴进去后，修改图片名字
box = (0, 0, 170, 420)
I=I.crop(box)
# I1=I1.crop(box)
# box = (0, 420, 1080, 780)
# I2 = I2.crop(box)
# I.paste(I1, box=(180, 354))
# I.paste(I2, box=(0, 420))
# I.save('result.jpg')
I.show()