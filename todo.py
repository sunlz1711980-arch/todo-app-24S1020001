tasks = []

def add_task():
    content = input("Nhập nội dung công việc: ")
    tasks.append({
        "content": content,
        "status": "Pending"
    })
    print("✅ Đã thêm công việc.")

def view_tasks():
    if not tasks:
        print("📭 Danh sách công việc trống.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['content']} [{task['status']}]")

def mark_task_done():
    if not tasks:
        print("📭 Không có công việc nào.")
        return

    view_tasks()
    try:
        index = int(input("Chọn số thứ tự công việc: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]['status'] = "Done"
            print("✅ Đã đánh dấu hoàn thành.")
        else:
            print("❌ Số không hợp lệ.")
    except ValueError:
        print("❌ Vui lòng nhập số.")

def main():
    while True:
        print("\n--- TODO LIST ---")
        print("1. Thêm công việc")
        print("2. Xem danh sách")
        print("3. Đánh dấu hoàn thành")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
