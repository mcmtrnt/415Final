# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1560561640.3182378
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
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>Dirt Bike Deals</title>\r\n        <link rel="icon" href="/static/homepage/media/favicon.ico/">\r\n\r\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">\r\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>\r\n     \r\n        <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n        <header>         \r\n            <div class="nav navbar-default custom-nav justify-content-between">     \r\n                <img src= "')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/dirt bike deals words.PNG/" width="270px" height="60px">          \r\n                <!-- <h1>Dirt Bike Deals</h1> -->\r\n\r\n                <li class="nav-item active">\r\n                    <a class="btn btn-outline-primary" href="/homepage/index/">Home <span class="sr-only">(current)</span></a>\r\n                </li>\r\n                \r\n                <li class="nav-item active">\r\n                    <a class="btn btn-outline-primary" href="/homepage/deals/">Deals<span class="sr-only">(current)</span></a>\r\n                </li>\r\n                 \r\n')
        if request.user.has_perm('homepage.view_ad'):
            __M_writer('                    <li class="nav-item active">\r\n                        <a class="btn btn-outline-primary" href="/homepage/calculator/">Price my bike<span class="sr-only">(current)</span></a>\r\n                    </li>\r\n\r\n')
        else:
            __M_writer('                    <li class="nav-item active">\r\n                        <a class="btn btn-warning" href="/homepage/checkout/">Purchase Pro Account<span class="sr-only">(current)</span></a>\r\n                    </li>\r\n')
        __M_writer('                <div>\r\n                \r\n')
        if request.user.is_authenticated:
            __M_writer('                    <a class="btn btn-outline-secondary" href="/homepage/account/" role="button">My Account</a>\r\n                    <a class="btn btn-primary" href="/homepage/logout/" role="button">Logout</a>\r\n                \r\n')
        else:
            __M_writer('                    <a class="btn btn-primary" href="/homepage/login/" role="button">Login</a>\r\n                \r\n                    <a class="btn btn-secondary" href="/homepage/signup/" role="button">Sign Up</a> \r\n')
        __M_writer('                </div>                     \r\n            </div>   \r\n                       \r\n        </header>\r\n\r\n        <main>\r\n            \r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </main>\r\n\r\n        <footer>\r\n            <address>Contact Us: dirtbikedeals.online@gmail.com</address>\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
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
{"filename": "C:/Users/Trent/scraper/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "28": 2, "29": 11, "30": 19, "31": 20, "32": 20, "33": 26, "34": 26, "35": 37, "36": 38, "37": 42, "38": 43, "39": 47, "40": 49, "41": 50, "42": 53, "43": 54, "44": 58, "49": 67, "55": 65, "61": 65, "67": 61}}
__M_END_METADATA
"""
