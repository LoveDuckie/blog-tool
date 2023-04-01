from typing import Any
from markdown import preprocessors, postprocessors, inlinepatterns
from markdown.extensions import Extension
import xml.etree.ElementTree as element_tree


class CodeblockProcessor(inlinepatterns.InlineProcessor):
    def handleMatch(self, match, data):
        if not data:
            raise ValueError("The data handled is invalid or null")
        el = element_tree.Element('del')
        el.text = match.group(1)
        return el, match.start(0), match.end(0)


class CodeblockExtension(Extension):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        code_block_pattern = r'```[a-zA-Z]+(.*?)```'  # like --del--
        md.inlinePatterns.register(CodeblockProcessor(
            code_block_pattern, md), 'del', 175)
