import ckan.model as model

def get_sysadmins():
    q = model.Session.query(model.User).filter(
        model.User.state == u'active'
    )
    return q.all()  
