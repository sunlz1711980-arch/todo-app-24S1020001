tasks = []  
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

if __name__ == "__main__":
    main()
def add_task():
    content = input("Nhập công việc mới: ")
    tasks.append({"content": content, "status": "Pending"})
    print("Đã thêm công việc.")
def view_tasks():
    if not tasks:
        print("Danh sách trống!")
        return
    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['content']} [{task['status']}]")


