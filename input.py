import data_types

def file_loader(file_name: str) -> dict:
    with open(file_name) as f:
        lines = f.readlines()
    
    first_line = lines[0].removesuffix('\n').split(" ")
    contribs_num = int(first_line[0])
    proj_num = int(first_line[1])

    contribs = []
    # Get contribs
    contrib_skill_count = 0
    sk = []
    current_person = data_types.contributor()
    
    # Get proj
    current_project = data_types.project()
    project_count = 0
    projects = []
    pr = []

    for line in lines[1:]:
        data = line.removesuffix('\n').split(" ")
        if contribs_num - 1 >= len(contribs):
            if contrib_skill_count == 0:
                current_person.name = data[0]
                contrib_skill_count = int(data[1])

            else:
                sk.append(data_types.skill(data[0], data[1]))
                contrib_skill_count -= 1
                if contrib_skill_count == 0:
                    current_person.skills = sk
                    sk = []
                    contribs.append(current_person)
                    current_person = data_types.contributor()
        elif proj_num >= len(projects):
            if project_count == 0:
                current_project.name = data[0]
                current_project.project_length = int(data[1])
                current_project.score = int(data[2])
                current_project.due_date = int(data[3])
                project_count = int(data[4])
            else:
                pr.append(data_types.skill(data[0], data[1]))
                project_count -= 1
                if project_count == 0:
                    current_project.roles = pr
                    pr = []
                    projects.append(current_project)
                    current_project = data_types.project()
    return {"projects": projects, "contribs": contribs}
    
if __name__ == '__main__':
    file_loader('inputFiles/a_an_example.in.txt')