class Reviewer:
    """Model a proofreading specialist."""

    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def describe_reviewer(self):
        print(f"Reviewer: {self.name.title()}")
        print(f"Expertise: {self.expertise}")

li = Reviewer('li wen', 'medical devices')
chen = Reviewer('chen yu', 'legal contracts')

li.describe_reviewer()
chen.describe_reviewer()
