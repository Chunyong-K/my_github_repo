import tkinter as tk
from performance_grade_classifier import *


class PG_GUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("Performance Grade Classifier")

        # Create two frames to group widgets.
        self.frame_1 = tk.Frame()
        self.frame_2 = tk.Frame()
        self.frame_3 = tk.Frame()
        self.frame_4 = tk.Frame()
        self.frame_5 = tk.Frame()
        self.frame_6 = tk.Frame()
        self.frame_7 = tk.Frame()
        self.frame_8 = tk.Frame()
        self.frame_9 = tk.Frame()
        self.frame_10 = tk.Frame()
        self.frame_11 = tk.Frame()
        self.frame_12 = tk.Frame()
        self.frame_13 = tk.Frame()

        # Create the widgets for frame one. (title display)
        self.title_label = tk.Label(self.frame_1, text='PERFORMANCE GRADE CLASSIFIER', fg="Green",
                                    font=("Helvetica", 18))
        self.title_label.pack()


        # Create the widgets for frame two.
        self.age_label = tk.Label(self.frame_2, text='age:')
        self.click_age_var = tk.StringVar()
        self.click_age_var.set("18-21")
        self.age_inp = tk.OptionMenu(self.frame_2,self.click_age_var, "18-21", "22-25", 'above 26')
        self.age_label.pack(side='left')
        self.age_inp.pack(side='left')


        # Create the widgets for frame three.
        self.sex_label = tk.Label(self.frame_2, text='sex:')
        self.click_sex_var = tk.StringVar()
        self.click_sex_var.set("Male")
        self.sex_inp = tk.OptionMenu(self.frame_2,self.click_sex_var, "Male", "Female")
        self.sex_label.pack(side='left')
        self.sex_inp.pack(side='left')

        # Create the widgets for frame four.
        self.grad_label = tk.Label(self.frame_2, text='Graduated high-school type:')
        self.click_grad_var = tk.StringVar()
        self.click_grad_var.set("private")
        self.grad_inp = tk.OptionMenu(self.frame_2, self.click_grad_var, "private", "state", 'other')
        self.grad_label.pack(side='left')
        self.grad_inp.pack(side='left')

        # Create the widgets for frame five.
        self.scholar_label = tk.Label(self.frame_3, text='Scholarship type:')
        self.click_scholar_var = tk.StringVar()
        self.click_scholar_var.set("Please select")
        self.scholar_inp = tk.OptionMenu(self.frame_3, self.click_scholar_var, "None", "25%", '50%', '75%', 'Full')
        self.scholar_label.pack(side='left')
        self.scholar_inp.pack(side='left')

        # Create the widgets for frame three.
        self.work_label = tk.Label(self.frame_3, text='Additional work (Y/N):')
        self.work_entry = tk.Entry(self.frame_3, bg="white", fg="black")
        self.work_label.pack(side='left')
        self.work_entry.pack(side='left')

        self.activity_label = tk.Label(self.frame_3, text='Regular artistic or sports activity (Y/N):')
        self.activity_entry = tk.Entry(self.frame_3, bg="white", fg="black")
        self.activity_label.pack(side='left')
        self.activity_entry.pack(side='left')

        # Create the widgets for frame three.
        self.partner_label = tk.Label(self.frame_4, text='Do you have a partner (Y/N):')
        self.partner_entry = tk.Entry(self.frame_4, bg="white", fg="black")
        self.partner_label.pack(side='left')
        self.partner_entry.pack(side='left')

        # Create the widgets for frame four.
        self.salary_label = tk.Label(self.frame_4, text='Total salary if available:')
        self.click_salary_var = tk.StringVar()
        self.click_salary_var.set("Please select")
        self.salary_inp = tk.OptionMenu(self.frame_4, self.click_salary_var, "USD 135-200", "USD 201-270",'USD 271-340',
                                        'USD 341-410', 'above 410')
        self.salary_label.pack(side='left')
        self.salary_inp.pack(side='left')

        # Create the widgets for frame four.
        self.transport_label = tk.Label(self.frame_4, text='Transportation to the university:')
        self.click_transport_var = tk.StringVar()
        self.click_transport_var.set("Please select")
        self.transport_inp = tk.OptionMenu(self.frame_4, self.click_transport_var, "Bus", 'Private car/taxi', 'Bicycle',
                                           'Other')
        self.transport_label.pack(side='left')
        self.transport_inp.pack(side='left')

        # Create the widgets for two frame.
        self.acco_label = tk.Label(self.frame_5, text='Accommodation type in Cyprus:')
        self.click_acco_var = tk.StringVar()
        self.click_acco_var.set("Please select")
        self.acco_inp = tk.OptionMenu(self.frame_5, self.click_acco_var, "rental", "dormitory", 'with family', 'Other')
        self.acco_label.pack(side='left')
        self.acco_inp.pack(side='left')

        # Create the widgets for two frame.
        self.mother_label = tk.Label(self.frame_5, text="Mother's education:")
        self.click_mother_var = tk.StringVar()
        self.click_mother_var.set("Please select")
        self.mother_inp = tk.OptionMenu(self.frame_5, self.click_mother_var, "primary school", "secondary school",
                                        'high school','university','MSc','Ph.D.')
        self.mother_label.pack(side='left')
        self.mother_inp.pack(side='left')

        # Create the widgets for two frame.
        self.father_label = tk.Label(self.frame_5, text="Father's education:")
        self.click_father_var = tk.StringVar()
        self.click_father_var.set("Please select")
        self.father_inp = tk.OptionMenu(self.frame_5, self.click_father_var, "primary school", "secondary school",
                                        'high school','university','MSc','Ph.D.')
        self.father_label.pack(side='left')
        self.father_inp.pack(side='left')

        self.sibling_label = tk.Label(self.frame_6, text="Number of sisters/brothers (if available):")
        self.click_sibling_var = tk.StringVar()
        self.click_sibling_var.set("Please select")
        self.sibling_inp = tk.OptionMenu(self.frame_6, self.click_sibling_var, "1", "2", '3', '4', '5 or above')
        self.sibling_label.pack(side='left')
        self.sibling_inp.pack(side='left')

        self.parental_status_label = tk.Label(self.frame_6, text="Parental status:")
        self.click_parental_status_var = tk.StringVar()
        self.click_parental_status_var.set("Please select")
        self.parental_status_inp = tk.OptionMenu(self.frame_6, self.click_parental_status_var, "married", "divorced",
                                                 'died - one of them or both')
        self.parental_status_label.pack(side='left')
        self.parental_status_inp.pack(side='left')

        self.mother_occup_label = tk.Label(self.frame_6, text="Mother's occupation:")
        self.click_mother_occup_var = tk.StringVar()
        self.click_mother_occup_var.set("Please select")
        self.mother_occup_inp = tk.OptionMenu(self.frame_6, self.click_mother_occup_var, "retired", "housewife",
                                              'government officer','private sector employee','self-employment','Other')
        self.mother_occup_label.pack(side='left')
        self.mother_occup_inp.pack(side='left')

        self.father_occup_label = tk.Label(self.frame_7, text="Father's occupation:")
        self.click_father_occup_var = tk.StringVar()
        self.click_father_occup_var.set("Please select")
        self.father_occup_inp = tk.OptionMenu(self.frame_7, self.click_father_occup_var, "retired",'government officer',
                                      'private sector employee', 'self-employment', 'Other')
        self.father_occup_label.pack(side='left')
        self.father_occup_inp.pack(side='left')

        self.study_hour_label = tk.Label(self.frame_7, text="Weekly study hours:")
        self.click_study_hour_var = tk.StringVar()
        self.click_study_hour_var.set("Please select")
        self.study_hour_inp = tk.OptionMenu(self.frame_7, self.click_study_hour_var, "None", '<5 hours',
                                      '6-10 hours', '11-20 hours', 'more than 20 hours')
        self.study_hour_label.pack(side='left')
        self.study_hour_inp.pack(side='left')

        self.non_sci_read_label = tk.Label(self.frame_7, text="Reading frequency(non-scientific books/journals):")
        self.click_non_sci_read_var = tk.StringVar()
        self.click_non_sci_read_var.set("Please select")
        self.non_sci_read_inp = tk.OptionMenu(self.frame_7, self.click_non_sci_read_var, "None", 'Sometimes', 'often')
        self.non_sci_read_label.pack(side='left')
        self.non_sci_read_inp.pack(side='left')

        self.sci_read_label = tk.Label(self.frame_8, text="Reading frequency(scientific books/journals):")
        self.click_sci_read_var = tk.StringVar()
        self.click_sci_read_var.set("Please select")
        self.sci_read_inp = tk.OptionMenu(self.frame_8, self.click_sci_read_var, "None", 'Sometimes', 'often')
        self.sci_read_label.pack(side='left')
        self.sci_read_inp.pack(side='left')

        self.seminar_attendance_label = tk.Label(self.frame_8, text='Attendance to the seminars/conferences related to '
                                                                    'the department (Y/N):')
        self.seminar_attendance_entry = tk.Entry(self.frame_8, bg="white", fg="black")
        self.seminar_attendance_label.pack(side='left')
        self.seminar_attendance_entry.pack(side='left')

        self.project_impact_label = tk.Label(self.frame_8, text="Impact of your projects/activities on your success:")
        self.click_project_impact_var = tk.StringVar()
        self.click_project_impact_var.set("Please select")
        self.project_impact_inp = tk.OptionMenu(self.frame_8, self.click_project_impact_var, "Positive", 'Negative',
                                                'Neutral')
        self.project_impact_label.pack(side='left')
        self.project_impact_inp.pack(side='left')

        self.class_attendance_label = tk.Label(self.frame_9, text="Attendance to classes:")
        self.click_class_attendance_var = tk.StringVar()
        self.click_class_attendance_var.set("Please select")
        self.class_attendance_inp = tk.OptionMenu(self.frame_9, self.click_class_attendance_var, "Always", 'Sometimes',
                                                  'Never')
        self.class_attendance_label.pack(side='left')
        self.class_attendance_inp.pack(side='left')

        self.preparation_one_label = tk.Label(self.frame_9, text="Preparation to midterm exams 1:")
        self.click_preparation_one_var = tk.StringVar()
        self.click_preparation_one_var.set("Please select")
        self.preparation_one_inp = tk.OptionMenu(self.frame_9, self.click_preparation_one_var, "Alone", 'With friends',
                                                 'Not applicable')
        self.preparation_one_label.pack(side='left')
        self.preparation_one_inp.pack(side='left')

        self.preparation_two_label = tk.Label(self.frame_9, text="Preparation to midterm exams 2:")
        self.click_preparation_two_var = tk.StringVar()
        self.click_preparation_two_var.set("Please select")
        self.preparation_two_inp = tk.OptionMenu(self.frame_9, self.click_preparation_two_var,"closest date to the exam"
                                                 , 'regularly during the semester', 'Never')
        self.preparation_two_label.pack(side='left')
        self.preparation_two_inp.pack(side='left')

        self.take_note_label = tk.Label(self.frame_10, text="Taking notes in classes:")
        self.click_take_note_var = tk.StringVar()
        self.click_take_note_var.set("Please select")
        self.take_note_inp = tk.OptionMenu(self.frame_10, self.click_take_note_var, "Never", 'Sometimes', 'Always')
        self.take_note_label.pack(side='left')
        self.take_note_inp.pack(side='left')

        self.listening_label = tk.Label(self.frame_10, text="Listening in classes:")
        self.click_listening_var = tk.StringVar()
        self.click_listening_var.set("Please select")
        self.listening_inp = tk.OptionMenu(self.frame_10, self.click_listening_var, "Never", 'Sometimes', 'Always')
        self.listening_label.pack(side='left')
        self.listening_inp.pack(side='left')

        self.discussion_label = tk.Label(self.frame_10, text="Discussion improves interest and success in the course:")
        self.click_discussion_var = tk.StringVar()
        self.click_discussion_var.set("Please select")
        self.discussion_inp = tk.OptionMenu(self.frame_10, self.click_discussion_var, "Never", 'Sometimes', 'Always')
        self.discussion_label.pack(side='left')
        self.discussion_inp.pack(side='left')

        self.flip_classroom_label = tk.Label(self.frame_11, text="Flip-classroom:")
        self.click_flip_classroom_var = tk.StringVar()
        self.click_flip_classroom_var.set("Please select")
        self.flip_classroom_inp = tk.OptionMenu(self.frame_11, self.click_flip_classroom_var, "Not useful", 'Useful',
                                                'Not applicable')
        self.flip_classroom_label.pack(side='left')
        self.flip_classroom_inp.pack(side='left')

        self.cum_grade_label = tk.Label(self.frame_11, text="Cumulative grade point average in the last semester:")
        self.click_cum_grade_var = tk.StringVar()
        self.click_cum_grade_var.set("Please select")
        self.cum_grade_inp = tk.OptionMenu(self.frame_11, self.click_cum_grade_var, "<2.00", '2.00-2.49', '2.50-2.99',
                                           '3.00-3.49','above 3.49')
        self.cum_grade_label.pack(side='left')
        self.cum_grade_inp.pack(side='left')

        self.exp_grade_label = tk.Label(self.frame_11,text="Expected Cumulative grade point average in the graduation:")
        self.click_exp_grade_var = tk.StringVar()
        self.click_exp_grade_var.set("Please select")
        self.exp_grade_inp = tk.OptionMenu(self.frame_11, self.click_exp_grade_var, "<2.00", '2.00-2.49', '2.50-2.99',
                                      '3.00-3.49', 'above 3.49')
        self.exp_grade_label.pack(side='left')
        self.exp_grade_inp.pack(side='left')

        self.course_id_label = tk.Label(self.frame_12, text="Course ID: ")
        self.click_course_id_var = tk.StringVar()
        self.click_course_id_var.set("Please select")
        self.course_id_inp = tk.OptionMenu(self.frame_12, self.click_course_id_var, "1", '2', '3', '4', '5', '6', '7',
                                           '8', '9')
        self.course_id_label.pack(side='left')
        self.course_id_inp.pack(side='left')

        #Create the widgets for fifteen frame = hd (prediction of heart disease)
        #self.pg_classify_ta = tk.Text(self.frame_13,height = 20, width = 50,bg= 'light blue')

        #Create predict button and quit button
        self.btn_classify = tk.Button(self.frame_12, text='Classify performance grade', command=self.classify_pg)
        self.btn_quit = tk.Button(self.frame_12, text='Quit', command=self.main_window.destroy)

        # Create the widgets for fifteen frame = hd (prediction of heart disease)
        self.pg_classify_ta = tk.Text(self.frame_13, height=20, width=80, bg='light blue')

        self.pg_classify_ta.pack()
        self.btn_classify.pack(side='left')
        self.btn_quit.pack()

        # Pack the frames.
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        self.frame_6.pack()
        self.frame_7.pack()
        self.frame_8.pack()
        self.frame_9.pack()
        self.frame_10.pack()
        self.frame_11.pack()
        self.frame_12.pack()
        self.frame_13.pack()
        # Enter the tkinter main loop.
        tk.mainloop()

    def classify_pg(self):
        result_string = ""

        self.pg_classify_ta.delete(0.0, tk.END)
        age = self.click_age_var.get()
        sex= self.click_sex_var.get()
        graduated_h_school_type = self.click_grad_var.get()
        scholarship_type = self.click_scholar_var.get()
        additional_work = self.work_entry.get()
        additional_work = additional_work.upper()
        activity = self.activity_entry.get()
        activity = activity.upper()
        partner = self.partner_entry.get()
        total_salary = self.click_salary_var.get()
        transport = self.click_transport_var.get()
        accomodation = self.click_acco_var.get()
        mother_ed = self.click_mother_var.get()
        farther_ed = self.click_father_var.get()
        siblings = self.click_sibling_var.get()
        parental_status = self.click_parental_status_var.get()
        mother_occup = self.click_mother_occup_var.get()
        father_occup = self.click_father_occup_var.get()
        weekly_study_hours = self.click_study_hour_var.get()
        reading_non_scientific = self.click_non_sci_read_var.get()
        reading_scientific = self.click_sci_read_var.get()
        attendance_seminars_dep = self.seminar_attendance_entry.get()
        attendance_seminars_dep = attendance_seminars_dep.upper()
        impact_of_projects = self.click_project_impact_var.get()
        attendances_classes = self.click_class_attendance_var.get()
        preparation_midterm_company = self.click_preparation_one_var.get()
        preparation_midterm_time = self.click_preparation_two_var.get()
        taking_notes = self.click_take_note_var.get()
        listenning = self.click_listening_var.get()
        discussion_improves_interest = self.click_discussion_var.get()
        flip_classrom = self.click_flip_classroom_var.get()
        grade_previous = self.click_cum_grade_var.get()
        grade_expected = self.click_exp_grade_var.get()
        course_id = int(self.click_course_id_var.get())

        if(age == '18-21'):
            age = 1
        elif(age == '22-25'):
            age = 2
        else:
            age = 3

        if(sex == 'Female'):
            sex = 1
        else:
            sex = 2

        if(graduated_h_school_type == 'private'):
            graduated_h_school_type = 1
        elif(graduated_h_school_type == 'state'):
            graduated_h_school_type = 2
        else:
            graduated_h_school_type= 3

        if(scholarship_type == 'None'):
            scholarship_type = 1
        elif(scholarship_type == '25%'):
            scholarship_type = 2
        elif (scholarship_type == '50%'):
            scholarship_type = 3
        elif (scholarship_type == '75%'):
            scholarship_type = 4
        else:
            scholarship_type = 5

        if(additional_work == 'Y'):
            additional_work = 1
        else:
            additional_work = 2

        if(activity == 'Y'):
            activity = 1
        else:
            activity = 2

        if(partner == 'Y'):
            partner = 1
        else:
            partner = 2

        if(total_salary == 'USD 135-200'):
            total_salary = 1
        elif(total_salary =='USD 201-270'):
            total_salary = 2
        elif (total_salary == 'USD 271-340'):
            total_salary = 3
        elif (total_salary == 'USD 341-410'):
            total_salary = 4
        else:
            total_salary = 5

        if(transport == 'Bus'):
            transport = 1
        elif(transport == 'Private car/taxi'):
            transport = 2
        elif(transport == 'Bicycle'):
            transport = 3
        else:
            transport = 4

        if(accomodation == 'rental'):
            accomodation = 1
        elif(accomodation == 'dormitory'):
            accomodation = 2
        elif (accomodation == 'with family'):
            accomodation = 3
        else:
            accomodation = 4

        if(mother_ed == 'primary school'):
            mother_ed = 1
        elif(mother_ed == 'secondary school'):
            mother_ed = 2
        elif (mother_ed == 'high school'):
            mother_ed = 3
        elif (mother_ed == 'university'):
            mother_ed = 4
        elif(mother_ed == 'MSc'):
            mother_ed = 5
        else:
            mother_ed = 6

        if(farther_ed == 'primary school'):
            farther_ed = 1
        elif(farther_ed == 'secondary school'):
            farther_ed = 2
        elif (farther_ed == 'high school'):
            farther_ed = 3
        elif (farther_ed == 'university'):
            farther_ed = 4
        elif(farther_ed == 'MSc'):
            farther_ed = 5
        else:
            farther_ed = 6

        if(siblings =='1'):
            siblings = 1
        elif(siblings == '2'):
            siblings = 2
        elif (siblings == '3'):
            siblings = 3
        elif (siblings == '4'):
            siblings = 4
        elif (siblings == '5 or above'):
            siblings = 5

        if(parental_status == 'married'):
            parental_status = 1
        elif(parental_status =='divorced'):
            parental_status = 2
        else:
            parental_status = 3

        if(mother_occup =='retired'):
            mother_occup = 1
        elif(mother_occup =='housewife'):
            mother_occup = 2
        elif (mother_occup == 'government officer'):
            mother_occup = 3
        elif (mother_occup == 'private sector employee'):
            mother_occup = 4
        elif (mother_occup == 'self-employment'):
            mother_occup = 5
        else:
            mother_occup = 6

        if(father_occup =='retired'):
            father_occup = 1
        elif (father_occup == 'government officer'):
            father_occup = 2
        elif (father_occup == 'private sector employee'):
            father_occup = 3
        elif (father_occup == 'self-employment'):
            father_occup = 4
        else:
            father_occup = 5

        if(weekly_study_hours == 'None'):
            weekly_study_hours = 1
        elif(weekly_study_hours =='<5 hours'):
            weekly_study_hours = 2
        elif (weekly_study_hours == '6-10 hours'):
            weekly_study_hours = 3
        elif (weekly_study_hours == '11-20 hours'):
            weekly_study_hours = 4
        else:
            weekly_study_hours = 5

        if(reading_non_scientific =='None'):
            reading_non_scientific = 1
        elif(reading_non_scientific =='Sometimes'):
            reading_non_scientific = 2
        else:
            reading_non_scientific = 3

        if (reading_scientific == 'None'):
            reading_scientific = 1
        elif (reading_scientific == 'Sometimes'):
            reading_scientific = 2
        else:
            reading_scientific = 3

        if(attendance_seminars_dep == 'Y'):
            attendance_seminars_dep = 1
        else:
            attendance_seminars_dep = 2

        if(impact_of_projects =='Positive'):
            impact_of_projects = 1
        elif(impact_of_projects =='Negative'):
            impact_of_projects = 2
        else:
            impact_of_projects = 3

        if(attendances_classes == 'Always'):
            attendances_classes = 1
        elif(attendances_classes == 'Sometimes'):
            attendances_classes = 2
        else:
            attendances_classes = 3

        if(preparation_midterm_company == 'Alone'):
            preparation_midterm_company = 1
        elif(preparation_midterm_company == 'With friends'):
            preparation_midterm_company = 2
        else:
            preparation_midterm_company = 3

        if(preparation_midterm_time =='closest date to the exam'):
            preparation_midterm_time = 1
        elif(preparation_midterm_time == 'regularly during the semester'):
            preparation_midterm_time = 2
        else:
            preparation_midterm_time = 3

        if(taking_notes == 'Never'):
            taking_notes = 1
        elif(taking_notes =='Sometimes'):
            taking_notes = 2
        else:
            taking_notes = 3

        if(listenning == 'Never'):
            listenning = 1
        elif(listenning =='Sometimes'):
            listenning = 2
        else:
            listenning = 3

        if(discussion_improves_interest == 'Never'):
            discussion_improves_interest = 1
        elif(discussion_improves_interest =='Sometimes'):
            discussion_improves_interest = 2
        else:
            discussion_improves_interest = 3

        if(flip_classrom =='Not useful'):
            flip_classrom = 1
        elif(flip_classrom == 'Useful'):
            flip_classrom = 2
        else:
            flip_classrom = 3

        if(grade_previous == '<2.00'):
            grade_previous = 1
        elif(grade_previous == '2.00-2.49'):
            grade_previous = 2
        elif (grade_previous == '2.50-2.99'):
            grade_previous = 3
        elif (grade_previous == '3.00-3.49'):
            grade_previous = 4
        elif (grade_previous == 'above 3.49'):
            grade_previous = 5

        if (grade_expected == '<2.00'):
            grade_expected = 1
        elif (grade_expected == '2.00-2.49'):
            grade_expected = 2
        elif (grade_expected == '2.50-2.99'):
            grade_expected = 3
        elif (grade_expected == '3.00-3.49'):
            grade_expected = 4
        elif (grade_expected == 'above 3.49'):
            grade_expected = 5



        result_string += "===Performance Grade=== \n"
        student_info = (age, sex, graduated_h_school_type, scholarship_type, additional_work, activity, partner,
                        total_salary, transport, accomodation, mother_ed, farther_ed, siblings, parental_status,
                        mother_occup, father_occup, weekly_study_hours, reading_non_scientific, reading_scientific,
                        attendance_seminars_dep, impact_of_projects, attendances_classes, preparation_midterm_company,
                        preparation_midterm_time, taking_notes, listenning, discussion_improves_interest, flip_classrom,
                        grade_previous, grade_expected, course_id)
        pg_prediction = best_model.predict([student_info])
        cl_accuracy = "{:.2f}".format(model_accuracy*100)
        disp_string = ("This classification has an accuracy of:"+ str(cl_accuracy) +" %\n")



        if(pg_prediction == [0]):
            result_string = (disp_string+ '\n'+ "The final grade of the student would be FAILED.")
        elif(pg_prediction == [1]):
            result_string = (disp_string+ '\n'+ "The final grade of the student would be PASSED, but not HD.")
        else:
            result_string = (disp_string+ '\n'+ "The final grade of the student would be High-Distinction.")

        self.pg_classify_ta.insert('1.0',result_string)


my_pg_GUI = PG_GUI()
