from db import *


def course_init():
    db.session.query(Course).delete()
    db.session.commit()

    new_course = Course(
        code="CS1110",
        name="Introduction to Computing Using Python",
        description="Programming and problem solving using Python. Emphasizes principles of software development, style, and testing. Topics include procedures and functions, iteration, recursion, arrays and vectors, strings, an operational model of procedure and function calls, algorithms, exceptions, object-oriented programming. Weekly labs provide guided practice on the computer, with staff present to help.",
        professors="Anne Bracy, Lilian Lee",
        rating=0,
        allratings="0",
        comments=[]
    )
    db.session.add(new_course)
    db.session.commit()

    new_course = Course(
        code="CS1300/INFO1300",
        name="Introductory Design and Programming for the Web",
        description="The World Wide Web is both a technology and a pervasive and powerful resource in our society and culture. To build functional and effective web sites, students need technical and design skills as well as analytical skills for understanding who is using the web, in what ways they are using it, and for what purposes. In this course, students develop skills in all three of these areas through the use of technologies such as XHTML, Cascading Stylesheets, and PHP. Students study how web sites are deployed and used, usability issues on the web, user-centered design, and methods for visual layout and information architecture. Through the web, this course provides an introduction to the interdisciplinary field of information science.",
        professors="Kyle Harms",
        rating=0,
        allratings="0",
        comments=[]
    )
    db.session.add(new_course)
    db.session.commit()

    new_course = Course(
        code="CS2110",
        name="Object-Oriented Programming and Data Structures",
        description="""Intermediate programming in a high-level language and introduction to computer science. Topics include object-oriented programming (classes, objects, subclasses, types), graphical user interfaces, algorithm analysis (asymptotic complexity, big "O" notation), recursion, testing, program correctness (loop invariants), searching/sorting, data structures (lists, trees, stacks, queues, heaps, search trees, hash tables, graphs), graph algorithms. Java is the principal programming language.""",
        professors="Michael Clarkson, David Gries",
        rating=0,
        allratings="0",
        comments=[]
    )
    db.session.add(new_course)
    db.session.commit()

    new_course = Course(
        code="CS2300/INFO2300",
        name="Intermediate Design and Programming for the Web",
        description="Web programming requires the cooperation of two machines: the one in front of the viewer (client) and the one delivering the content (server). INFO 1300 concentrates almost exclusively on the client side. The main emphasis in INFO 2300 is learning about server side processing. Students begin with a short overview of the PHP server-side scripting language, then look at interactions with databases, learning about querying via the database language SQL. Through a succession of projects, students learn how to apply this understanding to the creation of an interactive, data-driven site via PHP and the MYSQL database. Also considered are technologies such as Javascript and Ajax and techniques to enhance security and privacy. Design and usability issues are emphasized. A major component of the course is the creation of a substantial web site.",
        professors="Kyle Harms",
        rating=0,
        allratings="0",
        comments=[]
    )
    db.session.add(new_course)
    db.session.commit()

    new_course = Course(
        code="CS2800",
        name="Discrete Structures",
        description="""Covers the mathematics that underlies most of computer science. Topics include mathematical induction; logical proof; propositional and predicate calculus; combinatorics and discrete mathematics; some basic elements of basic probability theory; basic number theory; sets, functions, and relations; graphs; and finite-state machines. These topics are discussed in the context of applications to many areas of computer science, such as the RSA cryptosystem and web searching.""",
        professors="Anke van Zuylen",
        rating=0,
        allratings="0",
        comments=[]
    )
    db.session.add(new_course)
    db.session.commit()
