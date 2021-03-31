# Prepared by : Shvm-k
# License : MIT
#برنامج للتحويل من درجات حرارة مئوية الى درجات بافهرنهايت
print("ادخل درجة الحرارة المئوية")
c=input()
if(c.isdigit()):
    c=int(c)
    a=c*1.8+32
    print(c,"دجة مئوية=", a ,"فهرناهايت(f°)")
else:
    print(c+" ليس رقم")

print("ادخل درجة الحرارة بالفهرناهايت")
f=input()
if(f.isdigit()):
    f=int(f)
    b = (f - 32) / 1.8
    print(f, "فهرناهايت=", b, "درجة مئوية(c°)")
else:
    print(f+" ليس رقم")
