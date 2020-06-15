class ScoreSystem:

    def read(self):
        arch = open("notas.txt", 'r')
        content = arch.read()
        print(content)
        arch.close()

    def update(self, name, n1, n2, n3):
        arch = open("notas.txt", 'a')
        arch.write("\n"+name)
        arch.write(", "+n1)
        arch.write(", "+n2)
        arch.write(", "+n3)
        arch.close()

    def giveAverage(self, name):
        arch = open("notas.txt", 'r')
        content = arch.read()
        students = content.split('\n')

        for value in students:
            students_scores = value.split(',')

            student_name = students_scores[0]
            
            students_scores.pop(0)

            average = lambda scores: sum([int(i) for i in scores]) / 3

            if (student_name == name):
                return average(students_scores)



