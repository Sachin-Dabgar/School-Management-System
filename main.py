#  admin functions
import hashlib
import os
import binascii
import eel
# for staff

eel.init("web")


def dataSort():
    get = open("data.txt", "r")
    get.seek(0)
    temp = get.readlines()

    staffid = ""
    fdid = ""
    stid = ""
    acid = ""
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    ac = []
    fd = []
    mt = []
    st = []

    for i in range(len(temp)):
        if temp[i].startswith("ac"):
            ac.append(temp[i])

    for i in range(len(temp)):
        if temp[i].startswith("fd"):
            fd.append(temp[i])

    for i in range(len(temp)):
        if temp[i].startswith("mt"):
            mt.append(temp[i])

    for i in range(len(temp)):
        if temp[i].startswith("st"):
            st.append(temp[i])

    ac.sort()
    fd.sort()
    mt.sort()
    st.sort()

    # regenerate id  for mt
    for i in range(len(mt)):
        if count < 9:
            count += 1
            staffid = "00" + str(count)
        elif count < 99:
            count += 1
            staffid = "0" + str(count)
        else:
            count += 1
            staffid = str(count)

        staffid = "mt" + staffid

        data = mt[i].split("|")
        data[0] = staffid
        buf = f"{data[0]}|{data[1]}|{data[2]}|{data[3]}|{data[4]}|{data[5]}|{data[6]}|{data[7]}"
        mt[i] = buf

    # regenerate id for fd
    for i in range(len(fd)):
        if count1 < 9:
            count1 += 1
            fdid = "000" + str(count1)
        elif count1 < 99:
            count1 += 1
            fdid = "00" + str(count1)
        elif count1 < 999:
            count1 += 1
            fdid = "0"+str(count1)
        else:
            count1 += 1
            fdid = str(count1)

        fdid = "fd" + fdid

        data = fd[i].split("|")
        data[0] = fdid
        buf = f"{data[0]}|{data[1]}|{data[2]}|{data[3]}|\n"
        fd[i] = buf

    # regenerate id for ac
    for i in range(len(ac)):
        if count2 < 9:
            count2 += 1
            acid = "000" + str(count2)
        elif count2 < 99:
            count2 += 1
            acid = "00" + str(count2)
        elif count2 < 999:
            count2 += 1
            acid = "0" + str(count2)
        else:
            count2 += 1
            acid = str(count2)

        acid = "ac" + acid

        data = ac[i].split("|")
        data[0] = acid
        buf = f"{data[0]}|{data[1]}|{data[2]}|{data[3]}|\n"
        ac[i] = buf

    # regenerate id for st
    for i in range(len(st)):
        if count3 < 9:
            count3 += 1
            stid = "00" + str(count3)
        elif count3 < 99:
            count3 += 1
            stid = "0"+str(count3)
        else:
            count3 += 1
            stid = str(count3)

        data = st[i].split("|")
        stid = "st" + stid
        data[0] = stid
        buf = f"{data[0]}|{data[1]}|{data[2]}|{data[3]}|{data[4]}|{data[5]}|{data[6]}|\n"
        st[i] = buf

    fout = open("data.txt", "w")

    for i in range(len(ac)):
        op = f"{ac[i]}"
        fout.write(op)
    for i in range(len(fd)):
        op = f"{fd[i]}"
        fout.write(op)
    for i in range(len(mt)):
        op = f"{mt[i]}"
        fout.write(op)
    for i in range(len(st)):
        op = f"{st[i]}"
        fout.write(op)
    fout.close()
    get.close()

    fin1 = open("data.txt", "r")
    fin2 = open("index.txt", "w")
    fin1.seek(0)

    details = fin1.readlines()

    for i in range(len(details)):
        data = details[i].split("|")
        fin2.write(f"{i}|{data[0]}|\n")

    fin1.close()
    fin2.close()

# login


@eel.expose
def login(uid, password):
    flag = False
    if uid == "admin":
        if password == "admin":
            return "admin"
        else:
            return "wrong password"
    get = open("data.txt", "r")
    temp = get.readlines()
    udata = []
    for i in range(len(temp)):
        if temp[i].startswith(uid):
            udata = temp[i].split("|")
            flag = True
            break
        else:
            flag = False
    # decode
    # stored_password = udata[2]

    # salt = stored_password[:64]
    # stored_password = stored_password[64:]
    # pwdhash = hashlib.pbkdf2_hmac('sha512',
    #                               password.encode('utf-8'),
    #                               salt.encode('ascii'),
    #                               100000)
    # pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    # decode end

    print(udata)
    if not flag:
        return "nouser"
    if password != udata[2]:
        print("wrong password")
        return "Wrong password"
    elif udata[0].startswith("mt"):
        return "mentor"

    get.close()


