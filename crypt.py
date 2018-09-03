# -*- coding:utf-8 -*-
text = {
        'username': username,
        'password': password,
        'rememberLogin': 'true'
    }
    text = json.dumps(text)
    secKey = createSecretKey(16)
    encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
    data = {
        'params': encText,
        'encSecKey': encSecKey
    }

