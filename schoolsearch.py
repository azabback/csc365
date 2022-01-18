import searchfunctions
import pandas as pd


def format_data() -> pd.DataFrame:
    stu_df = pd.read_csv("students.txt", header=None)
    stu_df.columns = ["StLastName", "StFirstName", "Grade", "Classroom", "Bus",
                      "GPA", "TLastName", "TFirstName"]
    return stu_df


def main():
    stu_df = format_data()
    print("Please enter a valid search.\nPossible searches are:\n"
          "     - S[tudent]: <lastname> [B[us]]\n          - find student info by last name\n"
          "          - if B[us] option is specified, bus route information will be provided\n"
          "     - T[eacher]: <lastname>\n"
          "          - find student list by teacher last name\n"
          "     - G[rade]: <Number>\n"
          "          - find student list by grade number\n"
          "     - B[us]: <Number>\n          - find student info by bus route number\n"
          "     - G[rade]: <Number> H[igh] or\n"
          "       G[rade]: <Number> L[ow]\n"
          "          - find student info by grade number, either highest GPA in"
          "given grade, or lowest\n"
          "     - A[verage]: <Number>\n"
          "          - find average GPA for given grade number\n"
          "     - I[nfo]\n"
          "          - get overall info for each grade\n"
          "     - Q[uit]")
    while True:
        search = str(input("Enter Search: "))
        search_l = [i for i in search.split()]
        search_term = search_l[0]
        if len(search_l) > 1:
            val = search_l[1]
        if len(search_l) > 3:
            print("Invalid search.")
        else:
            if search_term == "S" or search_term == "Student":
                if len(search_l) == 3 and (search_l[2] == "B"
                                           or search_l[2] == "Bus"):
                    searchfunctions.stu_ln_search(stu_df, val, True)
                else:
                    searchfunctions.stu_ln_search(stu_df, val, False)
            elif search_term == "T" or search_term == "Teacher":
                searchfunctions.teacher_search(stu_df, val)
            # elif search_term == "G" or search_term == "G[rade]":
            #     insert function here
            #     insert High and Low functions too
            elif search_term == "B" or search_term == "Bus":
                searchfunctions.bus_search(stu_df, int(val))
            elif search_term == "A" or search_term == "Average":
                searchfunctions.grade_gpa_avg_search(stu_df, int(val))
            # elif search_term == "I" or search_term == "Info":
            #     insert function here
            elif search_term == "Q" or search_term == "Quit":
                break
            else:
                print("Invalid search.")


if __name__ == '__main__':
    main()

