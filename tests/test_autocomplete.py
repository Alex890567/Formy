class TestAutocomplete:
    def test_send_keys_to_address(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_address()
        assert testing_element == "Mountain View"