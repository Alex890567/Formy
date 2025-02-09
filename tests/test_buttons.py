class TestButtons:
    def test_click_primary_button(self, buttons_page):
        testing_element = buttons_page.click_primary_button()
        assert testing_element.is_enabled()

    def test_click_success_button(self, buttons_page):
        testing_element = buttons_page.click_success_button()
        assert testing_element.is_enabled()

    def test_click_info_button(self, buttons_page):
        testing_element = buttons_page.click_info_button()
        assert testing_element.is_enabled()

    def test_click_warning_button(self, buttons_page):
        testing_element = buttons_page.click_warning_button()
        assert testing_element.is_enabled()

    def test_click_danger_button(self, buttons_page):
        testing_element = buttons_page.click_danger_button()
        assert testing_element.is_enabled()

    def test_click_link_button(self, buttons_page):
        testing_element = buttons_page.click_link_button()
        assert testing_element.is_enabled()

    def test_click_left_button(self, buttons_page):
        testing_element = buttons_page.click_left_button()
        assert testing_element.is_enabled()