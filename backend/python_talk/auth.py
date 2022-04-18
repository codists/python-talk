def register():
    """
    用户注册
    :return: json
    """
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    user = Users(email=email, username=username, password=Users.set_password(Users, password))
    result = Users.add(Users, user)
    if user.id:
        returnUser = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'login_time': user.login_time
        }
        return jsonify(common.trueReturn(returnUser, "用户注册成功"))
    else:
        return jsonify(common.falseReturn('', '用户注册失败'))