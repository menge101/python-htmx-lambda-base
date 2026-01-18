from lib.components import banner, session
from typing import cast


def test_act(connection_thread_mock):
    session_data = cast(session.SessionData, {"yo:lo"})
    observed = banner.act(connection_thread_mock, session_data, {})
    expected = session_data, []
    assert observed == expected


def test_build_no_env():
    observed = banner.build()
    expected = {
        "body": '<div class="banner invisible">Environment name not set</div>',
        "cookies": [],
        "headers": {"Content-Type": "text/html"},
        "isBase64Encoded": False,
        "statusCode": 200,
    }
    assert observed == expected


def test_build_with_env(mocker):
    mocker.patch("lib.components.banner.os.environ.get", return_value="test")
    observed = banner.build()
    expected = {
        "body": '<div class="banner">This is the test environment</div>',
        "cookies": [],
        "headers": {"Content-Type": "text/html"},
        "isBase64Encoded": False,
        "statusCode": 200,
    }
    assert observed == expected
