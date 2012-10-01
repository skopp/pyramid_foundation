# PyFo/pyfo/scaffolds/__init__.py

from pyramid.scaffolds import PyramidTemplate


class PyramidFoundationTemplate(PyramidTemplate):
    _template_dir = 'pyramidfoundation_template'
    summary = 'A scaffold for Zurb Foundation support'
