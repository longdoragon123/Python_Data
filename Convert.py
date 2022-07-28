from tkinter import ttk
import pandas as pd
import glob, os
from tkinter import *
import random

# Create object
root = Tk()

# adjust size
root.title('Guild Python')
root.geometry('450x200')

#Add image
bg = PhotoImage(file=r'C:\Users\admin\Pictures\report\white-vs-transparent-background.png')

# Create Canvas
canvas1 = Canvas( root, width = 300,
                 height = 200)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 1, 0, image = bg, 
                     anchor = "w")

# Creating a photoimage object to use image
image = PhotoImage(file = r"C:\Users\admin\Pictures\report\anh_che.png")
smaller_image = image.subsample(3, 3) 
canvas1.create_image( 0, 140, image = smaller_image, 
                     anchor = "w")

# Add Text
canvas1.create_text( 250, 20, text = "Split to multiple file", font=('courier',15,'bold'),fill='#660000')

#add entry
e_1 = ttk.Entry(root, width=40, font=('courier', 10, 'bold'))
e_1.place(x=100,y = 35)

e_2 = ttk.Entry(root, width=40, font=('courier', 10, 'bold'))
e_2.place(x=100, y=65)

#add text
canvas1.create_text( 50, 45, text = "Đường dẫn", font=('courier',10,'bold'))
canvas1.create_text( 48, 75, text = "Nơi lưu trữ", font=('courier',10,'bold'))

#style text
style = ttk.Style()
style.configure('TEntry', foreground = 'green')

def myClick():
    paths = e_1.get()
    output = e_2.get()
    # paths = r'C:\Users\admin\Documents\test\converted'
    my_list = os.listdir(paths)
    # output = r'C:\Users\admin\Documents\test\converted_new'
    combine = 'split_combine_txt.txt'
    
    def converted():
        
        a = ['Trang','Nhi','Nhung','Dung','Vy','Khang','Khanh','Khoa','Vinh','Hoa','Anh','Kim','Nga','Nghi',
            'Lan','Phong','Long','Sang','Chi','Huynh','Loan','Di','Duy','Minh','Thy','Thu','Thi','Ly','My',
            'Nam','Thanh','Mai','An','Kha','Linh','Bi','Tuy','Em','Huy','Trung','Chung','Sa','Giang','Gia',
            'Na','Nhu','Quang','Quy','Phi','Ti','Trinh','Nho','Nhu']

        def convert_to_multiple_files(path_to_convert_file):
            in_csv = r'{}'.format(path_to_convert_file)
            #get the number of lines of the csv file to be read
            number_lines = sum(1 for row in (open(in_csv)))
            rowsize = 200
            header= ['First Name','Last Name','Phone']
            #start looping through data writing it to a new file for each set
            for i in range(0,number_lines,rowsize):
                df_split = pd.read_csv(in_csv, dtype = 'str',
                    nrows = rowsize,#number of rows to read at each loop
                    skiprows = i)#skip rows that have been read
                df_split.columns = header
                #csv to write data to a new file with indexed name. input_1.csv etc.
                out_csv = f'{output}\\{list_1}\\convert_multiple_' + str(i) + '.csv'
                # d = f'{output}\\{list_1}'
                df_split.to_csv(out_csv,
                    index=False,
                    header=True,
                    mode='a',#append data to csv file
                    chunksize=rowsize)#size of data to append for each loop

        def split_files(path_comb):
            # split uid|phone to 2 column UID, Phone
            df = pd.read_csv(r'{}'.format(path_combine))
            df[['Phone','UID']] = df['Uid|Phone'].str.split("|",expand=True)
            df_1 = df['Phone']
            df_1_csv =  df_1.to_csv(r'{}'.format(path_combine), index = None)
            
            # create columns 'First Name', 'Last name', 'Phone'.
            df_1_csv = pd.read_csv(r'{}'.format(path_combine),dtype = 'str')
            df_1_csv[['First Name', 'Last name']] = ''
            df_2_csv = df_1_csv.reindex(columns=['First Name','Last Name','Phone'])    
            
            keep= ["086","096","097","098","032","033",
                "034","035","036","037","038","039",# Vietel
                "089","090","093","070","079","077","076","078" # Mobifone
                ,"088","091","094","083","084","085","081","082", # Vinaphone
                "092","056","058"] # Vietnamobile
            
            #filter for rows that contain the partial string "Wes" in the conference column
            df_2_csv = df_2_csv[df_2_csv.Phone.str.contains('|'.join(keep))]
            df_dup = df_2_csv.drop_duplicates(keep='first')
            # df_dup.to_csv(r'{}'.format(path_combine), index = None)
            # print(df_dup)
            _list = []
            for i in range(0, len(df_dup)):
                item = random.choices(a)
                item = str(item[0])
                _list.append(item)
            df_dup['Last Name'] = _list    
            print(df_dup)
            df_dup.to_csv(r'{}'.format(path_combine), index = None)

        for list_1 in my_list:
            os.mkdir(f'{output}\\{list_1}')
            d = f'{output}\\{list_1}'
            # print(list_1)
            my_list_1 = os.listdir(r'{}\{}'.format(paths,list_1))
            for list_2 in my_list_1:
                df = pd.read_csv(r'{}\{}\{}'.format(paths,list_1,list_2), names = ["Uid|Phone"])
                df_to_txt = df.to_csv(f'{d}\\{list_2}.txt',index=None)
                # print(df_to_txt)
                files = os.path.join(r'{}'.format(d), "*.txt")
                files = glob.glob(files)
                df = pd.concat(map(pd.read_csv, files))
                filelist = glob.glob(os.path.join(d, "*.txt"))
                for f in filelist:
                    os.remove(f)
                df.to_csv( f'{d}\\{combine}', index=False)
            path_combine = f'{d}\\{combine}'
            print(path_combine)
            split_files(path_combine)
            convert_to_multiple_files(path_combine)
            filelist = glob.glob(os.path.join(d, "*_txt.txt"))
            for f in filelist:
                os.remove(f)  
    converted()
myButton = Button(root,text='Enter', command=myClick,bg='#00FFFF')
myButton.place(x=230, y=90)
root.mainloop()


