# This code only for create folder and move file to new folder with same name and add number to folder
# Đây là code tạo folder cho từng file PDF riêng biệt và đánh số thứ tư
# This program make by Le Xuan Thang
# Code này được tạo bởi Lê Xuân Thắng
# July 09th 2020
# Ngày 09 tháng 07 năm 2020
# Version: 0.1.0
# Phiên bản: 0.1.0
# This program run with CMD:
# Đầu vào khi chạy bằng CMD sẽ là:
# Form of command for run this program is:
# python [Create_Folder&Move_File.py] <sources_file> <star_nuber> 
# python [tên.py] pdf_folder\ star_number 
# sources_file: this is name of folder that keep your file
# star_number: It's Number that you want to star with
 
# Import libary / Thư viện
import os   
import sys
import shutil

# Step 1: take name of folder and number / Bước 1 Lấy tên file pdf và số bắt đầu
pdf_folder = sys.argv[1]
star_number = sys.argv[2]

# Main loop / Vòng lặp chính
i = star_number
for file_name in os.listdir(pdf_folder):
    # Take folder's name and split it to tuple/lấy tên folder và loại đuôi file
    clean_name = os.path.splitext(file_name)

    # Adding number / Ghép tên với số thứ tự
    complete_name = i + '. ' + clean_name[0]

    # Check folder exists / Kiểm tra thư mục xem đã có chưa nếu có rồi thì không tạo
    if not os.path.exists(complete_name):
        # Create folder with new name / Tạo thư mục với tên được ghép
        os.makedirs(complete_name)

    # Get sources path of sources folder / Lấy đường dẫn thư mục nguồn  
    abs_FROM_path = os.path.abspath(pdf_folder)
    from_path = os.path.join(abs_FROM_path,file_name)

    # Destination of new folder/Đường dẫn thư mục đích
    abs_TO_path = os.path.abspath('')
    to_path = os.path.join(abs_TO_path,complete_name)

    # Move file from sources folder to destination of new folder / Chuyển file từ thư mục nguồn sang thư mục đích
    print ('Moving file From', pdf_folder, '---To: ',complete_name )
    shutil.move(from_path,to_path)

    i = int(i)
    i = i + 1
    i = str(i)

print ('Creating and Moving file complete & have a good day')
# END