class Person:
    def __init__(self, interests, age, bedtime, tolerance):
        self.interests = interests
        self.age = age
        self.bedtime = bedtime
        self.tolerance = tolerance

    def is_interested(self, movie):
        return False

    def is_allowed(self, movie):
        return False

    def can_attend(self, screening):
        return False

    def will_attend(self, screening):
        return False


if __name__ == '__main__':
    # you can run your tests here
    pass
