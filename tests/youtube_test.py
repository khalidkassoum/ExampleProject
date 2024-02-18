import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from infra.browser_wrapper import BrowserWrapper
from logic.youtube_page import YouTubePage, YouTubeCommentLogic
from logic.youtube_page import YouTubeVideoPlayer_page
from logic.youtube_page import YouTubeVoiceSearchLogic


class Youtube_Page_Test(unittest.TestCase):
    def test_check_title_for_search(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")
        self.youtube_page = YouTubePage(self.driver)
        self.youtube_page.search_flow("Python programming")
        time.sleep(5)# we need to use Explicit Wait insted
        self.assertIn("Python programming",self.youtube_page.get_page_title(),"the title not show")#test/logic



class YouTubeVideoPlayerTest(Youtube_Page_Test):

    def test_play_video(self):

       logic = YouTubeVideoPlayer_page(self.driver)
       logic.play_video("OpenAI GPT-3")
       self.assertTrue(logic.is_video_playing(), "Video is not playing")

class YouTubeLikeDislikeTest(unittest.TestCase):
    def test_like_dislike_video(self):
        self.browser = BrowserWrapper()
        video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        self.driver = self.browser.get_driver(video_url)

        logic = YouTubeVideoPlayer_page(self.driver)

        logic.like_video(video_url)
        time.sleep(5)
        self.assertTrue(self.logic.like_video(), "Video was not liked successfully")
        logic.dislike_video(video_url)
        self.assertTrue(self.is_disliked(), "Video was not disliked successfully")




class comment_test(unittest.TestCase):

        def test_write_comment(self):

            logic = YouTubeCommentLogic(self.driver)
            video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            comment_text = "This is a test comment"
            logic.write_comment(video_url, comment_text)
            self.assertTrue(logic.is_comment_present(video_url, comment_text), "Comment is not present")


class YouTubeVoiceSearchTest(unittest.TestCase):
    def test_voice_search(self):

        logic = YouTubeVoiceSearchLogic(self.driver)
        logic.perform_voice_search()
        search_results_count = logic.get_search_results()
        self.assertGreater(search_results_count, 0, "No search results found")

if __name__ == "__main__":
    unittest.main()
