def create_profile(**kwargs):
    profile = {"name": kwargs.get("name", "Unknown"), "age": kwargs.get("age", "Unknown"), "location": kwargs.get("location", "Unknown")}
    for x, y in profile.items():
        print(f"{x}: {y}")
    return profile

create_profile(name="Kesh", age="24", location="Birmingham")

create_profile(name="Kesh", age="24")
