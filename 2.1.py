
print('''Khắc phục lỗi wifi không kết nối trên win 10
1.Kiểm tra thiết bị
Kiểm tra Router/Modem hoặc Wifi: Khởi động lại Router/Modem
Kiểm tra máy tính: Restart máy, tắt chế độ máy bay, forget wifi và kết nối lại
2.Sử dụng công cụ chẩn đoán của Window
Sử dụng Internet Connections Troubleshooter:
Vào Settings (Cài đặt) → Update & Security (Cập nhật & Bảo mật) → Troubleshoot (Khắc phục sự cố).
Chọn Additional troubleshooters (Bộ giải quyết sự cố bổ sung) (hoặc chỉ Troubleshoot tùy phiên bản).
Chọn Internet Connections (Kết nối Internet) rồi nhấn Run the troubleshooter (Chạy trình khắc phục sự cố).


3.Khắc phục Driver Wifi (lỗi, thiếu, cũ)
Cập nhật Driver:
Nhấn tổ hợp phím Windows+X và chọn Device Manager (Quản lý Thiết bị).
Mở rộng mục Network adapters (Bộ điều hợp mạng).
Tìm thiết bị Wireless Network Adapter (thường có chữ Wireless hoặc Wi-Fi).
Chuột phải vào nó và chọn Update driver (Cập nhật trình điều khiển), sau đó chọn Search automatically for updated driver software (Tự động tìm kiếm phần mềm điều khiển được cập nhật).
 Gỡ cài đặt và Cài đặt lại Driver:
Nếu cập nhật không hiệu quả, chuột phải vào Wireless Network Adapter và chọn Uninstall device (Gỡ cài đặt thiết bị).
Sau khi gỡ, khởi động lại máy tính. Windows sẽ tự động cài đặt lại driver khi khởi động.

4.Đặt cấu hình mạng về mặc định
-Reset Network Adapter (Khởi động lại Bộ điều hợp Mạng):
Mở Command Prompt (CMD) dưới quyền Administrator (Quản trị viên) (Tìm kiếm → gõ CMD → Chuột phải → Run as administrator).
Nhập các lệnh sau, nhấn Enter sau mỗi lệnh:
onetsh winsock reset
onetsh int ip reset
-Sử dụng Network Reset của Windows 10:
Vào Settings (Cài đặt) → Network & Internet (Mạng & Internet) → Status (Trạng thái).
Cuộn xuống và chọn Network reset (Đặt lại mạng).
Nhấn Reset now (Đặt lại ngay). Lưu ý: Thao tác này sẽ gỡ và cài đặt lại tất cả các bộ điều hợp mạng, đặt lại cấu hình về mặc định. Bạn sẽ cần kết nối lại tất cả các mạng Wi-Fi và Ethernet đã lưu.''')
from PIL import Image
img=Image.open('Picture2.1.png')
img.show() #Hiển thị ảnh

