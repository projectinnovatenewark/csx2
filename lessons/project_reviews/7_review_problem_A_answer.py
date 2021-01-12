"""
In this review problem, you will create a class with a method and then call that method with an
instantiated class object.
"""

# TODO:
# Create a class called "Movie" with the attributes title, genre, and rating. Then define a method
# called "printer()". The method should print the statement "[title] is a(n) [genre] movie with a
# [rating]% rating on Rotten Tomatoes."
class Movie():
  # TODO: What function does every class need?

  def __init__(self, title, genre, rating):
    self.title = title
    self.genre = genre
    self.rating = rating

  def printer(self):
    # some code here
    print(f"{self.title} is a(n) {self.genre} movie with a {self.rating}% rating on Rotten Tomatoes.")

avengies = Movie("The Avengers", "Action", 91)
avengies.printer()