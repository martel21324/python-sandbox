from student19 import Student

def test_student_name():
    student = Student("JF", "Quebec")
    assert student.name == "JF"
    assert student.house == "Quebec"

def test_invalid_name():
    try:
        _ = Student("", "Gryffindor")
        assert False, "Expected ValueError for invalid name"
    except ValueError as e:
        assert str(e) == "Invalid name"


def test_str_representation():
    student = Student("Harry", "Gryffindor")
    assert str(student) == "Harry from Gryffindor"
    
            