"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.


"""


# Parts 2 through 5:
# Create your classes and class methods

"""
Part 2: Classes and Init Methods

"""


class Student(object):
    """A student."""

    def __init__(self, first_name, last_name, address):
        """Initialize student."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def make_student_dictionary(self):
        """Create dictionary from initialized student variables."""

        student_dictionary = {}

        student_dictionary["first_name"] = self.first_name
        student_dictionary["last_name"] = self.last_name
        student_dictionary["address"] = self.address

        return student_dictionary       # dictionary is unordered, unlike prompt


class Question(object):
    """A question."""

    def __init__(self, question, answer):
        """Initialize question and answer."""

        self.question = question
        self.answer = answer

    def make_question_dictionary(self):
        """Create dictionary from initialized question and answer variables."""

        question_dictionary = {}

        question_dictionary["question"] = self.question
        question_dictionary["answer"] = self.answer

        return question_dictionary


class Exam(object):
    """A midterm or final exam."""

    def __init__(self, name):
        """Initialize exam."""

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Add question and answer to self.questions list."""

        self = Question(question, correct_answer)

        self.make_question_dictionary()

        return self.question_dictionary

    def make_exam(self):
        """Create dictionary containing exam type, questions, and answers."""

        exam_dictionary = {}

        exam_dictionary["name"] = self.name
        exam_dictionary["questions"] = self.questions

        return exam_dictionary


"""
Part 3: Methods

"""
