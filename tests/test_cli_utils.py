import io
import logging

import csvtools.cli_utils as cli_utils


def test_configure_logging_verbose_true(monkeypatch):
    captured = {}

    def fake_basic_config(**kwargs):
        captured.update(kwargs)

    monkeypatch.setattr(logging, "basicConfig", fake_basic_config)

    cli_utils.configure_logging(True)

    assert captured["level"] == logging.DEBUG
    assert captured["format"] == "%(asctime)s %(levelname)s %(message)s"


def test_configure_logging_verbose_false(monkeypatch):
    captured = {}

    def fake_basic_config(**kwargs):
        captured.update(kwargs)

    monkeypatch.setattr(logging, "basicConfig", fake_basic_config)

    cli_utils.configure_logging(False)

    assert captured["level"] == logging.INFO
    assert captured["format"] == "%(asctime)s %(levelname)s %(message)s"


def test_configure_stdin_encoding_with_reconfigure(monkeypatch):
    class FakeStdin:
        def __init__(self):
            self.encoding = None

        def reconfigure(self, encoding):
            self.encoding = encoding

    fake_stdin = FakeStdin()
    monkeypatch.setattr(cli_utils.sys, "stdin", fake_stdin)

    cli_utils.configure_stdin_encoding("latin-1")

    assert fake_stdin.encoding == "latin-1"


def test_configure_stdin_encoding_without_reconfigure(monkeypatch):
    # StringIO intentionally has no reconfigure attribute.
    fake_stdin = io.StringIO("col1,col2\n")
    monkeypatch.setattr(cli_utils.sys, "stdin", fake_stdin)

    cli_utils.configure_stdin_encoding("utf-16")

    assert not hasattr(fake_stdin, "reconfigure")
