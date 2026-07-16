import webbrowser
import urllib.parse


class SearchService:

    @staticmethod
    def open_website(url):
        webbrowser.open(url)

    @staticmethod
    def google_search(query):

        query = urllib.parse.quote(query)

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

    @staticmethod
    def youtube_search(query):

        query = urllib.parse.quote(query)

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        )