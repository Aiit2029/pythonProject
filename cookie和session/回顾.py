#   cookie

# 为了解决http协议无状态  为了维持会话，浏览器推出了cookie技术
    # 因为 客户端和 服务器 在会话中会产生数据， 而这产生的数据 有的是我们需要保存的 ，
    # 而无状态 导致 这些数据不会被保留，因此 cookie 技术应运而生

#  那么什么是 http协议 无状态
    # http协议 是 无连接 无状态的
    # 无连接 ： 又称 短连接

    # 无状态： 服务器在处理请求时 不会保存之前请求的任何信息
    #        每次请求对于服务器来说都是新的 独立的 服务器不会根据
    #        之前的请求来处理当前的请求

#  那么什么是cookie呢 ？
    # cookie 是浏览器的技术 ，当你 通过浏览器访问服务器时，服务器会给浏览器一个 身份令牌 ，
    # 浏览器会在本地保存这个 小令牌(是服务器产生的 键值对)
    # 当你再一次访问服务器时 浏览器会自动携带这个小令牌 而服务器通过这个小令牌来得知 你的信息

#  为什么 有的网站在同一个浏览器中 登录 第二个用户 ，第一个用户就不能使用了 ？
    # 因为 客户端第二次发送的cookie 会覆盖上一个第一个用户的cookie，你看到的部分原用户内容
    # 是本地缓存的上一个用户的内容， 当你刷新页面 会重新展示 当前用户的内容

# django 操作 cookie
    # request.COOKIES['is_login'] = 1
    # request.get['is_login']
    # request.get_signed_cooki()


    # 设置cookie

    # ret = render(request,'/login/')
    # ret.set_cookie('is_login',True,max_age=3600)
    # max_age  超时时间  单位是秒
    # expires  超时时间  格式为 datetime


    # 删除 cookie

    # ret.delete_cookie('is_login')


# session

# 什么是session？
    # session 是服务器端的技术 ，用户在访问服务器时
    # 服务器可以给每一个用户的浏览器 创建一个 独立的session对象
    # 所以用户在访问服务器的 资源时 可以把各自的数据放在 自己的session中
    # 当用户 再去访问该服务器 其他的网页资源的时候 可以从 这个用户的session中
    # 取出对应的数据  非常的便捷
    # 比如 用户登录 ， 当你登录进入 bilibili 时 在登陆界面登录 ，在哔哩哔哩所属的基本所有界面 都不必在多次登录
    # 因为  当前用户的数据在当前浏览器中的session中可以随时取用，略过登陆阶段

# 有了cookie 为什么还要用 session
    # 因为 cookie 虽然一定程度上解决了 无状态的麻烦
    # 但是因为cookie 本身最大支持4096字节 并且 cookie 本身保存在客户端
    # 可能被拦截或者窃取 ，相对来说不安全 ，因此 session 应运而生

    # session 给不同客户端的cookie 分配了 一个 id
    # 这样用户访问时服务器可以通过id 来分辨 用户
    # 而 session_id  可以通过 global_setting 中的 session_id
    # 重写在 自己的 settiing中 来修改 对应的 name


# django 操作 session
    # 默认 session 的 键值对和 id  存放在
    # django-session 表中
    # request.session['is_login'] =  True
    # request.session.get['is_login']
    # 当使用删除session时 ，django-session表中的数据也同步删除
    # del request.session['is_login']

    # 获取session 的 id
    # session_key = request.session.session_key

    # 删除过期session
    # request.session.clear_expired()

    # 检查对应的key 是否存在
    # request.session.exists('session_key')

    # CSRF Token相关装饰器在CBV只能加到dispatch方法上，或者加在视图类上然后name参数指定为dispatch方法。

    # 备注：

    # csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件。

    # csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。








