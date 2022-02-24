from msilib.schema import Directory
from data_types import  contributor, project
import out_put


def solve_single_task_queue(input):
    contrib = input['contribs']
    pro = input['projects']

    directives = []

    project_order_by_due_date = sorted(pro, key=lambda x: x.get_due_date())

    for current_pro in project_order_by_due_date:
        current_assignments = [] # (contrib,skill)
        # get roles: list of tuple(skill,level)
        roles = current_pro.get_roles()#(skill,level)
        abadon_project = False
        for role in roles:
            role_skill,role_level = role
            currently_working = [p for p,skil in current_assignments]
            peoples_skills = [p for p in contrib if not p in currently_working and p.get_skill(role_skill)>=role_level]
            people_skill_order = sorted(peoples_skills, key=lambda x: x.get_skill(role_skill))
            if len(people_skill_order) == 0:
                abadon_project = True
                break
            else:
                current_assignments.append(people_skill_order[0],role_skill)
        if abadon_project:
            continue
        else:
            directives.append((current_pro,current_assignments))
    
    return directives







def main():
    directory = 'inputFiles/'
    test_cases = ['a_an_example.in.txt','b_better_start_small.in.txt','c_collaboration.in.txt','d_dense_schedule.in.txt','e_exceptional_skills.in.txt','f_find_great_mentors.in.txt']
    for test in test_cases:
        inputFile = input(directory+test)
        solution = solve_single_task_queue(inputFile)
        out_put.write(solution,"SUB-"+test)

if __name__ == '__main__':
    main()