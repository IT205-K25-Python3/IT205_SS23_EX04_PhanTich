calculate_average(scores)

Input: List các giá trị (số/chuỗi).

Output: float (Điểm trung bình).

Pseudocode: Lọc các giá trị là số, tính tổng và chia cho số lượng. Nếu list rỗng hoặc không có số hợp lệ, trả về 0.0.

normalize_student_names(records)

Input: List dictionary.

Output: None (cập nhật trực tiếp vào records).

Pseudocode: Duyệt qua từng record, dùng .strip(), .split() để tách từ, capitalize() để viết hoa, sau đó join() lại.

export_learning_report(records)

Input: List dictionary.

Output: Ghi file .txt và in thông báo màu.

Pseudocode: Sử dụng datetime.now() để lấy thời gian, đếm số lượng dựa trên ĐTB >= 5.0, ghi nội dung vào file learning_report.txt.
