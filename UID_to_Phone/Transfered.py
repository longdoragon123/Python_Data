from tkinter import ttk
import pandas as pd
import glob, os
from tkinter import *

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
canvas1.create_text( 250, 10, text = "TRANSFERED", font=('courier',15,'bold'))

# var = StringVar()
# label = Label(root,anchor="center",textvariable=var,cursor='dot',bd=10)
# var.set('TRANSFERED')
# label.place(x=200,y=0)

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

    # paths = r'C:\Users\admin\Documents\test\Raw data'
    my_list = os.listdir(paths)
    # output = r'C:\Users\admin\Documents\test\Transfered'
    combine = 'combine_txt.txt'
    
    # myLabel_1 = Label(root, text=paths)
    # myLabel_1.pack()
    # myLabel_2 = Label(root, text=output)
    # myLabel_2.pack()
    
    def tranfered() :
        def convert_to_multiple_files(in_file):
            
            number_lines = sum(1 for row in (open(in_file)))
            rowsize = 200000
            #start looping through data writing it to a new file for each set
            for i in range(0,number_lines,rowsize):
                df_split = pd.read_csv(in_file, dtype ='str',
                    nrows = rowsize,#number of rows to read at each loop
                    skiprows = i)#skip rows that have been read
                #csv to write data to a new file with indexed name. input_1.csv etc.
                out_csv = f'{d}\\Combine_' + str(i) + '.txt' 
                df_split.to_csv(out_csv,
                    index=False,
                    header=True,
                    mode='a',#append data to csv file
                    chunksize=rowsize)#size of data to append for each loop

        for list_1 in my_list:
            os.mkdir(f'{output}\\{list_1}')   
            d = f'{output}\\{list_1}'
            # print(d)
            my_list_1 = os.listdir(r'{}\{}'.format(paths, list_1))
            
            for list_2 in my_list_1:
                df = pd.read_csv(r'{}\{}\{}'.format(paths,list_1,list_2), names = ['Uid'])
                df_to_txt = df['Uid'].to_csv(f'{d}\\{list_2[:-4]}.txt',index=None )
                
                files = os.path.join(r'{}'.format(d), "*.txt")
                files = glob.glob(files)
                df = pd.concat(map(pd.read_csv, files), ignore_index=True)
                print(files)
                
                filelist = glob.glob(os.path.join(d, "*.txt"))
                for f in filelist:
                    os.remove(f)
                
                df.to_csv( f'{d}\\{combine}', index=False)
            path_combine = f'{d}\\{combine}'
            print(path_combine)
            
            convert_to_multiple_files(path_combine)
            filelist = glob.glob(os.path.join(d, "*_txt.txt"))
            for f in filelist:
                os.remove(f)
    tranfered()

myButton = Button(root,text='Enter', command=myClick,bg='#00FFFF')
myButton.place(x=230, y=90)
root.mainloop()


