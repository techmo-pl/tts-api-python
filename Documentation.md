# Techmo TTS Service API

## 1. TTS GRPC API
The service base API is defined by the proto file. The API includes functions listed below:

```
service TTS
{
	rpc GetServiceVersion(GetServiceVersionRequest) returns (GetServiceVersionResponse);
	rpc GetResourcesId(GetResourcesIdRequest) returns (GetResourcesIdResponse);

	rpc ListVoices(ListVoicesRequest) returns (ListVoicesResponse);
	rpc ListSoundIcons(ListSoundIconsRequest) returns (ListSoundIconsResponse);
	rpc ListRecordings(ListRecordingsRequest) returns (ListRecordingsResponse);
	rpc ListLexicons(ListLexiconsRequest) returns (ListLexiconsResponse);

	rpc SynthesizeStreaming(SynthesizeRequest) returns (stream SynthesizeResponse);
	rpc Synthesize(SynthesizeRequest) returns (SynthesizeResponse);

	rpc GetChannelsUsage(GetChannelsUsageRequest) returns (GetChannelsUsageResponse);

	rpc PutRecording(PutRecordingRequest) returns (PutRecordingResponse);
	rpc DeleteRecording(DeleteRecordingRequest) returns (DeleteRecordingResponse);
	rpc GetRecording(GetRecordingRequest) returns (GetRecordingResponse);

	rpc PutLexicon(PutLexiconRequest) returns (PutLexiconResponse);
	rpc DeleteLexicon(DeleteLexiconRequest) returns (DeleteLexiconResponse);
	rpc GetLexicon(GetLexiconRequest) returns (GetLexiconResponse);
}
```

### 1.1. Functions Definitions

