from app import app
from flask import render_template, request, flash, redirect, url_for
from app.models import Course


taken_courses = []


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    courses = Course.query.all()
    cs105 = Course.query.filter_by(number=105).first()

    if len(taken_courses) != 0:
        fall_lst = get_next_fall_course(int(taken_courses[-1]))
    else:
        fall_lst = [cs105]

    spring_courses = Course.query.filter_by(term='S')

    return render_template('index.html', courses=courses, 
                                    taken_courses=taken_courses,
                                    fall_lst=fall_lst)


@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    taken_courses.append(str(select))
    # str(select) # just to see what select is
    return redirect(url_for('index'))


def get_next_fall_course(coursenum):
    fall_lst = []
    courses = Course.query.all()
    for c in courses:
        if c.number == 105:
            break
        else:
            if c.parent.number == coursenum and c.term == 'F':
                fall_lst.append(c)
    return fall_lst


def get_next_spring_course(course):
    spring_lst = []
    courses = Course.query.all()
    for c in courses:
        if c.parent == course.number and c.term == 'S':
            spring_lst.append(c)
    return spring_lst