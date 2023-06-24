def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    print("Welcome!");
    
    male_students = int(input("Insert Number Of Male Students Here: "));
    female_students = int(input("Insert Number Of Female Students Here: "));
    student_total = male_students + female_students;

    m_perc = (male_students / student_total) * 100;
    f_perc = (female_students / student_total) * 100;

    print(f"The total number of students: \t {student_total}");
    print(f"The number of males and females  \t{male_students} \t {female_students}");
    print(f"The percentage of males and females  \t{m_perc: .2f}% \t {f_perc: .2f}%");

    print("Please see RESULTS above. Thank you!");

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
