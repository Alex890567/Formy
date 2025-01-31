import pytest


@pytest.mark.autocomplete
class TestNavigation:
    def test_navigation_to_autocomplete(self, navigation_page):
        testing_element = navigation_page.go_to_autocomplete()
        assert testing_element == "https://formy-project.herokuapp.com/autocomplete"

    def test_navigation_to_buttons(self, navigation_page):
        testing_element = navigation_page.go_to_buttons()
        assert testing_element == "https://formy-project.herokuapp.com/buttons"

    def test_navigation_to_checkbox(self, navigation_page):
        testing_element = navigation_page.go_to_checkbox()
        assert testing_element == "https://formy-project.herokuapp.com/checkbox"

    def test_navigation_to_datepicker(self, navigation_page):
        testing_element = navigation_page.go_to_datepicker()
        assert testing_element == "https://formy-project.herokuapp.com/datepicker"

    def test_navigation_to_drag_and_drop(self, navigation_page):
        testing_element = navigation_page.go_to_drag_and_drop()
        assert testing_element == "https://formy-project.herokuapp.com/dragdrop"