@eel.expose
def addStaff(name, password, classes, email, quali, gender):
    fin = open("data.txt", 'r')
    fin.seek(0)
    details = fin.readlines()
    count = 0
    # staffid = ""
    for i in range(len(details)):
        data = details[i].split("|")
        if data[0].startswith("mt"):
            if data[4] == email:
                print("Staff already exist")
                return "Staff already exist"
                exit()
    for i in range(len(details)):
        if details[i].startswith("mt"):
            count += 1
    if count < 9:
        count += 1
        staffid = "00" + str(count)
    elif count < 99:
        count += 1
        staffid = "0" + str(count)
    else:
        count += 1
        staffid = str(count)
    staffid = "mt" + staffid

    # for password hashing
    # salt = hashlib.sha256(os.urandom(60)).hexdigest().#encode('ascii')
    # pwdhash = hashlib.pbkdf2_hmac('sha512', password.#encode('utf-8'),
    # salt, 100000)
    #pwdhash = binascii.hexlify(pwdhash)
    #password = (salt + pwdhash).decode('ascii')
    # end

    final = f"{staffid}|{name}|{password}|{classes}|{email}|{quali}|{gender}|\n"
    details.append(final)
    # opening file
    fout = open("data.txt", "w")
    for i in range(len(details)):
        op = f"{details[i]}"
        fout.write(op)

    fout.close()
    fin.close()
    dataSort()
    return "Successfully Data Added"


@eel.expose
def removeId(id):
    udata = []
    get = open("data.txt", "r")
    details = get.readlines()
    for i in range(len(details)):
        if details[i].startswith(id):
            udata = details[i].split("|")
            clear = ""
            details[i] = clear
            fout = open("data.txt", "w")
            for j in range(len(details)):
                op = f"{details[j]}"
                fout.write(op)
            fout.close()
    get.close()
    dataSort()

    return f"the data of {udata[3]} gone "


@eel.expose
def modifyStaff(uid, name, password, classes, email, quali, gender):
    vid = ""
    get = open("data.txt", "r")
    iget = open("index.txt", "r")
    details = get.readlines()
    index = iget.readlines()

    for i in range(len(index)):
        data = index[i].split("|")
        if data[1].startswith(uid):
            vid = data[0]

    vid = int(vid)
    vdata = details[vid].split("|")
    vdata[1] = name
    vdata[2] = password
    vdata[3] = classes
    vdata[4] = email
    vdata[5] = quali
    vdata[6] = gender
    vupdate = f"{vdata[0]}|{vdata[1]}|{vdata[2]}|{vdata[3]}|{vdata[4]}|{vdata[5]}|{vdata[6]}|\n"
    details[vid] = vupdate

    fout = open("data.txt", "w")
    for i in range(len(details)):
        op = details[i]
        fout.write(op)

    fout.close()
    get.close()
    iget.close()
    dataSort()
    return f"Modified Data of {uid}"


@eel.expose
def searchData(id):
    iget = open("index.txt", "r")
    index = iget.readlines()
    get = open("data.txt", "r")
    temp = get.readlines()
    pid = ""
    for i in range(len(index)):
        data = index[i].split("|")
        if data[1] == id:
            pid = data[0]
    pid = int(pid)
    userData = temp[pid].split("|")
    print(userData)
    get.close()
    iget.close()
    return userData

# for students


@eel.expose
def addStudent(classes, mentorid, name, phno, gender, blood):
    print(classes, mentorid, name, phno, gender, blood)
    fin = open("data.txt", 'r')
    fin.seek(0)
    details = fin.readlines()
    count = 0
    # staffid = ""
    for i in range(len(details)):
        data = details[i].split("|")
        if data[4] == phno:
            print("Student already exist")
            return "student already exsist"
            exit()
    for i in range(len(details)):
        if details[i].startswith("st"):
            count += 1
    if count < 9:
        count += 1
        studentid = "00" + str(count)
    elif count < 99:
        count += 1
        studentid = "0" + str(count)
    else:
        count += 1
        studentid = str(count)
    studentid = "st" + studentid
    final = f"{studentid}|{classes}|{mentorid}|{name}|{phno}|{gender}|{blood}|\n"
    details.append(final)
    # opening file
    fout = open("data.txt", "w")
    for i in range(len(details)):
        op = f"{details[i]}"
        fout.write(op)
    fout.close()
    fin.close()
    dataSort()
    return "Student Added Successfully"


@eel.expose
def modifyStudent(uid, classes, mentorid, name, phno, gender, blood):
    vid = ""
    get = open("data.txt", "r")
    iget = open("index.txt", "r")
    details = get.readlines()
    index = iget.readlines()

    for i in range(len(index)):
        data = index[i].split("|")
        if data[1].startswith(uid):
            vid = data[0]

    vid = int(vid)
    vdata = details[vid].split("|")
    vdata[1] = classes
    vdata[2] = mentorid
    vdata[3] = name
    vdata[4] = phno
    vdata[5] = gender
    vdata[6] = blood
    vupdate = f"{vdata[0]}|{vdata[1]}|{vdata[2]}|{vdata[3]}|{vdata[4]}|{vdata[5]}|{vdata[6]}|\n"
    details[vid] = vupdate

    fout = open("data.txt", "w")
    for i in range(len(details)):
        op = details[i]
        fout.write(op)

    fout.close()
    get.close()
    iget.close()
    dataSort()
    return f"Modified Data of {uid}"
