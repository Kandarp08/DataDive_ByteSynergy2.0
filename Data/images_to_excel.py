import os

from img2table.document import Image
from img2table.ocr import TesseractOCR

ocr = TesseractOCR(lang = "eng")

folder_list = ["113_163", "164_213", "214_263", "264_313", "314_361"]
counter = 1

for folder in folder_list:
        
    image_list = os.listdir("./Images/" + folder + "/")

    for image in image_list:

        img = Image(src = "./Images/" + folder + "/" + image)
                
        img.to_xlsx(dest = f"./ExcelSheets/Table{counter}.xlsx", ocr = ocr)
        counter += 1

        print(image + "Processed")