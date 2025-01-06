class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating
    
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 10 >= new_rating > 0:
            self._rating = new_rating
        else:
            print("Enter a valid rating.")
    
my_movie = Movie("007 Golden Eye", 9)
print(my_movie.rating)

fav_movie = Movie("JOJO", 4.5)
print(fav_movie.rating)
fav_movie.rating = 4.6
print(fav_movie.rating)