# DataDive_ByteSynergy2.0
First run the below command to download the dependencies for the code

    pip install requirement.txt

Part 1 : Convert the scanned data into Excel sheet :

1. First, we split the pdf file into five different pdf files and converted them into images using the ilovepdf website.
2. Then using the img2table library which uses OCR(optical character recognition) to convert these images into excel sheets.

Part 2 : Creating Lookup table :

1. For creating the lookup table, we extensively used the OpenPyXL library.
2. We have read the Excel files using the library and then written the data into the output Excel sheet, where the district is the row, and then all the columns are there, corresponding to each row entry.

Part 3 : Finding dependencies between different excel sheet and making it user accessible

1. First we trained our ML model by various government reports and data.
2. Then we use it for finding depencies realation between excel sheet.
3. Now for showing the data to the user, we took the help of Panda's library, in which we are taking input from the user, which is table no., and then showing the data of the table in the terminal.
