

from blog_tool.models.blog import Blog
from blog_tool.exporters.exporter_interface import ExporterInterface
from blog_tool.utility.types.utility_constructor import _init_parameter
import rich_click as click

from blog_tool.logging.blog_tool_logger import get_logger

logger = get_logger()


class HtmlMarkoExporter(ExporterInterface):
    def __init__(self, *args, **kwargs) -> None:
        _init_parameter(self, "stylesheets", kwargs)
        super().__init__(*args, **kwargs)

    def extend_cli(self, cli_group: click.Group):
        return super().extend_cli(cli_group)

    def export(self, blog: Blog, target_output_path: str):
        super().export(blog, target_output_path)

        blog_content = blog.content
        if blog_content is None:
            raise ValueError("The blog content is invalid or null")
