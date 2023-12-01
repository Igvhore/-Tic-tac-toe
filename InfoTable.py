V = []
def setV(a1, a2, a3, b1, b2, b3, c1, c2, c3, v):
  num = ((((((((a1*3)+a2)*3+a3)*3+b1)*3+b2)*3+b3)*3+c1)*3+c2)*3+c3
  V.insert(num, v)

for i1 in range(3):
  for i2 in range(3):
    for i3 in range(3):
      for i4 in range(3):
        for i5 in range(3):
          for i6 in range(3):
            for i7 in range(3):
              for i8 in range(3):
                for i9 in range(3):
                  setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,0.5);
                  if i1==i2 and i2==i3 and i3==1: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,1)
                  if i4==i5 and i5==i6 and i6==1: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,1)
                  if i7==i8 and i8==i9 and i9==1: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,1)
                  if i1==i5 and i5==i9 and i9==1: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,1)
                  if i7==i5 and i5==i3 and i3==1: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,1)
                  if i1==i4 and i4==i7 and i7==1: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,1)
                  if i2==i5 and i5==i8 and i8==1: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,1)
                  if i3==i6 and i6==i9 and i9==1: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,1)
                  if i1==i2 and i2==i3 and i3==2: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,0)
                  if i4==i5 and i5==i6 and i6==2: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,0)
                  if i7==i8 and i8==i9 and i9==2: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,0)
                  if i1==i5 and i5==i9 and i9==2: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,0)
                  if i7==i5 and i5==i3 and i3==2: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,0)
                  if i1==i4 and i4==i7 and i7==2: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,0)
                  if i2==i5 and i5==i8 and i8==2: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,0)
                  if i3==i6 and i6==i9 and i9==2: setV(i1,i2,i3,i4,i5,i6,i7,i8,i9,0)

  with open(r'C:\Users\aliev\Downloads\test.txt', 'w') as fp:
    for item in V:
      fp.write("%s\n" % item)
    print('Done')