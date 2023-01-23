def get_post_info(name, post_qty):
    info = f"{name} read a book by {post_qty}"
    return info


info = get_post_info('I', 'Svyatoslav Kulikov')
print(info)


def get_post_info(**person):
    print(person)

    print(type(person))
    info = (
        f"{person['name']} wrote"
        f"{person['post_qty']} posts"
    )
    return info
