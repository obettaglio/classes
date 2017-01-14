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

        return student_dictionary       # dictionary is unordered


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

    def ask_and_evaluate(self):
        """Prompt user for answer to question and return True or False."""

        user_answer = raw_input(self.question + " ")
        if user_answer == self.answer:
            return True
        else:
            return False


class Exam(object):
    """A midterm or final exam."""

    def __init__(self, name):
        """Initialize exam."""

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Add question and answer to self.questions list."""

        new_question = Question(question, correct_answer)
        new_question = new_question.make_question_dictionary()

        self.questions.append(new_question)

        return self.questions

    def make_exam(self):
        """Create dictionary containing exam type, questions, and answers."""

        exam_dictionary = {}

        exam_dictionary["name"] = self.name
        exam_dictionary["questions"] = self.questions

        return exam_dictionary

    def administer(self):
        """Prompt user for answer to exam question, return user's score."""

        user_score = 0
        perfect_score = 0

        # problems:
        for question in self.questions:
            user_answer = question["question"].ask_and_evaluate()
            if user_answer is True:
                user_score += 1
            perfect_score += 1

        user_percentage = float(user_score) / perfect_score

        return user_percentage
