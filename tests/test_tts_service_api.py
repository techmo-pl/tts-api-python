import pytest


@pytest.fixture
def tts_service_api() -> object:
    import tts_service_api.techmo_tts_api

    return tts_service_api.techmo_tts_api


@pytest.fixture(
    params=(
        "GetServiceVersionRequest",
        "GetServiceVersionResponse",
        "GetResourcesIdRequest",
        "GetResourcesIdResponse",
        "ListVoicesRequest",
        "ListVoicesResponse",
        "ListSoundIconsRequest",
        "ListSoundIconsResponse",
        "ListRecordingsRequest",
        "ListRecordingsResponse",
        "ListLexiconsRequest",
        "ListLexiconsResponse",
        "SynthesizeRequest",
        "SynthesizeResponse",
        "GetChannelsUsageRequest",
        "GetChannelsUsageResponse",
        "PutRecordingRequest",
        "PutRecordingResponse",
        "DeleteRecordingRequest",
        "DeleteRecordingResponse",
        "GetRecordingRequest",
        "GetRecordingResponse",
        "PutLexiconRequest",
        "PutLexiconResponse",
        "DeleteLexiconRequest",
        "DeleteLexiconResponse",
        "GetLexiconRequest",
        "GetLexiconResponse",
        "VoiceProfile",
        "Marker",
        "SynthesisConfig",
        "OutputConfig",
        "Voice",
        "ProsodicProperties",
        "VoiceInfo",
        "LexiconInfo",
    ),
)
def tts_service_api_attr(request) -> str:
    return request.param


@pytest.mark.parametrize(
    "api, attr",
    (
        pytest.param(
            pytest.lazy_fixture("tts_service_api"),
            pytest.lazy_fixture("tts_service_api_attr"),
            marks=pytest.mark.api("."),
        ),
    ),
)
def test_hasattr(api: object, attr: str):
    assert hasattr(api, attr)
