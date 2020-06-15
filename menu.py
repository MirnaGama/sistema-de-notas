from sistema_notas import ScoreSystem

s = System()

s.update("Maria", "10", "8", "7")
s.read()

print(s.giveAverage("Maria"))