print('''Mô tả lỗi: Khi mở file Python lớn(>1MB), Notepad++ có dấu hiệu bị lag, sau một khoảng thời gian thì bị đơ, không thể thao tác.
Cách khắc phục lỗi Notepad++ không mở được file Python lớn
1.Sử dụng Notepad++ 64-bit
-Nếu bạn đang dùng Windows 64-bit (hầu hết các máy tính hiện nay đều là 64-bit), hãy đảm bảo rằng bạn đã cài đặt phiên bản Notepad++ 64-bit.
Phiên bản 32-bit có giới hạn bộ nhớ thấp hơn, thường gặp khó khăn với các tệp trên 2 GB.
Phiên bản 64-bit có khả năng xử lý các tệp lớn hơn nhiều (về mặt lý thuyết có thể lên đến hàng trăm GB nếu bạn có đủ RAM).
- Cách kiểm tra và nâng cấp:
Mở Notepad++.
Vào ? (Help) → About Notepad++.
Kiểm tra xem nó hiển thị là x64 hay x86 (32-bit).
Nếu là x86, hãy gỡ cài đặt và tải xuống phiên bản 64-bit mới nhất từ trang web chính thức của Notepad++.
Kết quả: Notepad++ vẫn bị lag, đơ
2.Sử dụng trình soạn thảo văn bản chuyên dụng cho tệp lớn
-Đối với các tệp có dung lượng quá lớn (vài GB trở lên), Notepad++ không phải là lựa chọn tối ưu vì nó cố gắng tải toàn bộ tệp vào RAM. Bạn nên cân nhắc sử dụng các trình soạn thảo được thiết kế đặc biệt để đọc và chỉnh sửa tệp lớn bằng cách chỉ tải các phần nhỏ (chunk) của tệp vào bộ nhớ:
EmEditor: Được cộng đồng đánh giá cao về khả năng xử lý các tệp có kích thước khổng lồ (thậm chí 100GB). Có phiên bản miễn phí (EmEditor Free).
VS Code (Visual Studio Code): Là một IDE/Editor mạnh mẽ, có thể xử lý các tệp lớn tốt hơn Notepad++.
Glogg: Một công cụ xem nhật ký (log) siêu nhanh, lý tưởng để chỉ xem và tìm kiếm trong các tệp văn bản lớn.
UltraEdit: Phần mềm trả phí nổi tiếng với khả năng xử lý tệp lớn.

3.Chia các tệp lớn thành các tệp nhỏ
Nếu chỉ cần chỉnh sửa một phần nhỏ trong tệp hoặc xử lý từng phần một, bạn có thể sử dụng các công cụ bên ngoài để chia tệp lớn thành các tệp nhỏ hơn.
Bạn có thể tìm kiếm các công cụ chia tệp (file splitter) trực tuyến.
Đối với người dùng có kinh nghiệm, các lệnh trên Linux/WSL như split cũng có thể được sử dụng.
Kết quả: Khi đưa lên VSCode, file chạy mượt, nhanh''')
from PIL import Image
img = Image.open('Picture1.png')
img.show()