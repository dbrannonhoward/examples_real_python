name_for_userid = {
    382: "alice",
    590: "bob",
    951: "dilbert",
}


def greeting(userid):
    return 'hi %s' % name_for_userid.get(userid, 'there')


print(greeting(382))
print(greeting(9823489))

