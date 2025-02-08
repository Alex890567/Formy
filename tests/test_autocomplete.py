import pytest


class TestAutocomplete:

    @pytest.mark.autocomplete
    @pytest.mark.address
    def test_send_keys_to_address(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_address()
        assert testing_element == "Mountain View"

    @pytest.mark.autocomplete
    @pytest.mark.street_address
    def test_send_keys_to_street_address(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_street_address()
        assert testing_element == "Mountain View 23"

    @pytest.mark.autocomplete
    @pytest.mark.street_address_2
    def test_send_keys_to_street_address_2(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_street_address_2()
        assert testing_element == "Plain View 20"

    @pytest.mark.autocomplete
    @pytest.mark.city
    def test_send_keys_to_city(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_city()
        assert testing_element == "Houston"

    @pytest.mark.autocomplete
    @pytest.mark.state
    def test_send_keys_to_state(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_state()
        assert testing_element == "Texas"

    @pytest.mark.autocomplete
    @pytest.mark.zip_code
    def test_send_keys_to_zip_code(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_zip_code()
        assert testing_element == "1234"

    @pytest.mark.autocomplete
    @pytest.mark.country
    def test_send_keys_to_country(self, autocomplete_page):
        testing_element = autocomplete_page.send_keys_to_country()
        assert testing_element == "USA"