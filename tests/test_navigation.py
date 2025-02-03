import pytest


class TestNavigation:

    @pytest.mark.navigation
    @pytest.mark.autocomplete
    def test_navigation_to_autocomplete(self, navigation_page):
        testing_element = navigation_page.go_to_autocomplete()
        assert testing_element == "https://formy-project.herokuapp.com/autocomplete"

    @pytest.mark.navigation
    @pytest.mark.buttons
    def test_navigation_to_buttons(self, navigation_page):
        testing_element = navigation_page.go_to_buttons()
        assert testing_element == "https://formy-project.herokuapp.com/buttons"

    @pytest.mark.navigation
    @pytest.mark.checkbox
    def test_navigation_to_checkbox(self, navigation_page):
        testing_element = navigation_page.go_to_checkbox()
        assert testing_element == "https://formy-project.herokuapp.com/checkbox"

    @pytest.mark.navigation
    @pytest.mark.datepicker
    def test_navigation_to_datepicker(self, navigation_page):
        testing_element = navigation_page.go_to_datepicker()
        assert testing_element == "https://formy-project.herokuapp.com/datepicker"

    @pytest.mark.navigation
    @pytest.mark.drag_and_drop
    def test_navigation_to_drag_and_drop(self, navigation_page):
        testing_element = navigation_page.go_to_drag_and_drop()
        assert testing_element == "https://formy-project.herokuapp.com/dragdrop"

    @pytest.mark.navigation
    @pytest.mark.enabled_and_disabled_elements
    def test_navigation_to_enabled_and_disabled_elements(self, navigation_page):
        testing_element = navigation_page.go_to_enabled_and_disabled_elements()
        assert testing_element == "https://formy-project.herokuapp.com/enabled"

    @pytest.mark.navigation
    @pytest.mark.file_upload
    def test_navigation_to_file_upload(self, navigation_page):
        testing_element = navigation_page.go_to_file_upload()
        assert testing_element == "https://formy-project.herokuapp.com/fileupload"

    @pytest.mark.navigation
    @pytest.mark.key_and_mouse_press
    def test_navigation_to_key_and_mouse_press(self, navigation_page):
        testing_element = navigation_page.go_to_key_and_mouse_press()
        assert testing_element == "https://formy-project.herokuapp.com/keypress"

    @pytest.mark.navigation
    @pytest.mark.modal
    def test_navigation_to_modal(self, navigation_page):
        testing_element = navigation_page.go_to_modal()
        assert testing_element == "https://formy-project.herokuapp.com/modal"

    @pytest.mark.navigation
    @pytest.mark.page_scroll
    def test_navigation_to_page_scroll(self, navigation_page):
        testing_element = navigation_page.go_to_page_scroll()
        assert testing_element == "https://formy-project.herokuapp.com/scroll"

    @pytest.mark.navigation
    @pytest.mark.radio_button
    def test_navigation_to_radio_button(self, navigation_page):
        testing_element = navigation_page.go_to_radio_button()
        assert testing_element == "https://formy-project.herokuapp.com/radiobutton"