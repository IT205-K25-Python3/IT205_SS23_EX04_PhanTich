from utils.score_utils import calculate_average, classify_student
from datetime import datetime
from colorama import Fore, Style

def display_student_scores(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    print("\n--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for i, s in enumerate(records, 1):
        avg = calculate_average(s["scores"])
        rank = classify_student(avg)
        print(f"{i}. [{s['student_id']}] {s['name']:<15} | Điểm: {s['scores']} | ĐTB: {avg:.2f} - {rank}")

def export_learning_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    passed = [s for s in records if calculate_average(s["scores"]) >= 5.0]
    
    with open("learning_report.txt", "w", encoding="utf-8") as f:
        f.write(f"Báo cáo ngày: {datetime.now()}\n")
        f.write(f"Tổng: {len(records)} | Đạt: {len(passed)} | Cần cải thiện: {len(records) - len(passed)}")
    
    print(Fore.GREEN + ">> Đã xuất báo cáo ra file learning_report.txt" + Style.RESET_ALL)