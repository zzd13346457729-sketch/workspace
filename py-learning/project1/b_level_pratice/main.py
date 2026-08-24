from school.student import Student


def main():
    student1 = Student("张三", 95)
    student2 = Student("李四", 78)

    student1.show_info()
    print()

    student2.show_info()


if __name__ == "__main__":
    main()
