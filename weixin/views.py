#coding:utf-8

from django.shortcuts import render



# Create your views here.



from django.views.decorators.csrf import csrf_exempt


from wechat_sdk import WechatBasic

from wechat_sdk.exceptions import ParseError

from wechat_sdk.messages import TextMessage

from wechat_sdk import WechatConf





from django.http import HttpResponse,HttpResponseRedirect,HttpResponseBadRequest




conf = WechatConf(

    token='71451085a',

    appid='wx65a275d3c1a71d29',

    appsecret='c1e1656bd05b52a4f0858f72b6ef69fa',

    encrypt_mode='normal',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式

    encoding_aes_key='PlrRDX372PXe2b5ORxE0sKMZjY1fqahqQRKmjSksDcb'  # 如果传入此值则必须保证同时传入 token, appid

)

wechat = WechatBasic(conf=conf)


@csrf_exempt

def weixin(request):

    if request.method=="GET":

        signature=request.GET['signature']

        timestamp=request.GET['timestamp']

        echostr=request.GET['echostr']

        nonce=request.GET['nonce']

        if wechat.check_signature(signature, timestamp, nonce):

            return HttpResponse(echostr)

        else:

            return HttpResponse(False)

    else:
        try:
            wechat.parse_data(data=request.body)
        except ParseError:

            return HttpResponseBadRequest('Invalid XML Data')

        message = wechat.get_message()

        response = wechat.response_text(content="感谢您的关注！\n回复【功能】两个字查看支持的功能\n更多功能正在开发")

        if isinstance(message,TextMessage):
            content=message.content
            xml=wechat.response_text(content=content)
            return HttpResponse(xml, content_type="application/xml")
        else:
            return HttpResponse(response, content_type="application/xml")

