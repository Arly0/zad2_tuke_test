class Movie:
    def __init__(self, title, length, genre, age_limit, release_date):
        self.title = title
        self.length = length
        self.genre = genre
        self.age_limit = age_limit
        self.release_date = release_date

    def validate_date(self, date):
        pass

    def get_time_passed(self, date):
        return 0


if __name__ == '__main__':
    # you can run your tests here
    pass
