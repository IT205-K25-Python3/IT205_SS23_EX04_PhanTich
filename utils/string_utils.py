def normalize_student_names(records):
    for student in records:
        name = student["name"].strip()
        words = name.split()
        student["name"] = " ".join([word.capitalize() for word in words])