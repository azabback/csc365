import pandas as pd


def to_float(c):
    return float(c)


def stu_ln_search(df: pd.DataFrame, ln_in: str, bus: bool) -> None:
    res_str = ""
    for i in range(0, len(df.StLastName)):
        if df["StLastName"].iloc[i] == ln_in:
            if not bus:
                res_str += f"\n\n{df.StLastName.iloc[i]}, {df.StFirstName.iloc[i]}\nGrade {df.Grade.iloc[i]}, " \
                          f"Classroom {df.Classroom.iloc[i]}\nTeacher: {df.TLastName.iloc[i]}, {df.TFirstName.iloc[i]}"
            else:
                res_str += f"\n\n{df.StLastName.iloc[i]}, {df.StFirstName.iloc[i]}\nBus {df.Bus.iloc[i]}"
    print(res_str.strip())


def bus_search(df: pd.DataFrame, bus_in: int) -> None:
    res_str = ""
    for i in range(0, len(df.Bus)):
        if df.Bus.iloc[i] == bus_in:
            res_str += f"\n{df.StLastName.iloc[i]}, {df.StFirstName.iloc[i]}," \
                       f" Grade {df.Grade.iloc[i]}, Classroom {df.Classroom[i]}"
    print(res_str.strip())


def grade_gpa_avg_search(df: pd.DataFrame, grade_in: int):
    grade_df = df[df.Grade == grade_in]
    if len(grade_df) != 0:
        print(f"Grade {grade_in} Average: "
              f"{round(sum(grade_df.GPA)/len(grade_df.GPA), 2)}")


def teacher_search(data: pd.DataFrame, tlastname: str):
  df_students = data[data["TLastName"] == tlastname]
  # df_students = data[['lastname','firstname']].where(data['TLastName']== tlastname).dropna()
  for i in range(len(df_students)):
    list_students = df_students[["lastname", "firstname"]].values[i]
    students = ""
    for i in list_students:
      students += str(i) + ","
    students = students[:-1]
    print(students)


