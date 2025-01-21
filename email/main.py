import os
with open("names/names.txt", "r") as file:
    names = file.readlines()

names = [name.strip() for name in names]

with open("email/email.txt", "r") as file:
    emailtemplate = file.read()

for name in names:
    pesonalizedemail = emailtemplate.replace("[name]", name)
    email_file_path = os.path.join("send", f"{name}.txt")

    with open(email_file_path, "w") as output_file:
        output_file.write(pesonalizedemail)




