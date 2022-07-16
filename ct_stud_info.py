
class Stud_info:
    def __init__(self,id,name,gen,dob,city):
        self.dict = {
            'id': id,
            'name': name,
            'gender': gen,
            'dob': dob,
            'city': city,
        }
    
    def add_grades(self,stud_grades):
        self.dict['grades'] = stud_grades.grades
        return self.dict

class Stud_grades:
    def __init__(self,**grades):
        self.grades = {
            'Mathematics': grades['Math'],
            'Physics': grades['Phy'],
            'Chemistry': grades['Chem'],
            'Total': grades['Total']
        }

class Stud_lst:
    def __init__(self):
        self.lst = []
    
    def add_stud(self, *students):
        for student in students:
            self.lst.append(student.dict)
        return self.lst
    
    def unique_cities(self):
        city_lst = []
        for ele in self.lst:
            if ele['city'] in city_lst:
                continue
            else:
                city_lst.append(ele['city'])
        return sorted(city_lst)

    def max_mark_cities(self):
        city_max_mark_dict = {}
        for ele in self.lst:
            if ele['city'] not in city_max_mark_dict.keys():
                city_max_mark_dict[ele['city']] = [ele['id'],ele['name'],int(ele['grades']['Total'])]
            
            elif int(ele['grades']['Total']) > city_max_mark_dict[ele['city']][-1]:
                city_max_mark_dict[ele['city']] = [ele['id'],ele['name'],int(ele['grades']['Total'])]
        return city_max_mark_dict

    def max_mark_city(self, *cities):
        all_cities_max_mark = self.max_mark_cities()
        max_mark_city_dict = {}
        for city in cities:
            if city not in all_cities_max_mark.keys():
                return "City not in dataset."
            max_mark_city_dict[city] = all_cities_max_mark[city]
        return max_mark_city_dict
                
    def max_mark(self, gender = None):
        max_mark = 0
        max_name = ''
        max_id = ''
        if gender == None:
            for ele in self.lst:
                if int(ele['grades']['Total']) > max_mark:
                    max_mark = int(ele['grades']['Total'])
                    max_name = ele['name']
                    max_id = ele['id']
            return {
            'id': max_id,
            'name': max_name,
            'Total': max_mark
            }
        if gender != None:
            for ele in self.lst:
                if int(ele['grades']['Total']) > max_mark and ele['gender'] == gender:
                    max_mark = int(ele['grades']['Total'])
                    max_name = ele['name']
                    max_id = ele['id']
            return {
            'id': max_id,
            'name': max_name,
            'Total': max_mark
            }

    def max_mark_subj(self,subj):
        max_subj = 0
        max_subj_tm = []
        max_subj_id = []
        max_subj_name = []
        for ele in self.lst:
            if int(ele['grades'][subj]) > max_subj:
                max_subj = int(ele['grades'][subj])
                max_subj_tm.clear()
                max_subj_tm.append(int(ele['grades']['Total']))
                max_subj_id.clear()
                max_subj_id.append(ele['id'])
                max_subj_name.clear()
                max_subj_name.append(ele['name'])
            elif int(ele['grades'][subj]) == max_subj:
                max_subj_tm.append(int(ele['grades']['Total']))
                max_subj_id.append(ele['id'])
                max_subj_name.append(ele['name'])
        return {
            'id': max_subj_id,
            'Name': max_subj_name,
            f'{subj} marks': max_subj,
            'Total marks': max_subj_tm,   
        }

    def avg_marks(self,subj = None):
        total_marks = 0
        if subj == None:
            for ele in self.lst:
                total_marks+= int(ele['grades']['Total'])
            return round(total_marks/len(self.lst))
        else:
            for ele in self.lst:
                total_marks+= int(ele['grades'][subj])
            return round(total_marks/len(self.lst))
    
    def no_of_stud_cities(self):
        no_dict = {}
        cities_lst = self.unique_cities()
        for city in cities_lst:
            no_dict[city] = 0
        for ele in self.lst:
            no_dict[ele['city']]+=1
        return no_dict