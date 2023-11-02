subjects_dict = {}

with open("учебные_предметы.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    parts = line.strip().split(': ')
    if len(parts) == 2:
        subject, lessons_info = parts
        total_lessons = 0
        lessons = lessons_info.split()
        for lesson in lessons:
            if '(' in lesson and ')' in lesson:
                count, lesson_type = lesson.strip('()').split('(')
                total_lessons += int(count)
        subjects_dict[subject] = total_lessons
    else:
        print(f"Неправильный формат строки: {line}")

print("Словарь с общим количеством занятий по каждому предмету:")
print(subjects_dict)
