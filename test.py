#! python3
import os
import time

def inc(x, example=0):
    x += 1
    return x

def incBy(y,n):
    y += n
    return y

#def printNoBr(x):
#    print(x, end='', sep='')

def printNoSep(x):
    print(x, sep='')

def printCode(code):
    print(code, "= ", end="")
    if code[0:5] == "print":
        exec (code)
    else:
        code="print("+code+")"
        exec (code)

print('test 0')
print()

print("Hello", "World!")

print()
print('test 1')
print()
cnt = 0
x = 2
y = 2012

# while (cnt<=y) я без понятия, как тут писать циклы пока
#    do x=x*x
#    inc (cnt)
print(x)

print()
print('test 2')
print()
x = "blue"
y = "green"
z = x
print(x, y, z)
z = y
print(x, y, z)
x = z
print(x, y, z)

print()
print('test 3')
print()
route = 866
print(route, type(route))
route = "North"
print(route, type(route))

print()
print('test 4')
print()
list = [325611, ]

x = 123
list.append(x)
y = 456
list.append(y)
z = 789
list.append(z)
a = 000
list.insert(a, 0)
print(list)
print(len(list))
list.remove(0)
print(list)
print(len(list))
print("Numpad:D")
print(list[2])
print(list[1])
print(list[0])

print()
print('test 5')
print()
b = None
print("a is not None, b is None")
print(a is not None, b is None)

print()
print('test 6')
print()
a = 2
b = 6
print('a==b?', a == b, 'a<b?', a < b)
a = 'cheburek'
b = 'cheburek'
print(a is b)
print(a == b)

a = 0
print('a=9')
print('0 <= a <= 10 is', 0 <= a <= 10)

# print('three'<4) - низзя
# print('3'<4) - так же
print("int('3')<4 is", int('3') < 4, '- так можно')

print()
print('test 7g')
print()
p = (4, 'frog', 9, -33, 9, 2)
print("p=(4, 'frog', 9, -33, 9, 2)")
print('2 in p is', 2 in p)
print('"dog" not in p is', "dog" not in p)
print()
print('phase="Peace is no longer permitted during Winterval"')
phase = "Peace is no longer permitted during Winterval"
print('"v" in phase is', "v" in phase)
print('"ring" in phase is', "ring" in phase)

print()
print('test 8wtf')
print()
five = 5
two = 2
zero = 0
five and two
two and five
five and zero
# нафиг это дерьмо, я примерно понимаю алгебру-логику, но зачем
# с integer это делать не понимаю. В условиях - нужно, но зачем
# integer???

print()
print('test 9g')
print('циклы')
print()

something = 35  # input  я пока не знаю, как вводить, но если тут что-то
# будет, то something будет True
#print('Введите что-нибудь')
somethingother = 10
# if somethingbyinput
if something < 10:
    print("test")  # строка1
elif somethingother < something:
    print('something_other<something and if elif work')  # строка2
else:
    print("something_other<something and if elif didn't work")  # строка else (выполняется )



while True:
    try:
        print('Введите что-нибудь или 0 для остановки (^Z тоже сработает) (33 пропускается)')
        #somethingbyinput = input()
        somethingbyinput = 1
        cnt=0
        print("Ввод данных закоментирован, включён рандом")
        if somethingbyinput and cnt<=10:
            inc(cnt)
            from random import randint###!!!
            somethingbyinput=randint(0,15)
            print("Вы ввели:")
            print()
            somethingbyinput = int(somethingbyinput)
            if somethingbyinput==1:
                print("one")
            elif somethingbyinput==2:
                print("two")
            elif somethingbyinput==3:
                print("three")
            elif somethingbyinput==3:
                pass
            elif somethingbyinput==4:
                print("four")
            elif somethingbyinput==5:
                print("five")
            elif somethingbyinput==6:
                print("six")
            elif somethingbyinput==7:
                print("seven")
            elif somethingbyinput==8:
                print("eight")
            elif somethingbyinput==9:
                print("nine")
            elif somethingbyinput==10:
                print("ten")
            elif somethingbyinput==0:
                break
            else:
                print(somethingbyinput)
    except ValueError as err:
        #print(err)
        print("Введено не число, а вот что:", somethingbyinput)
    except EOFError:
        print("except EOFError")
        break #нужно только при цикле. Останавливает цикл. Здесь, например,
        #цикл вообще без условия

print("Всё, надоело с if баловаться")
print()

countries=("Дания", "Финляндия", "Норвегия", "Швеция")
for country in countries:
    print(country)

for letter in "абвгдеёжзийклмнопрстуфхцшщчьыъэюя":
    if letter in "аеёиоуыэюя":
        print(letter, " - гласная")
    else:
        print(letter, " - согласная")

print()
print("test 10g")
print("операторы")
print()

print()
print("21.12.2015")
print("diary > Написал тудушник, обратный отсчёт и прогу для средней цены на бу технику")
print()

