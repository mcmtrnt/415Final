# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555713960.7520123
_enable_loop = True
_template_filename = 'C:/Users/Trent/scraper/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>Dirt Bike Deals</title>\r\n        <link rel="icon" href="/static/homepage/media/favicon.ico/">\r\n\r\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">\r\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>\r\n\r\n\r\n        \r\n        <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n        <header>         \r\n            <div class="nav navbar-default custom-nav justify-content-between">               \r\n                    <h1>Dirt Bike Deals</h1>\r\n\r\n                    <!-- <li class="nav-item active"> -->\r\n                        <!-- <a class="btn btn-outline-primary" href="/homepage/index/">Home <span class="sr-only">(current)</span></a> -->\r\n                    <!-- </li> -->\r\n                  \r\n                    <li class="nav-item active">\r\n                        <a class="btn btn-outline-primary" href="/homepage/deals/">Deals<span class="sr-only">(current)</span></a>\r\n                    </li>\r\n                   \r\n              \r\n                    <li class="nav-item active">\r\n                        <a class="btn btn-outline-primary" href="/homepage/calculator/">Price my bike<span class="sr-only">(current)</span></a>\r\n                    </li>\r\n\r\n\r\n                    <div>\r\n                        \r\n                    <!-- <a class="btn btn-primary" href="/homepage/logout/" role="button">Logout</a> -->\r\n                    \r\n                \r\n                    <!-- <a class="btn btn-primary" href="/homepage/login/" role="button">Login</a> -->\r\n                  \r\n                    <!-- <a class="btn btn-secondary" href="/homepage/signup/" role="button">Sign Up</a>  -->\r\n                    \r\n                    </div>                     \r\n            </div>   \r\n                       \r\n        </header>\r\n\r\n        <main>\r\n            \r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </main>\r\n\r\n        <footer>\r\n\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                Site content goes here in sub-templates.\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/scraper/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "26": 2, "27": 11, "28": 21, "29": 22, "30": 22, "35": 62, "41": 60, "47": 60, "53": 47}}
__M_END_METADATA
"""
