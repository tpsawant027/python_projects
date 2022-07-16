import matplotlib.pyplot as plt
import csv
import ct_stud_info as ctsi
if __name__ == '__main__':

    stud_lst = ctsi.Stud_lst()

    with open('data.csv') as data:
        data_dict = csv.DictReader(data)
        for row in data_dict:
            stud = ctsi.Stud_info(row['id'],row['Name'],row['Gender'],row['dob'],row['City'])
            stud_grades = ctsi.Stud_grades(Math = row['Math'], Phy = row['Phy'], Chem = row['Chem'], Total = row['Total'] )
            stud.add_grades(stud_grades)
            stud_lst.add_stud(stud)
    
    above_avg = []
    below_avg = []
    avg_marks = stud_lst.avg_marks()
    for ele in stud_lst.lst:
        if int(ele['grades']['Total']) >= avg_marks:
            above_avg.append([ele['id'], ele['name']])
        else:
            below_avg.append([ele['id'], ele['name']])
    id_stud = []
    total_marks_stud = []
    for ele in stud_lst.lst:
        id_stud.append(ele['id'])
        total_marks_stud.append(int(ele['grades']['Total']))

    # plt.figure(1)
    # plt.axhline(y = avg_marks)
    # plt.scatter(id_stud,total_marks_stud, c = "green")
    # plt.figure(2)
    # plt.axhline(y = avg_marks)
    # plt.plot(id_stud,total_marks_stud, c = "green")
    # plt.figure(3)
    # plt.axhline(y = avg_marks)
    # plt.bar(id_stud,total_marks_stud)
    # plt.show()

    # print(above_avg)
    # print("\n")
    # print(below_avg)



    # print(stud_lst.max_mark())
    # print(stud_lst.max_mark('F'))
    # print(stud_lst.unique_cities())
    # print(stud_lst.max_mark_cities())
    # print(stud_lst.max_mark_city('Bengaluru','Chennai'))
    # print("\n")
    # print(stud_lst.max_mark_subj('Mathematics'))
    # print(stud_lst.max_mark_subj('Physics'))
    # print(stud_lst.max_mark_subj('Chemistry'))
    # print("\n")
    # print(stud_lst.avg_marks())
    # print(stud_lst.avg_marks('Mathematics'))
    # print(stud_lst.avg_marks('Physics'))
    # print(stud_lst.avg_marks('Chemistry'))
    print(stud_lst.no_of_stud_cities())