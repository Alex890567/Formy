class TestAutocomplete:
    def test_send_keys_to_address(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_address()
        assert testing_element == "Mountain View"

    def test_send_keys_to_street_address(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_street_address()
        assert testing_element == "Mountain View 23"

    def test_send_keys_to_street_address_2(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_street_address_2()
        assert testing_element == "Plain View 20"

    def test_send_keys_to_city(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_city()
        assert testing_element == "Houston"

    def test_send_keys_to_state(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_state()
        assert testing_element == "Texas"

    def test_send_keys_to_zip_code(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_zip_code()
        assert testing_element == "1234"