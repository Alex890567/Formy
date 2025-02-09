class TestButtons:
    def test_click_primary_button(self, buttons_page):
        testing_element = buttons_page.click_primary_button()
        assert testing_element.is_enabled()