# display


@eel.expose
def displayStaff():
    get = open("data.txt", "r")

    details = get.readlines()
    list = []
    for i in range(len(details)):
        if details[i].startswith("mt"):
            list.append(details[i])
    count = len(list)
    return list, count


@eel.expose
def displayStudent():
    get = open("data.txt", "r")

    details = get.readlines()
    list = []
    for i in range(len(details)):
        if details[i].startswith("st"):
            list.append(details[i])
    count = len(list)
    return list, count


# achievements


@eel.expose
def addAc(title, desc, year):
    fin = open("data.txt", 'r')
    fin.seek(0)
    details = fin.readlines()
    count = 0
    for i in range(len(details)):
        data = details[i].split("|")
        if data[1] == title:
            print("Activity already exsit")
            return "Activity already exsit"
            exit()
    for i in range(len(details)):
        if details[i].startswith("ac"):
            count += 1
    if count < 9:
        count += 1
        staffid = "000" + str(count)
    elif count < 99:
        count += 1
        staffid = "00" + str(count)
    elif count < 999:
        count += 1
        staffid = "0" + str(count)
    else:
        count += 1
        staffid = str(count)
    staffid = "ac" + staffid
    final = f"{staffid}|{title}|{desc}|{year}|\n"
    details.append(final)
    # opening file
    fout = open("data.txt", "w")
    for i in range(len(details)):
        op = f"{details[i]}"
        fout.write(op)
    fout.close()
    fin.close()
    dataSort()
    return "Achivement added "


@eel.expose
def modifyAc(uid, title, desc, year):
    vid = ""
    get = open("data.txt", "r")
    iget = open("index.txt", "r")
    details = get.readlines()
    index = iget.readlines()
    for i in range(len(index)):
        data = index[i].split("|")
        if data[1].startswith(uid):
            vid = data[0]
    vid = int(vid)
    vdata = details[vid].split("|")
    vdata[1] = title
    vdata[2] = desc
    vdata[3] = year
    vupdate = f"{vdata[0]}|{vdata[1]}|{vdata[2]}|{vdata[3]}|\n"
    details[vid] = vupdate
    fout = open("data.txt", "w")
    for i in range(len(details)):
        op = details[i]
        fout.write(op)
    fout.close()
    get.close()
    iget.close()
    dataSort()
    return f"Modified Data of {uid}"


# display achievements
@eel.expose
def displayAc():
    get = open("data.txt", "r")

    details = get.readlines()
    list = []
    for i in range(len(details)):
        if details[i].startswith("ac"):
            list.append(details[i])
    count = len(list)
    return list, count


# for feedback
@eel.expose
def addFeedback(name, email, feed):
    print(name, email, feed)
    fin = open("data.txt", 'r')
    fin.seek(0)
    details = fin.readlines()
    count = 0

    for i in range(len(details)):
        if details[i].startswith("fd"):
            count += 1
    if count < 9:
        count += 1
        staffid = "000" + str(count)
    elif count < 99:
        count += 1
        staffid = "00" + str(count)
    elif count < 999:
        count += 1
        staffid = "0" + str(count)
    else:
        count += 1
        staffid = str(count)
    staffid = "fd" + staffid
    final = f"{staffid}|{name}|{email}|{feed}|\n"
    details.append(final)
    # opening file
    fout = open("data.txt", "w")
    for i in range(len(details)):
        op = f"{details[i]}"
        fout.write(op)
    fout.close()
    fin.close()
    dataSort()

    return "Thank you for response"


@eel.expose
def displayFd():

    get = open("data.txt", "r")

    details = get.readlines()
    list = []
    for i in range(len(details)):
        if details[i].startswith("fd"):
            list.append(details[i])
    count = len(list)
    return list, count

# remove for admin

# staff can also modify the details of students


# def driver():
    # removeId("ac0001")
    # addStaff("twinkal", "tiku", "7th", "tiku@email.com", "be", "female")
    # dataSort()
    # modifyStaff("mt002", "shshhs", "anything", "3rd",
    #             "email@email.com", "mtech", "male")
    # addStudent("3th", "mt003", "amit bhadana", "8383839383", "male", "o-")
    # addAc("halloffame", "google approved", "2022")
    # modifyStudent("st003", "1st", "mt003", "carry", "3983828383", "male", "ab-")
    # modifyAc("ac0002", "bgmi india", "faug is in trouble", "2025")
    # displayStaff()
    # displayStudent()
    # addFeedback("bahubali", "bahu@gmail.com", "jai mahishmati")

    # displayAc()
    # displayFd()

    # login("mt006", "tiku")

eel.start("index.html")
