def arithmetic_arranger(problems, answer = False):
  line1, line2, line3, line4 = "", "", "", ""
  if (answer): line4 = "\n"
  if (len(problems) > 5): 
    return "Error: Too many problems."

  for problem in problems:
    nbr1 = problem.split(' ')[0]
    nbr2 = problem.split(' ')[2]
    operator = problem.split(' ')[1]

    if (operator != '+' and operator != '-'): 
      return "Error: Operator must be '+' or '-'."
    if (nbr1.isdigit() == False or nbr2.isdigit() == False):
      return "Error: Numbers must only contain digits."
    if (len(nbr1) > 4 or len(nbr2) > 4):
      return "Error: Numbers cannot be more than four digits."

    space = len(max(nbr1, nbr2, key=len))
    line1 += "  " + " " * (space - len(nbr1)) + str(nbr1) + " " * 4
    line2 += operator + " " + " " * (space - len(nbr2)) + str(nbr2) + " " * 4
    line3 += "--" + "-" * space + " " * 4
    if (answer):
      result = eval(problem)
      line4 += " " * ((space + 2) - len(str(result))) + str(result) + " " * 4
  
  return line1[:-4] + "\n" + line2[:-4] + "\n" + line3[:-4] + line4[:-4]