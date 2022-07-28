import os, img2pdf

chapters = os.listdir()
for chapter in chapters:
    pdf = open(f'{chapter}.pdf', 'wb')
    os.chdir(chapter)
    images = os.listdir()
    if images:
            imgs = img2pdf.convert(images)
            pdf.write(imgs);pdf.close()
    os.chdir(os.pardir)
