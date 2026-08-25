class MediaError(Exception):
    """Raised when something that is not a media item is added to a catalogue."""

    def __init__(self, message: str, obj: object) -> None:
        super().__init__(message)
        self.obj = obj


class Movie:
    def __init__(self, title: str, year: int, director: str, duration: int) -> None:
        if not title.strip():
            raise ValueError("Title cannot be empty")
        if year < 1895:
            raise ValueError("Year must be 1895 or later")
        if not director.strip():
            raise ValueError("Director cannot be empty")
        if duration <= 0:
            raise ValueError("Duration must be positive")

        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self) -> str:
        return f"{self.title} ({self.year}) - {self.duration} min, {self.director}"


class TVSeries(Movie):
    def __init__(
        self,
        title: str,
        year: int,
        director: str,
        duration: int,
        seasons: int,
        total_episodes: int,
    ) -> None:
        super().__init__(title, year, director, duration)

        if seasons < 1:
            raise ValueError("Seasons must be 1 or greater")
        if total_episodes < 1:
            raise ValueError("Total episodes must be 1 or greater")

        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self) -> str:
        return (
            f"{self.title} ({self.year}) - {self.seasons} seasons, "
            f"{self.total_episodes} episodes, {self.duration} min avg, {self.director}"
        )


class MediaCatalogue:
    def __init__(self) -> None:
        self.items: list[Movie] = []

    def add(self, media_item: Movie) -> None:
        if not isinstance(media_item, Movie):
            raise MediaError("Only Movie or TVSeries instances can be added", media_item)
        self.items.append(media_item)

    def get_movies(self) -> list[Movie]:
        # exact type, not isinstance: TVSeries subclasses Movie and belongs in its own list
        return [item for item in self.items if type(item) is Movie]

    def get_tv_series(self) -> list[TVSeries]:
        return [item for item in self.items if isinstance(item, TVSeries)]

    def __str__(self) -> str:
        if not self.items:
            return "Media Catalogue (empty)"

        movies = self.get_movies()
        series = self.get_tv_series()

        lines = [f"Media Catalogue ({len(self.items)} items):", ""]

        if movies:
            lines.append("=== MOVIES ===")
            lines += [f"{index}. {movie}" for index, movie in enumerate(movies, 1)]
            lines.append("")

        if series:
            lines.append("=== TV SERIES ===")
            lines += [f"{index}. {show}" for index, show in enumerate(series, 1)]

        return "\n".join(lines)


if __name__ == "__main__":
    catalogue = MediaCatalogue()

    try:
        catalogue.add(Movie("The Matrix", 1999, "The Wachowskis", 136))
        catalogue.add(Movie("Inception", 2010, "Christopher Nolan", 148))
        catalogue.add(TVSeries("Scrubs", 2001, "Bill Lawrence", 24, 9, 182))
        catalogue.add(TVSeries("Breaking Bad", 2008, "Vince Gilligan", 47, 5, 62))
        print(catalogue)
    except ValueError as error:
        print(f"Validation Error: {error}")
    except MediaError as error:
        print(f"Media Error: {error}")
        print(f"Unable to add {error.obj}: {type(error.obj)}")
