# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554952678.8029225
_enable_loop = True
_template_filename = 'C:/Users/Trent/scraper/homepage/templates/signup.html'
_template_uri = 'signup.html'
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
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content">\r\n        <div class="wrapper">\r\n            <div id="formContent">\r\n              <!-- Tabs Titles -->\r\n          \r\n                <div>\r\n                    <p style="font-size: 1.5rem;">Create a free account</p>\r\n                </div>\r\n          \r\n              <!-- Login Form -->\r\n              \r\n              <form method="POST">\r\n                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form.as_table()))
        __M_writer('\r\n                <input type="submit" value="Sign Up">\r\n              </form>\r\n              \r\n          \r\n              <!-- Remind Password -->\r\n              <div id="formFooter">\r\n                <a class="underlineHover" href="/homepage/login/">Log In</a>\r\n              </div>\r\n          \r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/scraper/homepage/templates/signup.html", "uri": "signup.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "48": 3, "56": 3, "57": 16, "58": 16, "64": 58}}
__M_END_METADATA
"""
