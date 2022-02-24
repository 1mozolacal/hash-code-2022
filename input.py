import os

class Skill:
    def __init__(self, name, level) -> None:
        self.name = name
        self.level = level
        

class Contributor:
    def __init__(self, name : str = '', skill_num:str = '', skill: list = []) -> None:
        self.name = name
        self.skill_num = skill_num
        self.skill = skill
        self.workingDays = []
    
    
    

class Project:
    """
    an integer Di (1 ≤ Di ≤ 105) – the number of days it takes to complete the project,
    an integer Si (1 ≤ Si ≤ 105) – the score awarded for project’s completion,
    an integer Bi (1 ≤ Bi ≤ 105) – the “best before” day for the project,
    an integer Ri (1 ≤ Ri ≤ 100) – the number of roles in the project.
    """
    def __init__(self, name: str, estimation: int, score: int, best_before: int, role_count: int, roles: list ) -> None:
        self.name = name
        self.estimation = estimation
        self.score = score
        self.best_before = best_before
        self.role_count = role_count
        self.roles = roles
        

def file_loader(file_name: str):
    with open(file_name) as f:
        lines = f.readlines()
    
    first_line = lines[0].removesuffix('\n').split(" ")
    contribs_num = int(first_line[0])
    proj_num = first_line[1]

    contribs = []
    # Get contribs
    contrib_skill_count = 0
    current_person = Contributor()
    
    # Get proj
    current_project = Project()
    project_count = 0

    for line in lines[1:]:
        data = line.removesuffix('\n').split(" ")
        if contribs_num - 1 >= len(contribs):
            if contrib_skill_count == 0:

                current_person.name = data[0]
                current_person.skill_num = data[1]
                contrib_skill_count = int(data[1])

            elif contrib_skill_count != 0:
                current_person.skill.append(Skill(data[0], data[1]))
                contrib_skill_count -= 1
                if contrib_skill_count == 0:
                    contribs.append(current_person)
                    current_person = Contributor()
        else:
            if project_count == 0:
                current_project.name = data[0]
                current_project.estimation = data[1]
                current_project.score = data[2]
                current_project.best_before = data[3]
                current_project.role_count = data[4]
            

    
    print(contribs)

    for contrib in contribs:
        print(contrib.name)
        print(contrib.skill_num)
        print(contrib.skill)


    

file_loader('inputFiles/a_an_example.in.txt')