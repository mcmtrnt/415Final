# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555804915.0499606
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
        range = context.get('range', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        len = context.get('len', UNDEFINED)
        deals = context.get('deals', UNDEFINED)
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
        range = context.get('range', UNDEFINED)
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        len = context.get('len', UNDEFINED)
        deals = context.get('deals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    \r\n\r\n    <div class="alert alert-success">\r\n        <p><strong>Compare local ads to their Kelly Blue Book value and find the best deals!</strong></p>\r\n    </div>\r\n\r\n    <div class="row">\r\n        <div class="col-md-12">\r\n\r\n    <div class="content">\r\n\r\n            <table class="table table-striped table-bordered table-hover">\r\n                <caption style="caption-side: top">Click a row to be redirected to the item\'s ad</caption>\r\n                <thead class="thead-dark">\r\n                    <tr>\r\n                        <th>Year</th>\r\n                        <th>Make</th>\r\n                        <th>Model</th>\r\n                        <th>Price</th>\r\n                        <th>KBB</th>\r\n                        <th>Difference</th>\r\n                    </tr>\r\n                </thead>\r\n                <tbody>\r\n')
        for i in range (len(deals)):  
            if deals[i].difference < 0:
                __M_writer('                            <tr class="table-success clickable-row" data-href=\'https://classifieds.ksl.com/listing/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].ksl_id ))
                __M_writer("'>\r\n")
            else:       
                __M_writer("                            <tr class='clickable-row' data-href='https://classifieds.ksl.com/listing/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].ksl_id ))
                __M_writer("'>\r\n")
            __M_writer('                            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].year ))
            __M_writer('</td>               \r\n                            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].make ))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].model ))
            __M_writer('</td>               \r\n                            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].price ))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].kbb_value ))
            __M_writer('</td>               \r\n                            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( deals[i].difference ))
            __M_writer('</td>\r\n                        </tr>          \r\n')
        __M_writer('                </tbody>\r\n\r\n            </table>\r\n\r\n\r\n\r\n    </div>\r\n\r\n</div>\r\n\r\n<!-- <div class="col-md-2">Hi</div> -->\r\n\r\n</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/scraper/homepage/templates/deals.html", "uri": "deals.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 60, "51": 4, "61": 4, "62": 30, "63": 31, "64": 32, "65": 32, "66": 32, "67": 33, "68": 34, "69": 34, "70": 34, "71": 36, "72": 36, "73": 36, "74": 37, "75": 37, "76": 38, "77": 38, "78": 39, "79": 39, "80": 40, "81": 40, "82": 41, "83": 41, "84": 44, "90": 84}}
__M_END_METADATA
"""
