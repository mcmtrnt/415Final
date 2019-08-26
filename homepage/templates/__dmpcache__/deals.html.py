# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1560556870.1933374
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
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        deals = context.get('deals', UNDEFINED)
        request = context.get('request', UNDEFINED)
        range = context.get('range', UNDEFINED)
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
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        deals = context.get('deals', UNDEFINED)
        request = context.get('request', UNDEFINED)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    \r\n\r\n    <div class="alert alert-success">\r\n        <p><strong>Compare local ads to their Kelly Blue Book value and find the best deals!</strong></p>\r\n    </div>\r\n\r\n    <div class="row">\r\n        <div class="col-md-12">\r\n\r\n    <div class="content">\r\n        \r\n        <table class="table table-striped table-bordered table-hover">\r\n            <caption style="caption-side: top">Click a row to be redirected to the item\'s ad</caption>\r\n            <thead class="thead-dark">\r\n                <tr>\r\n                    <th>Location</th>\r\n                    <th>Year</th>\r\n                    <th>Make</th>\r\n                    <th>Model</th>\r\n                    <th>Price</th>\r\n                    <th>KBB</th>\r\n                    <th>Difference</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        for i in range (len(deals)):  
            if deals[i].difference < 0:
                if request.user.has_perm('homepage.view_ad'):
                    __M_writer('                            <tr class="table-success clickable-row" data-href=\'https://classifieds.ksl.com/listing/')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].ksl_id ))
                    __M_writer("'>\r\n")
                else:
                    __M_writer("                            <tr class='clickable-row' data-href='https://classifieds.ksl.com/listing/")
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].ksl_id ))
                    __M_writer("'>\r\n")
            else:       
                __M_writer("                        <tr class='clickable-row' data-href='https://classifieds.ksl.com/listing/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].ksl_id ))
                __M_writer("'>\r\n")
            if request.user.has_perm('homepage.view_ad'):    
                __M_writer('                        <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(deals[i].city))
                __M_writer('</td>                                          \r\n                        <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].year ))
                __M_writer('</td>     \r\n')
            else:
                __M_writer('                        <td>X</td>\r\n                        <td>X</td>\r\n')
            __M_writer('                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].make ))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].model ))
            __M_writer('</td>               \r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].price ))
            __M_writer('</td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].kbb_value ))
            __M_writer('.00</td>   \r\n')
            if request.user.has_perm('homepage.view_ad'):            
                __M_writer('                        <td>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].difference ))
                __M_writer('</td>\r\n')
            else:
                __M_writer('                        <td>X</td>\r\n')
            __M_writer('                    </tr>          \r\n')
        __M_writer('            </tbody>\r\n\r\n        </table>\r\n\r\n    </div>\r\n\r\n</div>\r\n\r\n</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/scraper/homepage/templates/deals.html", "uri": "deals.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 71, "52": 4, "63": 4, "64": 31, "65": 32, "66": 33, "67": 34, "68": 34, "69": 34, "70": 35, "71": 36, "72": 36, "73": 36, "74": 38, "75": 39, "76": 39, "77": 39, "78": 41, "79": 42, "80": 42, "81": 42, "82": 43, "83": 43, "84": 44, "85": 45, "86": 48, "87": 48, "88": 48, "89": 49, "90": 49, "91": 50, "92": 50, "93": 51, "94": 51, "95": 52, "96": 53, "97": 53, "98": 53, "99": 54, "100": 55, "101": 57, "102": 59, "108": 102}}
__M_END_METADATA
"""
