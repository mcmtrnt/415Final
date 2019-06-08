# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1560005955.8925235
_enable_loop = True
_template_filename = 'C:/Users/Trent/scraper/homepage/templates/account.html'
_template_uri = 'account.html'
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
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <p>Username: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( request.user.username ))
        __M_writer('</p>\r\n    <p>First Name: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( request.user.first_name ))
        __M_writer('</p>\r\n    <p>Last Name: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( request.user.last_name ))
        __M_writer('</p>\r\n    \r\n')
        if request.user.has_perm('homepage.view_ad'):
            __M_writer('        <a class="btn btn-outline-danger" href="/homepage/cancel/">Cancel My Subscription<span class="sr-only">(current)</span></a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/scraper/homepage/templates/account.html", "uri": "account.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "48": 3, "56": 3, "57": 4, "58": 4, "59": 5, "60": 5, "61": 6, "62": 6, "63": 8, "64": 9, "70": 64}}
__M_END_METADATA
"""
