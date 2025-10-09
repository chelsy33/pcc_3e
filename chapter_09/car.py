# 知识点：在类中封装属性与方法，跟踪车辆状态。

class TranslationProject:
    """A simple model of a translation project."""

    def __init__(self, client, language_pair):
        self.client = client
        self.language_pair = language_pair
        self.status = 'preparation'
        self.word_count = 0

    def update_word_count(self, words):
        self.word_count += words

    def describe_project(self):
        print(f"Client: {self.client}")
        print(f"Language pair: {self.language_pair}")
        print(f"Status: {self.status}")
        print(f"Word count: {self.word_count}")

    def advance_status(self, new_status):
        self.status = new_status


project = TranslationProject('GlobalTech', 'EN->ZH')
project.update_word_count(3200)
project.advance_status('translation')
project.describe_project()
