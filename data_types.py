

class contributor():
    def __init__(self, name,skills):
        self.name = name
        self.skills = skills

    def get_skill(self,skill_name):
        if not skill_name in self.skills:
            return 0
        return self.skills[skill_name]

    def improve_skill(self,skill_name):
        if skill_name in self.skills:
            self.skills[skill_name] +=1
        else:
            self.skills[skill_name] = 1

    def canWorkOnProject(self,skillName,skillLevel):
        for skill in self.skills:
            if skillName in skill:
                return skillLevel>skill[1]
        return False


class project():
    def __init__(self, name,roles,project_length,score,due_date):
        self.name = name
        temp_roles = {}
        for skill, level in roles:
            temp_roles[skill] = level
        self.roles = temp_roles
        self.roles_ordering = [skill for skill,level in roles]
        self.project_length = project_length
        self.score = score
        self.due_date = due_date

    def assign(self,assignments):
        place_holder = [None] * len(assignments)
        for skill,person in assignments:
            place_holder[self.roles_ordering.index(skill)] = person
        return place_holder

    def getDueDate(self):
        return self.due_date
    def getProjectLength(self):
        return self.project_length
    def getScore(self):
        return self.score
    