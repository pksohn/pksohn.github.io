import jinja2
from jinja2 import FileSystemLoader
import markdown
import os
import argparse

here = os.path.dirname(os.path.realpath(__file__))

# Inspiration from https://gist.github.com/glombard/7554134

HTML_TEMPLATE = """
{% extends "base.html" %}

{% macro get_html() %}
{{ content | markdown }}
{% endmacro %}

{% block content %}
{% set html_content = get_html() %}
{{ html_content }}
{% endblock %}
"""


def render_markdown():
    with open('home.md') as mf:
        new_path = os.path.join(here, 'index.html')
        the_markdown = mf.read()

    md = markdown.Markdown(extensions=['meta'])

    env = jinja2.Environment()
    env.loader = FileSystemLoader('./templates')
    env.filters['markdown'] = lambda text: jinja2.Markup(md.convert(text))
    env.globals['get_title'] = lambda: md.Meta['title'][0]
    env.trim_blocks = True
    env.lstrip_blocks = True

    with open(new_path, 'w') as new:
        new.write(env.from_string(HTML_TEMPLATE).render(
            content=the_markdown))


render_markdown()
