class Reviewer:
    """Model a proofreading specialist."""

    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def describe_reviewer(self):
        print(f"Reviewer: {self.name.title()}")
        print(f"Expertise: {self.expertise}")

    def review_project(self):
        print(f"{self.name.title()} is reviewing the translation.")


reviewer = Reviewer('li wen', 'medical devices')
reviewer.describe_reviewer()
reviewer.review_project()