#   #printCode("x=3")
#   print(x)
#
#   def assign(code):
#       for cnt in code: #for cnt in 'x=2'
#           if cnt == "=":
#               file = open('test_temp.py', 'w')
#               file.write(code)
#               file.close()
#               import test_temp
#               print(" is set")
#               assign=True
#       if assign != True:
#           print("")
#   #  def test(code):
#   #      print('1x=',x)
#   #      print(code)
#   #      exec(compile('x=5', '<string>', 'single'))
#   #      exec(compile('a = 5', '<string>', 'single'))
#   #      print('a=',a)
#   #      print('2x=',x)
#   #
#   #  x=2
#   #  print("test set x to 2")
#   #
#   #  test("x=5")
#   #  print("3x=",x)
#   code = compile('for i in range(3): print("Python is cool")',
#                  'foo.py','exec')
#   eval(code)
#   testassign=10
#   def printAssign(code): # Это не присвоение, а выполнение. Хотел спать, поэтому написал фигню. ПОшёл савпать.
#       #printNoBr(code)   # попробуй в файл сохранять не всё выражение, а только после равно и присваивать variable
#                          # должно работать
#       #printNoBr(" = ")
#       cnt=0
#       cnt2=2
#       while cnt<len(code):
#           #print("code[cnt] =", code[cnt], ", cnt =", cnt, "cnt2 =", cnt2, ", code[cnt:cnt2] =", code[cnt:cnt2])
#           #print(code)
#           if code[cnt] == "=" or code[cnt:cnt2] == " =":
#               #print('found')
#               #print("variable = '", code[:cnt], "'", sep="")
#               variable = code[:cnt]
#               print(code, sep='')
#               print(variable, " = ", sep="", end="")
#               file=open('test_temp.py', 'w')
#               file.write("global " + variable + '\n')
#               file.write(code + '\n')
#               file.write("print("+variable+")")
#               #file.write('global')
#               file.close()
#               break
#           cnt += 1
#           cnt2 += 1
#       import test_temp
#       # code=code+"\nprint("+'testassign'+")"
#       # toExecute = compile(code,
#       #                     'foo.py', 'exec')
#       # print(eval(toExecute))
#   #printAssign("testassign = 100+600")
#   #printCode("testassign = 100+600")
#
#   def printAssign(code):
#       print("start", "/n", "cnt=0")
#       cnt=0
#       print("while cnt(",cnt,")<len(code)(",len(code),")")
#       while cnt<len(code):
#           print('if code[cnt] == "=":')
#           if code[cnt] == "=":
#               print('code[', cnt, '] = (', code[cnt],')')
#               print()
#               assignation = code[:cnt]
#               print("assignation = (", assignation,')', sep='')
#               print('(', assignation[len(assignation)-1:len(assignation)], ')', sep='')
#               if assignation[len(assignation)-1:len(assignation)] == " ":
#                   global assignation
#                   assignation=assignation[:len(assignation)-1]
#               print("assignation = (", assignation,')', sep='')
#               print ("if assignation[len(assignation):len(assignation)+2] == " ":")
#               #var = code[cnt:]
#               #print("var =", var)
#               execglobals={assignation:1}
#               execexecglobals="{"+assignation+":1}"
#               execcode="""
#   global """+assignation+"""
#   exec('"""+code+"""', """+execexecglobals+""")
#   print("""+assignation+""")
#               """
#               print(execcode)
#
#               #code2 = compile(execcode,
#               #'foo.py','exec')
#
#               testassign=exec(execcode,execglobals)
#               print("Мы получили", assignation, "=", testassign)
#           cnt += 1
#   nouse=input()
#   printAssign("testassign = 100+600")
#
#
#   def test(test):
#       x=5
#       assign("x=2")
#       print('x =', x)
#       x += 1
#       print('x =', x)



print()
print("21.12.2015")
print("diary > Написал более умный обратный отсчёт с недопрогрессбаром и возможностью "
      "задать последовательность заданий, вконец заколебался с printAssign, так и смогёл")
print()

seeds = ['sesame', 'sunflower']
print("seeds = ['sesame', 'sunflower']")
seeds += ['pumpkin']
print("seeds += ['pumpkin']")
print("seeds = ", seeds)
try:
    print("seeds += 5")
    seeds += 5
    print(seeds)
except TypeError as err:
    print(err)
seeds += [5]
print("seeds += [5]")
printCode("print(seeds)")
seeds += [9, 1, 5, 'poppy']
print("seeds += [9, 1, 5, 'poppy']")
print("seeds = ", seeds)
seeds += "durian"
print("seeds += 'durian'")
print("seeds = ", seeds)

print()
print("test 10g")
print("ввод/вывод XD")
print()

print("Введите натуральные числа, после каждого нажимая Enter, или просто нажмите Enter для завершения")
total = 0
count = 0
while True:
    line=input("integer: ")
    if line:
        try:
            number=int(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else:
        break
    if count:
        print("count = ", count, ", total = ", total, ", mean = ", total/count, sep="")

