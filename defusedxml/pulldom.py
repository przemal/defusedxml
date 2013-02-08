# defusedxml
#
# Copyright (c) 2013 by Christian Heimes <christian@python.org>
# Licensed to PSF under a Contributor Agreement.
# See http://www.python.org/psf/license for licensing details.

from xml.dom.pulldom import parse as _parse
from xml.dom.pulldom import parseString as _parseString
from .sax import make_parser

__origin__ = "xml.dom.pulldom"


def parse(stream_or_string, parser=None, bufsize=None, forbid_dtd=False,
          forbid_entities=True):
    if parser is None:
        parser = make_parser()
        parser.forbid_dtd = forbid_dtd
        parser.forbid_entities = forbid_entities
    return _parse(stream_or_string, parser, bufsize)


def parseString(string, parser=None, forbid_dtd=False, forbid_entities=True):
    if parser is None:
        parser = make_parser()
        parser.forbid_dtd = forbid_dtd
        parser.forbid_entities = forbid_entities
    return _parseString(string, parser)
