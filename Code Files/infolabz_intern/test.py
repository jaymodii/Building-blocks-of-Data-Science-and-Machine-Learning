class FunEvent:
    def __init__(self, tags, year):
        self.tags = tags
        self.year = year

    def __str__(self):
        return f"FunEvent(tags={self.tags}, year={self.year})"


tags = ["google", "ml"]
year = "abc"
print(id(tags))
# print(id(year))
bootcamp = FunEvent(tags, year)
tags=["bootcamp"]
print(id(tags))
# print(id(year))
print(bootcamp)