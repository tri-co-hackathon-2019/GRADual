from app.models import Course
from app import db

def create_database():
    cs105 = Course(department="CS", 
                    number=105,
                    term='F',
                    frequency=1,
                    taken=False,
                    core=True,
                    domain='C',
                    parent=None)
    cs106 = Course(department="CS", 
                    number=106,
                    term='S',
                    frequency=1,
                    taken=False,
                    core=True,
                    domain='C',
                    parent=105)
    cs231 = Course(department="CS", 
                    number=231,
                    term='F',
                    frequency=1,
                    taken=False,
                    core=True,
                    domain='C',
                    parent=105)
    cs208 = Course(department="CS", 
                    number=208,
                    term='F',
                    frequency=2,
                    taken=False,
                    core=False,
                    domain='C',
                    parent=106)
    math215 = Course(department="MATH", 
                    number=215,
                    term='E',
                    frequency=1,
                    taken=False,
                    core=False,
                    domain='C',
                    parent=105)
    cs222 = Course(department="CS", 
                    number=222,
                    term='S',
                    frequency=1,
                    taken=False,
                    core=False,
                    domain='C',
                    parent=215)
    cs240 = Course(department="CS", 
                    number=240,
                    term='F',
                    frequency=1,
                    taken=False,
                    core=True,
                    domain='C',
                    parent=231)
    cs245 = Course(department="CS", 
                    number=245,
                    term='F',
                    frequency=1,
                    taken=False,
                    core=True,
                    domain='C',
                    parent=231)
    cs287 = Course(department="CS", 
                    number=287,
                    term='S',
                    frequency=2,
                    taken=False,
                    core=False,
                    domain='C',
                    parent=106)
    cs340 = Course(department="CS", 
                    number=340,
                    term='F', 
                    frequency=1, 
                    taken=False,
                    core=True, 
                    domain='C', 
                    parent=231)

    cs345 = Course(department="CS", 
                    number=345,
                    term='S',
                    frequency=1,
                    taken=False,
                    core=True,
                    domain='C',
                    parent=231)
    cs350 = Course(department="CS", 
                    number=350,
                    term='S',
                    frequency=2,
                    taken=False,
                    core=True,
                    domain='C',
                    parent=245)
    cs399 = Course(department="CS", 
                    number=399,
                    term='F',
                    frequency=1,
                    taken=False,
                    core=True,
                    domain='C',
                    parent=350)
    cs400 = Course(department="CS", 
                    number=400,
                    term='S',
                    frequency=1,
                    taken=False,
                    core=True,
                    domain='C',
                    parent=399)
    cs_course_list = [cs105, cs106, cs208, cs222, cs231, cs240,cs245, cs287, cs340, cs350, cs345, cs399, cs400, math215]
    for course in cs_course_list:
        db.session.add(course)
    db.session.commit()

def delete_database():
    for course in Course.query.all():
        db.session.delete(course)
    db.session.commit()

# CS Major Tree
# def create_tree_cs():
    # cs105 = Node(Course('CS',105,'F',1,False,True,'C'), parent=None)
    # cs106 = Node(Course('CS',106,'S',1,False,True,'C'), parent=cs105)
    # cs231 = Node(Course('CS',231,'F',1,False,True,'C'), parent=cs105)
    # cs208 = Node(Course('CS',208,'F',2,False,False,'C'), parent=cs106)
    # cs215 = Node(Course('CS',215,'S',2,False,False,'C'), parent=cs106)
    # math215 = Node(Course('MATH',215,'E',1,False,False,'C'), parent=cs105)
    # cs222 = Node(Course('CS',222,'S',1,False,False,'C'), parent=math215)
    # cs240 = Node(Course('CS',240,'F',1,False,True,'C'), parent=cs231)
    # cs245 = Node(Course('CS',245,'F',1,False,True,'C'), parent=cs231)
    # cs287 = Node(Course('CS',287,'S',2,False,False,'C'), parent=cs106)
    # cs340 = Node(Course('CS',340,'F',1,False,True,'C'), parent=cs231)
    # cs345 = Node(Course('CS',345,'S',1,False,True,'C'), parent=cs231)
    # cs350 = Node(Course('CS',350,'S',2,False,True,'C'), parent=cs245)
    # cs399 = Node(Course('CS',399,'F',1,False,True,'C'), parent=cs350)
    # cs400 = Node(Course('CS',400,'S',1,False,True,'C'), parent=cs399)
