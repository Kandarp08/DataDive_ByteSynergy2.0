# This program converts the images of tables into excel sheets. Thse sheets are stored in the folder ExcelSheets
# Note: This program would take several minutes to run due to large amount of processing involved.

import os
from img2table.document import Image
from img2table.ocr import TesseractOCR

ocr = TesseractOCR(lang = "eng")

# These folders contain the images of tables.
folder_list = ["113_163", "164_213", "214_263", "264_313", "314_361"]
counter = 1

# Iterate through each folder
for folder in folder_list:
        
    image_list = os.listdir("./Images/" + folder + "/")

    # Iterate through each image in the folder
    for image in image_list:

        img = Image(src = "./Images/" + folder + "/" + image)
                
        img.to_xlsx(dest = f"./ExcelSheets/Table{counter}.xlsx", ocr = ocr) # Convert image to excel file
        counter += 1

        print(image + "Processed")