import webbrowser
import urllib.parse


class SearchService:

    @staticmethod
    def open_google():
        webbrowser.open("https://www.google.com")

    @staticmethod
    def open_youtube():
        webbrowser.open("https://www.youtube.com")

    @staticmethod
    def open_github():
        webbrowser.open("https://github.com")

    @staticmethod
    def open_chatgpt():
        webbrowser.open("https://chat.openai.com")

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