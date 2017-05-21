import jinja2
from jinja2 import FileSystemLoader
import markdown
import os
import argparse

here = os.path.dirname(os.path.realpath(__file__))

templates = os.path.join(here, 'templates')
posts = os.path.join(here, 'posts')

all_md_files = [os.path.join(posts, f)
                for f in os.listdir(posts)
                if f.endswith('.md')]

parser = argparse.ArgumentParser()
parser.add_argument('markdown', nargs='?',
                    help='path to markdown file(s) to process',
                    default=all_md_files)

args = parser.parse_args()

# Inspiration from https://gist.github.com/glombard/7554134

HTML_TEMPLATE = """
{% extends "posts.html" %}

{% macro get_html() %}
{{ content | markdown }}
{% endmacro %}

{% block content %}
{% set html_content = get_html() %}
{{ html_content }}
{% endblock %}

{% block title %}
{% set html_content = get_html() %}
{{ get_title() }}
{% endblock %}

"""


def render_markdown(path):
    with open(path) as mf:
        fp, fn = os.path.split(path)
        name = fn.split('.')[0]
        html_name = '{}.html'.format(name)
        new_path = os.path.join(fp, html_name)
        the_markdown = mf.read()

    md = markdown.Markdown(extensions=['meta'])

    env = jinja2.Environment()
    env.loader = FileSystemLoader(templates)
    env.filters['markdown'] = lambda text: jinja2.Markup(md.convert(text))
    env.globals['get_title'] = lambda: md.Meta['title'][0]
    env.trim_blocks = True
    env.lstrip_blocks = True

    with open(new_path, 'w') as new:
        new.write(env.from_string(HTML_TEMPLATE).render(
            content=the_markdown))


for i in args.markdown:
    render_markdown(i)
