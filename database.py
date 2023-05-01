def datab(n,c):
    name= n
    confident = c
    import sqlite3
    conn = sqlite3.connect('studentinfo.db')
    d=conn.execute("select * from studentinfo where Name = ?",[name]);
    for a in d:
        print(a)
    roll=a[1]
    address = a[2]
    dep = a[3]
    print(roll,address,dep)

    s = conn.execute("Select * from studentinfo")
    for a in s:
        print(a)

    conn.close()

    import sqlite3
    conn = sqlite3.connect( 'sample.db')

    data = conn.execute('select * from student')
    for x in data:
        print(x)

    import pytz
    from datetime import datetime

    tz_nepal = pytz.timezone("Asia/Kathmandu")
    date = datetime.now(tz_nepal)
    print(date)
    d=date.strftime('%Y-%m-%d')
    print(d)

    time = date.strftime('%H:%M:%S')
    print(time)

    data = conn.execute("select * from student where date =? and name =?",([d,name]))
    a = []
    for x in data:
        a.append(x[0])
        print(a)
    if(confident > 50):
        if(len(a)>0):
            m = "Attendance already done"
            print(m)
        else:
            conn.execute("INSERT INTO `student` (`Name`, `Roll_no`, `Address`, `Category`, `Date`, `Time`) VALUES (?, ?, ?, ?, ?, ?)",(name,roll,address,dep,d,time))
            m="Data inserted"
            print(m)
            conn.commit()
    else:
        m="confident is less than 50%"
        print(m)

    data = conn.execute('select * from student')
    for x in data:
        print(x)
    conn.close()
    return m