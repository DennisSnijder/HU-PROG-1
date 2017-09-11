def new_password(oldpassword: str, newpassword: str) -> bool:
    if oldpassword != newpassword and len(newpassword) > 6:
        return True

    return False

print(new_password('my-old-password', 'my-new-password'))
print(new_password('my-old-password', 'my-old-password'))