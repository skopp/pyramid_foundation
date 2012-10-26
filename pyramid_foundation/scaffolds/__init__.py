# PyFo/pyfo/scaffolds/__init__.py

from pyramid.scaffolds import PyramidTemplate


class PyramidFoundationTemplate(PyramidTemplate):
    _template_dir = 'pyramid_foundation_template'
    summary = 'Pyramid scaffold to extend project with Foundation support'
