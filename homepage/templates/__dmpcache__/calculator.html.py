# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555432152.488879
_enable_loop = True
_template_filename = 'C:/Users/Trent/scraper/homepage/templates/calculator.html'
_template_uri = 'calculator.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        value = context.get('value', UNDEFINED)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        value = context.get('value', UNDEFINED)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div class="container-fluid">\r\n        <div class="row content">\r\n            <div class="col-sm-3">\r\n        \r\n            </div>\r\n        \r\n            <div class="col-sm-6">\r\n                <div class="content">\r\n                    <div class="wrapper">\r\n                        <div id="formContent">\r\n                            <form method="POST">\r\n                                <div><p>Enter Dirt Bike Information</p></div>\r\n                                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form.as_table()))
        __M_writer('\r\n                                <input type="submit" value="Predict">\r\n                                \r\n                                <div><p></p></div>\r\n                                \r\n                            </form> \r\n                        </div>\r\n                    </div>\r\n                </div>\r\n\r\n            </div>\r\n\r\n            <div class="col-sm-3">\r\n                <h4>Prediction:</h4>\r\n                <p>We recommend you price your bike at <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( value ))
        __M_writer('</strong></p>\r\n\r\n                \r\n\r\n            </div>\r\n\r\n        </div>\r\n    </div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/scraper/homepage/templates/calculator.html", "uri": "calculator.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "49": 3, "58": 3, "59": 17, "60": 17, "61": 31, "62": 31, "68": 62}}
__M_END_METADATA
"""
