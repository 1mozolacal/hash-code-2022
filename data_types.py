class skill():
    def __init__(self, name, level):
        self.name = name
        self.level = level


class contributor():
    def __init__(self, name : str = '', skills: list = []):
        self.name = name
        self.skills = skills

    def get_skill(self, skill_name):
        if not skill_name in self.skills:
            return 0
        return self.skills[skill_name]

    def improve_skill(self, skill_name):
        if skill_name in self.skills:
            self.skills[skill_name] += 1
        else:
            self.skills[skill_name] = 1

    def canWorkOnProject(self, name, level):
        for skill in self.skills:
            if name in skill:
                return level > skill[1]
        return False


class project():
    # estimation = project_length
    # due_date = best_before
    def __init__(self, name : str = '', roles: list = [], project_length: int = 0,  score: int = 0, due_date : int = 0):
        self.name = name
        temp_roles = {}
        for skill, level in roles:
            temp_roles[skill] = level
        self.roles = temp_roles
        self.roles_ordering = [skill for skill, level in roles]
        self.project_length = project_length
        self.score = score
        self.due_date = due_date

    def assign(self, assignments):
        place_holder = [None] * len(assignments)
        for skill, person in assignments:
            place_holder[self.roles_ordering.index(skill)] = person
        return place_holder

    def getDueDate(self):
        return self.due_date

    def getProjectLength(self):
        return self.project_length

    def getScore(self):
        return self.score

    def getRoles(self):
        return self.roles_orderng
