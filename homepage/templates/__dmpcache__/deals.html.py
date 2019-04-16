# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555436623.101935
_enable_loop = True
_template_filename = 'C:/Users/Trent/scraper/homepage/templates/deals.html'
_template_uri = 'deals.html'
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
        len = context.get('len', UNDEFINED)
        bikes = context.get('bikes', UNDEFINED)
        range = context.get('range', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<meta http-equiv="refresh" content="15" >\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        bikes = context.get('bikes', UNDEFINED)
        range = context.get('range', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    \r\n\r\n    <div class="alert alert-success">\r\n        <p><strong>Compare local ads to their Kelly Blue Book value and find the best deals!</strong></p>\r\n    </div>\r\n\r\n    <div class="row">\r\n        <div class="col-md-12">\r\n\r\n    <div class="content">\r\n')
        if request.user.is_authenticated:
            __M_writer('            <table class="table table-striped table-bordered table-hover">\r\n                <caption style="caption-side: top">Click a row to be redirected to the item\'s ad</caption>\r\n                <thead class="thead-dark">\r\n                    <tr>\r\n                        <!-- <th>Year</th> -->\r\n                        <th>Make</th>\r\n                        <th>Model</th>\r\n                        <th>Price</th>\r\n                        <th>KBB</th>\r\n                        <th>Difference</th>\r\n                    </tr>\r\n                </thead>\r\n                <tbody>\r\n')
            for i in range (len(bikes)):  
                if bikes[i].difference < 0:
                    __M_writer('                            <tr class="table-success clickable-row" data-href=\'https://classifieds.ksl.com/listing/')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( bikes[i].ksl_id ))
                    __M_writer("'>\r\n")
                else:       
                    __M_writer("                            <tr class='clickable-row' data-href='https://classifieds.ksl.com/listing/")
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( bikes[i].ksl_id ))
                    __M_writer("'>\r\n")
                __M_writer('                            <!-- <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( bikes[i].year ))
                __M_writer('</td>                -->\r\n                            <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( bikes[i].make ))
                __M_writer('</td>\r\n                            <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( bikes[i].model ))
                __M_writer('</td>               \r\n                            <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( bikes[i].price ))
                __M_writer('</td>\r\n                            <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( bikes[i].kbb_value ))
                __M_writer('</td>               \r\n                            <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( bikes[i].difference ))
                __M_writer('</td>\r\n                        </tr>          \r\n')
            __M_writer('                </tbody>\r\n\r\n            </table>\r\n\r\n')
        else:
            __M_writer('            You must be logged in to view deals\r\n            <a class="btn btn-primary" href="/homepage/login/" role="button">Login</a>\r\n')
        __M_writer('\r\n    </div>\r\n\r\n</div>\r\n\r\n<!-- <div class="col-md-2">Hi</div> -->\r\n\r\n</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/scraper/homepage/templates/deals.html", "uri": "deals.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 63, "52": 4, "63": 4, "64": 16, "65": 17, "66": 30, "67": 31, "68": 32, "69": 32, "70": 32, "71": 33, "72": 34, "73": 34, "74": 34, "75": 36, "76": 36, "77": 36, "78": 37, "79": 37, "80": 38, "81": 38, "82": 39, "83": 39, "84": 40, "85": 40, "86": 41, "87": 41, "88": 44, "89": 48, "90": 49, "91": 52, "97": 91}}
__M_END_METADATA
"""
