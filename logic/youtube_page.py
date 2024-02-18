from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from infra.base_page import BasePage
import time

class YouTubePage(BasePage):

    SEARCH_INPUT = "//input[@id='search']"

    def __init__(self,driver):
        super().__init__(driver)
        self.search_input = self._driver.find_element(By.XPATH,self.SEARCH_INPUT)

    def fill_search_input(self,text):
        self.search_input.send_keys(text)#logic

    def press_enter_on_search_input(self):
        self.search_input.send_keys(Keys.RETURN)

    def search_flow(self,text):
        self.fill_search_input(text)
        self.press_enter_on_search_input()

class YouTubeVideoPlayer_page:
        def __init__(self, driver):
            self.driver = driver

        def play_video(self, search_query):

            search_input = self.driver.find_element_by_name("search_query")
            search_input.send_keys(search_query)
            search_input.submit()
            first_video = self.driver.find_element_by_css_selector("ytd-video-renderer #thumbnail")
            first_video.click()

        def is_video_playing(self):

            try:
                video_player = self.driver.find_element_by_css_selector("video.video-stream.html5-main-video")
                return video_player.is_displayed()
            except:
                return False

        def like_video(self,video_url):
            self.driver.get(video_url)
            like_button = self.driver.find_element(By.CSS_SELECTOR, "ytd-toggle-button-renderer#button[aria-label='Like this video']")
            like_button.click()
            return like_button.is_displayed()


        def is_liked(self, like_button):
            # Check if the button is active
            return "style-default-active" in like_button.get_attribute("class")

        def dislike_video(self,video_url):
         self.driver.get(video_url)
         dislike_button = self.driver.find_element_by_css_selector(
            "ytd-menu-renderer #button[aria-label='Dislike this video']")
         dislike_button.click()



class YouTubeCommentLogic:
    def __init__(self, driver):
        self.driver = driver

    def write_comment(self, video_url, comment_text):

        self.driver.get(video_url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        comment_box = self.driver.find_element_by_css_selector("div#placeholder-area")
        comment_box.click()
        comment_input = self.driver.find_element_by_css_selector("div#contenteditable-root")
        comment_input.send_keys(comment_text)
        submit_button = self.driver.find_element_by_css_selector("ytd-button-renderer#submit-button")
        submit_button.click()

    def is_comment_present(self, video_url, comment_text):

        self.driver.get(video_url)
        comments_section = self.driver.find_element_by_css_selector("ytd-comments#comments")
        return comment_text in comments_section.text



class YouTubeVoiceSearchLogic:
    def __init__(self, driver):
        self.driver = driver

    def perform_voice_search(self):  
        voice_search_button = self.driver.find_element_by_css_selector("button#search-icon-legacy")
        voice_search_button.click()
        time.sleep(3)
        search_button = self.driver.find_element_by_css_selector("button#search-icon-legacy")
        search_button.click()

    def get_search_results(self):
        search_results = self.driver.find_elements_by_css_selector("ytd-video-renderer")
        return len(search_results)
