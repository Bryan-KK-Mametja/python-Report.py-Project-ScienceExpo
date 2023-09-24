print("Multi-purpose command prompt by Bryan Kgoana Mametja")
print("2022 Eskom Expo")
print("Enter (help) for help")
while True:
    command = input(">>>>_* ")
    if command == "help":
        print("First enter the key-word [report] to the prompt and select the excel file you would like to report using the file-dialog.")
        print("The report has multiple keys that have sub-keys.\n")
        print("Keys and their sub-keys:\n")
        print("[clean]-to clear the data to make it easier for the prompt to work with. You will be asked for a cleaning method of your choice.")
        print("The cleaning methods:")
        print("--[nan] to clean the data of any Nan values")
        print("--[str-to-int] to convert string values to intergers so the prompt is able to read it. For example converting (No) to (0) and (Yes) to (1).")
        print("--[done] to save the cleaned version of the file and use it later.\n")
        print("[show-index]-to iterate through each index within the file.")
        print("[view-col]-to view a particular column within the file.")
        print("[count-str]-to count the number of strings within the column. For example the number of (No) strings or (Yes) srings within a column.")
        print("\n[filter-col]-to filter out the data that meets a certain criteria within a coloumn.")
        print("--[>]- (the number values within the column entered) > (more than the given value that the user entered) *Note the spacing.")
        print("--[>]- (the number values within the column entered) < (less than the given value that the user entered) *Note the spacing.\n")
        print("[sum-col]-to retrieve certain information within and of the data within the column.")
        print("The summerization operations:")
        print("[mean]-to retrieve the mean of the data.")
        print("[describe]-to retrieve the metadata")
        print("[all] -all of the above.\n")
        print("[graph-data]-to plot a graph based onthe information within the file. *Make sure the data is clean first.")
        print("[graph-spec]-to plot a graph based on a specific column within the file.")
        print("[report]-to store metadata and graphs of the columns within the file. *You must select these columns.")
    if command == "report":
        try:
            import pandas as pd
            from matplotlib import pyplot as plt
            import os
            import shutil
            import tkinter as tk
            from tkinter import filedialog
            import numpy as np
            import random
            from cryptography.ferent import Fernet

            oss = os.getcwd()
            root = tk.Tk()
            root.withdraw()
            pd.set_option('display.max_columns', None)

            print("[Stats for report]")
            print(f"{oss}\n")
            files = filedialog.askopenfilename()
            df = pd.read_excel(files,index_col = 0)
            print(df)

            ##dfName = (f"{files}[Cleaned].xlsx")
            ##df.to_excel(dfName)
            ##print("[Saved] dataframe")

            with open(f"{files}Summary_Data_report_.txt", "w") as dataFile:
                dataFile.write("Summary of dataframe.\n")
                dataFile.close()


            while True:
                commands = input(">>>>* ")
                if commands == "clear":
                        break

                if commands == "clean":
                    while True:
                        function = input("Enter cleaning method: ")
                        if function == "nan":
                            print("Nan_values replaced.\n")
                            df = df.fillna(0)
                            print(df)
                        if function == "str-to-int":
                            no = input("Enter number of values to be converted: ")
                            if no == "1":
                                col = input("Enter column name: ")
                                value = input("Enter string value to be converted: ")
                                dfValues = {value:0}
                                df[col] = [dfValues[item] for item in df[col]]
                                print(df)
                            if no == "2":
                                col = input("Enter column name: ")
                                value = input("Enter string value to be converted: ")
                                valueTwo = input("Enter string value to be converted: ")
                                dfValues = {value:0, valueTwo:1}
                                df[col] = [dfValues[item] for item in df[col]]
                                print(df)
                            if no == "3":
                                col = input("Enter column name: ")
                                value = input("Enter string value to be converted: ")
                                valueTwo = input("Enter string value to be converted: ")
                                valueThree = input("Enter string value to be converted: ")
                                dfValues = {value:0, valueTwo:1, valueThree:2}
                                df[col] = [dfValues[item] for item in df[col]]
                                print(df)
                            if no == "4":
                                col = input("Enter column name: ")
                                value = input("Enter string value to be converted: ")
                                valueTwo = input("Enter string value to be converted: ")
                                valueThree = input("Enter string value to be converted: ")
                                valueFour = input("Enter string value to be converted: ")
                                dfValues = {value:0, valueTwo:1, valueThree:2, valueFour:3, valueFive:4}
                                df[col] = [dfValues[item] for item in df[col]]
                                print(df)
                            if no == "5":
                                col = input("Enter column name: ")
                                value = input("Enter string value to be converted: ")
                                valueTwo = input("Enter string value to be converted: ")
                                valueThree = input("Enter string value to be converted: ")
                                valueFour = input("Enter string value to be converted: ")
                                valueFive = input("Enter string value to be converted: ")
                                dfValues = {value:0, valueTwo:1, valueThree:2, valueFour:3, valueFive:4}
                                df[col] = [dfValues[item] for item in df[col]]
                                print(df)
                        if function == "done":
                            dfName = (f"{files}[Cleaned].xlsx")
                            df.to_excel(dfName)
                            print("\n[Dataframe saved]\n")
                            break
                if commands == "show-index":
                    with open(f"{files}Summary_Data_report_.txt","a") as dataFile:
                        for index in df.iterrows():
                            str_index = str(index)
                            dataFile.write(str_index)
                        dataFile.close()
                            
                if commands == "view-col":
                    col = input("Enter col: ")
                    print(df[col])
                    strCol = str(df[col])
                    with open(f"{files}Summary_Data_report_.txt", "a") as dataFile:
                            dataFile.write(f"View_col\n\n{strCol}\n")
                            dataFile.close()
                            
                if commands == "count-str":
                    col = input("Enter col: ")
                    print(df[col])
                    print(list(df[col]))
                    words = input("Enter words to count: ")
                    print((list(df[col])).count(words))
                    count = str((list(df[col])).count(words))
                    with open(f"{files}Summary_Data_report_.txt", "a") as dataFile:
                            dataFile.write(f"Count_str\n\nStr: {words} count: {count}\n")
                            dataFile.close()
                            
                if commands == "filter-col":
                    #convert to list
                    col = input("Enter col: ")
                    operator,number = map(str, input("Enter filter: ").split())
                    number = int(number)
                    if operator == ">":
                        filter_result = (df[col]>(number))
                        print(df[col]>(number))
                        am_l = str(df[col]>(number))
                        with open(f"{files}Summary_Data_report_.txt", "a") as dataFile:
                            dataFile.write(f"Filter\n\nNumber: {number} Filter: {operator}\n{am_l}\n")
                            dataFile.close()
                            
                    if operator == "<":
                        filter_result = (df[col]<(number))
                        print(df[col]<(number))
                        am_r = str(df[col]<(number))
                        with open(f"{files}Summary_Data_report_.txt", "a") as dataFile:
                            dataFile.write(f"Filter\n\nNumber: {number} Filter: {operator}\n{am_r}\n")
                            dataFile.close()
                        
                if commands == "sum-col":
                    col = input("Enter col: ")
                    opr = input("Enter summerization operation: ")
                    if opr == "mean":
                        print(df[col].mean())
                        mean = str(df[col].mean())
                        with open(f"{files}Summary_Data_report_.txt", "a") as dataFile:
                            dataFile.write(f"Mean\n\n{mean}")
                            dataFile.close()
                    if opr == "describe":
                        print(df[col].describe())
                        des = str(df[col].describe())
                        with open(f"{files}Summary_Data_report_.txt", "a") as dataFile:
                            dataFile.write(f"Description\n\n{des}")
                            dataFile.close()
                    if opr == "all":
                        print(f"mean: {df[col].mean()}")
                        print(f"mode: {df[col].mode()}")
                        print(f"median: {df[col].median()}")
                        print("[===========]")
                        print(df[col].describe())
                        print("[===========]")
                        Data = str(f"mean: {df[col].mean()}\nmode: {df[col].mode()}\nmedian: {df[col].median()}\n[===========]{df[col].describe()}")
                        with open(f"{files}Summary_Data_report_.txt", "a") as dataFile:
                            dataFile.write(f"Data_info\n\n{Data}")
                            dataFile.close()
                if commands == "graph-data":
                    df.plot()
                    plt.show()
                if commands == "graph-spec":
                    value = input("Enter specific data to plot: ")
                    df[f"{value}"].plot()
                    plt.show()

                if commands == "report":
                    with open(f"{files}_index file.txt","w") as txt_file:
                        for index in df.iterrows():
                            str_index = str(index)
                            txt_file.write(str_index)
                        txt_file.close()
                        
                    colNo = input("Enter no. of required columns: ")
                    if colNo == "1":
                        col = input("Enter column: ")
                        with open(f"{files}_values Report_summary.txt","w") as txt_file:
                            mean = str(df[col].mean())
                            mode = str(df[col].mode())
                            median = str(df[col].median())
                            description = str(df[col].describe())
                            filedata = (f"mean:{mean}\nmode:{mode}\nmedian:{median}\des:{description}")
                            filed = str(filedata)
                            txt_file.write(filed)
                        txt_file.close()

                    if colNo == "2":
                        col = input("Enter column: ")
                        col2 = input("Enter column: ")
                        with open(f"{files}_values Report_summary_.txt","w") as txt_file:
                            mean = str(df[col].mean())
                            mode = str(df[col].mode())
                            median = str(df[col].median())
                            description = str(df[col].describe())

                            mean2 = str(df[col2].mean())
                            mode2 = str(df[col2].mode())
                            median2 = str(df[col2].median())
                            description2 = str(df[col2].describe())
                            
                            filedata = (f"mean:{mean}\nmode:{mode}\nmedian:{median}\ndes:{description}\nCol2:\nmean:{mean2}\nmode:{mode2}\nmedian:{median2}\n des:{description2}")
                            filed = str(filedata)
                            txt_file.write(filed)
                        txt_file.close()
                            
                    if colNo == "3":
                        col = input("Enter column: ")
                        col2 = input("Enter column: ")
                        col3 = input("Enter column: ")
                        with open(f"{files}_values Report_summary_.txt","w") as txt_file:
                            mean = str(df[col].mean())
                            mode = str(df[col].mode())
                            median = str(df[col].median())
                            description = str(df[col].describe())

                            mean2 = str(df[col2].mean())
                            mode2 = str(df[col2].mode())
                            median2 = str(df[col2].median())
                            description2 = str(df[col2].describe())
                            
                            mean3 = str(df[col3].mean())
                            mode3 = str(df[col3].mode())
                            median3 = str(df[col3].median())
                            description3 = str(df[col3].describe())
                            
                            filedata = (f"mean:{mean}\nmode:{mode}\nmedian:{median}\ndes:{description}\nCol2:\nmean:{mean2}\nmode:{mode2}\nmedian:{median2}\ndes:{description2}\nCol3:\nmean:{mean3}\nmode:{mode3}\nmedian:{median3}\ndes:{description3}")
                            filed = str(filedata)
                            txt_file.write(filed)
                        txt_file.close()
                        
                    if colNo == "4":
                        col = input("Enter column: ")
                        col2 = input("Enter column: ")
                        col3 = input("Enter column: ")
                        col4 = input("Enter column: ")
                        with open(f"{files}_values Report_summary_.txt","w") as txt_file:
                            mean = str(df[col].mean())
                            mode = str(df[col].mode())
                            median = str(df[col].median())
                            description = str(df[col].describe())

                            mean2 = str(df[col2].mean())
                            mode2 = str(df[col2].mode())
                            median2 = str(df[col2].median())
                            description2 = str(df[col2].describe())
                            
                            mean3 = str(df[col3].mean())
                            mode3 = str(df[col3].mode())
                            median3 = str(df[col3].median())
                            description3 = str(df[col3].describe())
                            
                            mean4 = str(df[col4].mean())
                            mode4 = str(df[col4].mode())
                            median4 = str(df[col4].median())
                            description4 = str(df[col4].describe())
                            
                            filedata = (f"mean:{mean}\nmode:{mode}\nmedian:{median}\ndes:{description}\nCol2:\nmean:{mean2}\nmode:{mode2}\nmedian:{median2}\ndes:{description2}\nCol3:\nmean:{mean3}\nmode:{mode3}\nmedian:{median3}\ndes:{description3}\nCol4:\nmean:{mean4}\nmode:{mode4}\nmedian:{median4}\ndes:{description4}")
                            filed = str(filedata)
                            txt_file.write(filed)
                        txt_file.close()
                        
                    if colNo == "5":
                        col = input("Enter column: ")
                        col2 = input("Enter column: ")
                        col3 = input("Enter column: ")
                        col4 = input("Enter column: ")
                        col5 = input("Enter column: ")
                        with open(f"{files}_values Report_summary_.txt","w") as txt_file:
                            mean = str(df[col].mean())
                            mode = str(df[col].mode())
                            median = str(df[col].median())
                            description = str(df[col].describe())

                            mean2 = str(df[col2].mean())
                            mode2 = str(df[col2].mode())
                            median2 = str(df[col2].median())
                            description2 = str(df[col2].describe())
                            
                            mean3 = str(df[col3].mean())
                            mode3 = str(df[col3].mode())
                            median3 = str(df[col3].median())
                            description3 = str(df[col3].describe())
                            
                            mean4 = str(df[col4].mean())
                            mode4 = str(df[col4].mode())
                            median4 = str(df[col4].median())
                            description4 = str(df[col4].describe())
                            
                            mean5 = str(df[col5].mean())
                            mode5 = str(df[col5].mode())
                            median5 = str(df[col5].median())
                            description5 = str(df[col5].describe())
                            
                            filedata = (f"mean:{mean}\nmode:{mode}\nmedian:{median}\ndes:{description}\nCol2:\nmean:{mean2}\nmode:{mode2}\nmedian:{median2}\ndes:{description2}\nCol3:\nmean:{mean3}\nmode:{mode3}\nmedian:{median3}\ndes:{description3}\nCol4:\nmean:{mean4}\nmode:{mode4}\nmedian:{median4}\ndes:{description4}\nCol5:\nmean:{mean5}\nmode:{mode5}\nmedian:{median5}\ndes:{description5}")
                            filed = str(filedata)
                            txt_file.write(filed)
                        txt_file.close()
                            
                    os.mkdir(f"{files}_plots")
                    df = pd.read_excel(files)
                    df.plot()
                    plt.savefig("Overview.jpg")
                    print("[Plot completed]\n================")
                    shutil.move("Overview.jpg", f"{files}_plots")
                    print("[Plot saved]\n================")
                    
                    x = df.plot.area(figsize=(12,4), subplots=True)
                    plt.plot()
                    plt.savefig(f"{files}.jpg")
                    print("[Plot completed]\n================")
                    shutil.move(f"{files}.jpg", f"{files}_plots")
                    print("[Plot saved]\n================")                    
                
        except:
            pass
        #    print("It seems an incorrect value has been entered. Please check the values entered ....")

    if command == ".exit":
        break

