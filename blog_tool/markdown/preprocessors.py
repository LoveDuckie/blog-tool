from typing import Any
from markdown import preprocessors, postprocessors, processor, inlinepatterns
from markdown.extensions import Extension
import xml.etree.ElementTree as etree


class CodeblockProcessor(inlinepatterns.InlineProcessor):
    def handleMatch(self, match, data):
        if not data:
            raise ValueError("The data handled is invalid or null")
        el = etree.Element('del')
        el.text = match.group(1)
        return el, match.start(0), match.end(0)


class CodeblockExtension(Extension):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        CODE_BLOCK_PATTERN = r'```[a-zA-Z]+(.*?)```'  # like --del--
        md.inlinePatterns.register(CodeblockProcessor(
            CODE_BLOCK_PATTERN, md), 'del', 175)
