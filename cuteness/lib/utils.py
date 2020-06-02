def getParam(name, kwargs):
    hasparam = name in kwargs
    param = kwargs.get(name)
    return hasparam, param