#### GetServiceVersion
*rpc GetServiceVersion([GetServiceVersionRequest](#getserviceversionrequest)) returns ([GetServiceVersionResponse](#getserviceversionresponse))*

Returns the version of the service, in [SemVer](https://semver.org/) format.

#### GetResourcesId
*rpc GetResourcesId([GetResourcesIdRequest](#getresourcesidrequest)) returns ([GetResourcesIdResponse](#getresourcesidresponse))*

Returns an identifier of the resources used by the service.

#### ListVoices
*rpc ListVoices([ListVoicesRequest](#listvoicesrequest)) returns ([ListVoicesResponse](#listvoicesresponse))*

Lists all available voices which can be used to synthesize speech.

#### ListSoundIcons
*rpc ListSoundIcons([ListSoundIconsRequest](#listsoundiconsrequest)) returns ([ListSoundIconsResponse](#listsoundiconsresponse))*

Lists all sound icons (their keys) for the requested (*voice*, *variant*, *language*) tuple.

#### ListRecordings
*rpc ListRecordings([ListRecordingsRequest](#listrecordingsrequest)) returns ([ListRecordingsResponse](#listrecordingsresponse))*

Lists all recordings (their keys) for the requested (*voice*, *variant*, *language*) tuple.

#### ListLexicons
*rpc ListLexicons([ListLexiconsRequest](#listlexiconsrequest)) returns ([ListLexiconsResponse](#listlexiconsresponse))*

Lists all currently loaded lexicons which can be referred by [\<lexicon\>](https://www.w3.org/TR/speech-synthesis11/#S3.1.5.1) tag in synthesize requests.

#### SynthesizeStreaming
*rpc SynthesizeStreaming([SynthesizeRequest](#synthesizerequest)) returns (stream [SynthesizeResponse](#synthesizeresponse))*

Synthesizes the speech (audio signal) based on the requested phrase and the optional configuration.<br/>
Returns audio signal with synthesized speech (streaming version, one or more response packets).

#### Synthesize
*rpc Synthesize([SynthesizeRequest](#synthesizerequest)) returns ([SynthesizeResponse](#synthesizeresponse))*

Synthesizes the speech (audio signal) based on the requested phrase and the optional configuration.<br/>
Returns audio signal with synthesized speech (non-streaming version, always one response packet).

#### GetChannelsUsage
*rpc GetChannelsUsage([GetChannelsUsageRequest](#getchannelsusagerequest)) returns ([GetChannelsUsageResponse](#getchannelsusageresponse))*

Returns the info containing number of total available channels and channels currently in use.

#### PutRecording
*rpc PutRecording([PutRecordingRequest](#putrecordingrequest)) returns ([PutRecordingResponse](#putrecordingresponse))*

Adds a new recording with the requested key for the requested voice, or overwrites the existing one if there is already such a recording defined.

**Note:**<br/>
Licence must allow reconfiguration, otherwise *PERMISSION_DENIED* error is returned.

#### DeleteRecording
*rpc DeleteRecording([DeleteRecordingRequest](#deleterecordingrequest)) returns ([DeleteRecordingResponse](#deleterecordingresponse))*

Removes the recording with the requested key from the list of recordings of the requested voice.

**Note:**<br/>
Licence must allow reconfiguration, otherwise *PERMISSION_DENIED* error is returned.

#### GetRecording
*rpc GetRecording([GetRecordingRequest](#getrecordingrequest)) returns ([GetRecordingResponse](#getrecordingresponse))*

Sends back the content of the recording with the requested key for the requested voice, data is returned in the linear PCM16 format.

#### PutLexicon
*rpc PutLexicon([PutLexiconRequest](#putlexiconrequest)) returns ([PutLexiconResponse](#putlexiconresponse))*

Adds a new lexicon with the requested name or overwrites the existing one if there is already a lexicon with such name.

**Note:**<br/>
Licence must allow reconfiguration, otherwise *PERMISSION_DENIED* error is returned.

#### DeleteLexicon
*rpc DeleteLexicon([DeleteLexiconRequest](#deletelexiconrequest)) returns ([DeleteLexiconResponse](#deletelexiconresponse))*

Removes the lexicon with the requested name.

**Note:**<br/>
Licence must allow reconfiguration, otherwise *PERMISSION_DENIED* error is returned.

#### GetLexicon
*rpc GetLexicon([GetLexiconRequest](#getlexiconrequest)) returns ([GetLexiconResponse](#getlexiconresponse))*

Sends back the content of the lexicon with the requested name.

### 1.2. Requests and Responses Definitions

#### GetServiceVersionRequest
The request message for *[GetServiceVersion](#getserviceversion)* function. The message is empty.

#### GetServiceVersionResponse
The version info returned by *[GetServiceVersion](#getserviceversion)* function.

| Field     | Type     | Description |
| --------- | -------- | ----------- |
| *version* | *string* | Version of the sevice, in [SemVer](https://semver.org/) format. |

#### GetResourcesIdRequest
The request message for *[GetResourcesId](#getresourcesid)* function. The message is empty.

#### GetResourcesIdResponse
The identifier returned by *[GetResourcesId](#getresourcesid)* function.

| Field | Type     | Description |
| ----- | -------- | ----------- |
| *id*  | *string* | Identifier of the resource pack the service is started with. |

Identifier is an free-form string, which uniquely identifies a resource pack provided with the service.

#### ListVoicesRequest
The request message for *[ListVoices](#listvoices)* function.

| Field      | Type     | Description |
| ---------- | -------- | ----------- |
| *language_code* | *string* | [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code with an optional dialect.<br/>Optional. When non-empty, limits the listed voices to the voices supporting the requested language. |

#### ListVoicesResponse
The listing of available voices returned by *[ListVoices](#listvoices)* function.

| Field              | Type    | Description  |
| ------------------ | ------- | ------------ |
| *sampling_rate_hz* | *int32* | The sampling rate in Hz of all voices (it is identical for all available voices). |
| *voices*           | *[VoiceInfo](#voiceinfo)* (repeated) | The list of all available voices or voices supporting the requested language. |

#### ListSoundIconsRequest
The request message for *[ListSoundIcons](#listsoundicons)* function.

| Field           | Type | Description |
| --------------- | ---- | ----------- |
| *voice_profile* | *[VoiceProfile](#voiceprofile)* | Profile of the voice to list the sound icons for. |

#### ListSoundIconsResponse
The result of the *[ListSoundIcons](#listsoundicons)* function.

| Field     | Type                | Description |
| --------- | ------------------- | ----------- |
| *keys*    | *string* (repeated) | The list of keys of all available sound icons for the requested voice profile. |

#### ListRecordingsRequest
The request message for *[ListRecordings](#listrecordings)* function.

| Field           | Type | Description |
| --------------- | ---- | ----------- |
| *voice_profile* | *[VoiceProfile](#voiceprofile)* | Profile of the voice to list the recordings for. |

#### ListRecordingsResponse
The result of the *[ListRecordings](#listrecordings)* function.

| Field     | Type                | Description |
| --------- | ------------------- | ----------- |
| *keys*    | *string* (repeated) | The list of keys of all available recordings for the requested voice profile. |

#### ListLexiconsRequest
The request message for *[ListLexicons](#listlexicons)* function.

| Field           | Type     | Description |
| --------------- | -------- | ----------- |
| *language_code* | *string* | [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code with an optional dialect.<br/>Optional. When non-empty, limits the listed lexicons to the lexicons supprting the requested language. |

#### ListLexiconsResponse
The result of the *[ListLexicons](#listlexicons)* function.

| Field      | Type                   | Description |
| ---------- | ---------------------- | ----------- |
| *lexicons* | *[LexiconInfo](#lexiconinfo)* (repeated) | The list of all available lexicons. |

#### SynthesizeRequest
The request message for *[SynthesizeStreaming](#synthesizestreaming)* and *[Synthesize](#synthesize)* functions.

| Field              | Type            | Description |
| ------------------ | --------------- | ----------- |
| *text*             | *string*        | A phrase to be synthesized. |
| *synthesis_config* | *[SynthesisConfig](#synthesisconfig)* | Optional. Tweaks the default service synthesis configuration. |
| *output_config*    | *[OutputConfig](#outputconfig)*       | Optional. Overrides the default output audio properties. |

The message contains a phrase to be synthesized and optional configurations.<br/>
The phrase to synthesize is either a plain text in orthographic form, or a subset of [SSML](https://w3.org/TR/speech-synthesis11/).
Consult the service documentation for the full list of supported SSML tags.<br/>
*synthesis_config*'s fields can be set to specify parameters of synthesis (language, voice, prosodic properties, etc.),
and *output_config* alters the format of the output (sampling rate, PCM16 or encoding like Ogg/Vorbis compression).

#### SynthesizeResponse
The result of the *[SynthesizeStreaming](#synthesizestreaming)* and *[Synthesize](#synthesize)* functions.

| Field              | Type     | Description |
| ------------------ | -------- | ----------- |
| *sampling_rate_hz* | *int32*  | Sampling rate of the returned audio in hertz. |
| *audio*            | *bytes*  | Audio data bytes either as Linear PCM (uncompressed 16-bit signed little-endian samples),<br/>or encoded if requested by *output_config*. |
| *warnings*         | *string* (repeated) | All the warnings generated by the service during processing of the request. |

During *[SynthesizeStreaming](#synthesizestreaming)*, a series of one or more such messages are streamed back to the caller.<br/>
On the other hand, *[Synthesize](#synthesize)* simply returns exactly one response message.

#### GetChannelsUsageRequest
The request message for *[GetChannelsUsage](#getchannelsusage)* function. The message is empty.

#### GetChannelsUsageResponse
The result of the *[GetChannelsUsage](#getchannelsusage)* function.

| Field                  | Type    | Description |
| ---------------------- | ------- | ----------- |
| *total_channels_count* | *int32* | The number of all available channels for the service, set by the licence.<br/>*INT_MAX* means unrestricted access. |
| *used_channels_count*  | *int32* | The number of channels currently in use. |

#### PutRecordingRequest
The request message for *[PutRecording](#putrecording)* function.

| Field              | Type     | Description |
| ------------------ | -------- | ----------- |
| *voice_profile*    | *[VoiceProfile](#voiceprofile)* | Profile of the voice to put the recording for. |
| *recording_key*    | *string* | The key of the new recording. |
| *sampling_rate_hz* | *int32*  | Sampling rate of the recording audio data in Hertz. |
| *content*          | *bytes*  | The recording audio data, in linear PCM16 format. |

If there already exists a recording with such key for the requested voice profile, the existing recording content is overwritten.

#### PutRecordingResponse
The result of the *[PutRecording](#putrecording)* function. The message is empty, the response is used to verify returned GRPC status.

#### DeleteRecordingRequest
The request message for *[DeleteRecording](#deleterecording)* function.

| Field           | Type     | Description |
| --------------- | -------- | ----------- |
| *voice_profile* | *[VoiceProfile](#voiceprofile)* | Profile of the voice to look for the recording. |
| *recording_key* | *string* | The requested key of the recording (unique for any given voice profile). |

#### DeleteRecordingResponse
The result of the *[DeleteRecording](#deleterecording)* function. Message is empty, is used to verify returned GRPC status.

#### GetRecordingRequest
The request message for *[GetRecording](#getrecording)* function.

| Field           | Type     | Description |
| --------------- | -------- | ----------- |
| *voice_profile* | *[VoiceProfile](#voiceprofile)* | Profile of the voice to look for the recording. |
| *recording_key* | *string* | The requested key of the recording (unique for any given voice profile). |

#### GetRecordingResponse
The result of the *[GetRecording](#getrecording)* function.

| Field              | Type    | Description |
| ------------------ | ------- | ----------- |
| *sampling_rate_hz* | *int32* | Sampling rate of the recording audio data in Hertz. |
| *content*          | *bytes* | The recording audio data, in linear PCM16 format. |

#### PutLexiconRequest
The request message for *[PutLexicon](#putlexicon)* function.

| Field     | Type     | Description  |
| --------- | -------- | ------------ |
| *uri*     | *string* | URI of the lexicon, used as *uri* attribute of [\<lexicon\>](https://www.w3.org/TR/speech-synthesis11/#S3.1.5.1) tags in synthesize requests. |
| *outside_lookup_behaviour* | *[OutsideLookupBehaviour](#outsidelookupbehaviour)* | Can lexicon be selected for phrases outside of [\<lookup\>](https://www.w3.org/TR/speech-synthesis11/#S3.1.5.2) SSML tags. |
| *content* | *string* | A content of the lexicon, shall comply to [PLS](https://www.w3.org/TR/pronunciation-lexicon/). |

The service supports only a subset of [PLS](https://www.w3.org/TR/pronunciation-lexicon/). Consult the service documentation for the full list of supported PLS tags.

#### PutLexiconResponse
The result of the *[PutLexicon](#putlexicon)* function. Message is empty, the response is used to verify returned GRPC status.

#### DeleteLexiconRequest
The request message for *[DeleteLexicon](#deletelexicon)* function.

| Field | Type     | Description |
| ----- | -------- | ----------- |
| *uri* | *string* | URI of the lexicon to delete. |

#### DeleteLexiconResponse
The result of the *[DeleteLexicon](#deletelexicon)* function. Message is empty, is used to verify returned GRPC status.

#### GetLexiconRequest
The request message for *[GetLexicon](#getlexicon)* function.

| Field | Type     | Description |
| ----- | -------- | ----------- |
| *uri* | *string* | URI of the lexicon to list its content. |

#### GetLexiconResponse
The result of the *[GetLexicon](#getlexicon)* function.

| Field  | Type       | Description |
| ------ | ---------- | ----------- |
| *outside_lookup_behaviour* | *[OutsideLookupBehaviour](#outsidelookupbehaviour)* | Can lexicon be selected for phrases outside of [\<lookup\>](https://www.w3.org/TR/speech-synthesis11/#S3.1.5.2) SSML tags. |
| *content* | *string* | If successful, contains the content of the lexicon, in [PLS](https://www.w3.org/TR/pronunciation-lexicon/) format. |

#### VoiceProfile
Provides information about voice, its variant, and language code as a selector for set of sound icons and predefined recordings.

| Field           | Type     | Description |
| --------------- | -------- | ----------- |
| *voice_name*    | *string* | The voice name to look for the recording. |
| *voice_variant* | *int32*  | The variant of the voice to look for the recording. |
| *language_code* | *string* | [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code with an optional dialect to look for the recording. |

#### SynthesisConfig
Provides information to the synthesizer that specifies how to process the request.

| Field               | Type              | Description  |
| ------------------- | ----------------- | ------------ |
| *language_code*     | *string*          | [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code with an optional dialect of text to be synthesized.<br/>may be overridden by SSML tags in request text. |
| *voice*             | *[Voice](#voice)* | Requested voice to be used to synthesize the text.<br/>May be overridden by SSML tags in request text. |
| *prosodic_properties* | *[ProsodicProperties](#prosodicproperties)* | Optional. Defines the parameters of synthesized speech. |
| *silence_duration_between_segments_ms* | *int32* | Optional. Overrides the configured value for duration of silence between segments, in milliseconds. |

If there is no voice satisfying all the required criteria defined by the *voice* field, the voice is selected according to *name* (if defined) first, *gender* (if defined) second, and *age* (if defined) third.

#### OutputConfig
Defines the parameters of the output audio.

| Field              | Type    | Description |
| ------------------ | ------- | ----------- |
| *audio_encoding*   | *[AudioEncoding](#audioencoding)* | Requested format of the output audio stream. |
| *sampling_rate_hz* | *int32* | Desired sampling frequency in Hertz of synthesized audio. The value 0 means use the default Synthesizer sampling rate. |
| *max_frame_size*   | *int32* | Maximum frame size sent at once to the client to enable *RTF Throttling* (default=0, throttling disabled). |

When RTF Throttling is enabled, the RTF (**R**eal **T**ime **F**actor) is throttled to 1.0, with one frame (with *max_frame_size* size) sent in advance.
The frame size is expressed in samples, regardless of *audio_encoding* used (frame size expressed in bytes would likely be far smaller if output is not *PCM16*).
Enabling RTF Throttling guarantees that when connection is interrupted, the respective channel is freed after time no longer than the playback time of a one frame.

RTF Throttling is effective only for *[TTS::SynthesizeStreaming](#synthesizestreaming)* calls. It is silently ignored for *[TTS::Synthesize](#synthesize)* calls.

#### Voice
Voice definition used to describe requested voice in *[SynthesisConfig](#synthesisconfig)*.

| Field     | Type     | Description            |
| --------- | -------- | ---------------------- |
| *name*    | *string* | The name of the voice. If empty, it is not taken into account in voice selection. |
| *gender*  | *[Gender](#gender)* (optional) | Gender of the voice. If not set, it is not taken into account in voice selection. |
| *age*     | *[Age](#age)* (optional) | Age of the voice. If not set, it is not taken into account in voice selection. |
| *variant* | *int32*  | Variant of the voice. |

#### ProsodicProperties
Prosodic properties of the speech to be synthesized.

| Field    | Type    | Description |
| -------- | ------- | ----------- |
| *pitch*  | *float* | The average speech pitch scaling factor. The value 1.0 is a neutral value. |
| *range*  | *float* | The pitch range scaling factor. The value 1.0 is a neutral value. |
| *rate*   | *float* | The speech rate (speed) scaling factor. The value 1.0 is a neutral value. |
| *stress* | *float* | The speech stress scaling factor. The value 1.0 is a neutral value. |
| *volume* | *float* | The speech volume scaling factor. The value 1.0 is a neutral value. |

#### VoiceInfo
Information about a voice, returned by *[ListVoices](#listvoices)* function.

| Field                 | Type | Description |
| --------------------- | ---- | ----------- |
| *supported_languages* | *string* (repeated) | The list of [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) codes of languages supported by the voice. |
| *name*                | *string* | The name of the voice. |
| *gender*              | *[Gender](#gender)* | Gender of the voice. |
| *age*                 | *[Age](#age)* | Age of the voice. |
| *variants_count*      | *int32* | The number of variants of the voice (at least one). |

#### LexiconInfo
Lexicon uri and behaviour outside lookup tags returned by *[ListLexicons](#listlexicons)* function.

| Field                      | Type     | Description |
| -------------------------- | -------- | ----------- |
| *uri*                      | *string* | URI of the lexicon, used as *uri* attributes of [\<lexicon\>](https://www.w3.org/TR/speech-synthesis11/#S3.1.5.1) tags in synthesize requests. |
| *outside_lookup_behaviour* | *[OutsideLookupBehaviour](#outsidelookupbehaviour)* | Can lexicon be selected for phrases outside of [\<lookup\>](https://www.w3.org/TR/speech-synthesis11/#S3.1.5.2) SSML tags. |

### 1.3. Enumerations

#### Gender
Enum type, indicates the gender of the voice.

| Name     | Number |
| -------- | -------|
| *FEMALE* | 0      |
| *MALE*   | 1      |

#### Age
Enum type, indicates the age of the voice.

| Name     | Number | Description |
| -------- | ------ | ----------- |
| *ADULT*  | 0      | Selected for [SSML](https://www.w3.org/TR/speech-synthesis11/#S3.2.1) *age* attribute in range (16 - 60\]. Default. |
| *CHILD*  | 1      | Selected for [SSML](https://www.w3.org/TR/speech-synthesis11/#S3.2.1) *age* attribute in range \[0 - 16\]. |
| *SENILE* | 2      | Selected for [SSML](https://www.w3.org/TR/speech-synthesis11/#S3.2.1) *age* attribute in range (60 - *inf*). |

#### AudioEncoding
Enum type, indicates the requested format of the response audio data.

| Name         | Number | Description |
| ------------ | ------ | ----------- |
| *PCM16*      | 0      | Uncompressed 16-bit signed integer samples, without any header. |
| *OGG_VORBIS* | 1      | [Ogg](https://en.wikipedia.org/wiki/Ogg)/[Vorbis](https://en.wikipedia.org/wiki/Vorbis) encoded data stream. |
| *OGG_OPUS*   | 2      | [Ogg](https://en.wikipedia.org/wiki/Ogg)/[Opus](https://en.wikipedia.org/wiki/Opus_(audio_format)) encoded data stream. |
| *A_LAW*      | 3      | [ITU-T G.711](https://en.wikipedia.org/wiki/G.711) A-law encoded stream. |
| *MU_LAW*     | 4      | [ITU-T G.711](https://en.wikipedia.org/wiki/G.711) mu-law encoded stream. |

**Note:**<br/>
When using Ogg/Opus encoding, only 8kHz, 12kHz, 16kHz, 24kHz, and 48kHz sampling rates are allowed.

#### OutsideLookupBehaviour
Enum type, indicates if is lexicon allowed to be matched even for phrases outside of [\<lookup\>](https://www.w3.org/TR/speech-synthesis11/#S3.1.5.2) SSML tags.

| Name         | Number |
| ------------ | ------ |
| *ALLOWED*    | 0      |
| *DISALLOWED* | 1      |
