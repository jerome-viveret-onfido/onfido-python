import onfido

api = onfido.Api("My_API_Key")


def test_address_picker(requests_mock):
    mock_create = requests_mock.get("https://api.onfido.com/v3/addresses/pick?postcode=SW46EH", json=[])
    api.address.pick("SW46EH")
    assert mock_create.called is True

