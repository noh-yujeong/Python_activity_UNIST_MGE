# implement here your solution
from module06_trees.part01.decision_tree import DecisionTree

class MRP:

    __expense = 0

    def __init__(self, company):
        self._company = company
        self._parts = []
        self._subassemblies = []


    def storage_parts(self):
        read_file_name = "parts.dat"
        read_file = open(read_file_name, "r")
        for line in read_file.readlines():
            values = line.strip().split(',')
            self._parts.append(values)
        read_file.close()
        for i in range(len(self._parts)):
            self._parts[i][2] = int(self._parts[i][2])
            self._parts[i][3] = int(self._parts[i][3])
        return self._parts


    def storage_subassemblies(self):
        read_file_name = "subassemblies.dat"
        read_file = open(read_file_name, "r")
        for line in read_file.readlines():
            values = line.strip().split(',')
            self._subassemblies.append(values)
        read_file.close()
        for i in range(len(self._subassemblies)):
            self._subassemblies[i][1] = int(self._subassemblies[i][1])
        return self._subassemblies


    def calculate_and_verify(self, product):
        for i in range(len(self._subassemblies)):
            if self._subassemblies[i][0] == "SA01":
                s1 = self._subassemblies[i][1]
            elif self._subassemblies[i][0] == "SA02":
                s2 = self._subassemblies[i][1]
            elif self._subassemblies[i][0] =="SA03":
                s3 = self._subassemblies[i][1]
            elif self._subassemblies[i][0] == "SA04":
                s4 = self._subassemblies[i][1]
            elif self._subassemblies[i][0] == "SA05":
                s5 = self._subassemblies[i][1]
            elif self._subassemblies[i][0] == "SA06":
                s6 = self._subassemblies[i][1]
        for j in range(len(self._parts)):
            if self._parts[j][0] == "frame_a":
                fra = self._parts[j][2]
            elif self._parts[j][0] == "frame_b":
                frb = self._parts[j][2]
            elif self._parts[j][0] == "chain_a":
                cha = self._parts[j][2]
            elif self._parts[j][0] == "chain_b":
                chb = self._parts[j][2]
            elif self._parts[j][0] == "tire_a":
                tia = self._parts[j][2]
            elif self._parts[j][0] == "wheel_a":
                wha = self._parts[j][2]
            elif self._parts[j][0] == "completewheel_a":
                cwa = self._parts[j][2]
            elif self._parts[j][0] == "handlebar_c":
                hac = self._parts[j][2]
            elif self._parts[j][0] == "rubberhandle_a":
                rha = self._parts[j][2]
        if product == "coolbike":
            if int(rha/2) > hac:
                s4 = s4 + hac
            else:
                s4 = s4 + int(rha/2)
            if tia > wha:
                s2 = s2 + int(wha/2)
            else:
                s2 = s2 + int(tia/2)
            if frb > cha:
                s1 = s1 + cha
            else:
                s1 = s1 + frb
            if s1 > s2:
                s3 = s3 + s2
            else:
                s3 = s3 + s1
            if s3 > s4:
                n_cb = s4
            else:
                n_cb = s3
            return n_cb
        elif product == "boringbike":
            if int(rha/2) > hac:
                s4 = s4 + hac
            else:
                s4 = s4 + int(rha/2)
            if fra > chb:
                s6 = s6 + chb
            else:
                s6 = s6 + fra
            if cwa > s6:
                s5 = s5 + s6
            else:
                s5 = s5 + cwa
            if s5 > s4:
                n_bb = s4
            else:
                n_bb = s5
            return n_bb
        else:
            product = input("{0} produces boringbike or coolbike.\nTry again: ".format(self._company))
            return self.calculate_and_verify(product)


    def procurement(self, part, num_order):
        if num_order >= 7:
            for i in range(len(self._parts)):
                if self._parts[i][0] == part:
                    self._parts[i][2] = int(self._parts[i][2]) + num_order + 2
                    self.__expense = self.__expense + int(self._parts[i][3]) * (num_order + 2)
                else:
                    pass
        elif num_order < 0:
            num_order = input("We can't not buy minus units\n Put another number: ")
            return self.procurement(part, num_order)
        else:
            for i in range(len(self._parts)):
                if self._parts[i][0] == part:
                    self._parts[i][2] = self._parts[i][2] + num_order + 1
                    self.__expense = self.__expense + self._parts[i][3] * (num_order + 1)
                else:
                    pass


    def execute_order(self, product, num_order):
        if product == "coolbike":
            for i in range(len(self._subassemblies)):
                if self._subassemblies[i][0] == "SA03":
                    if self._subassemblies[3][1] == num_order:
                        self._subassemblies[3][1] = self._subassemblies[3][1] - num_order
                        break
                    else:
                        pass
                    if self._subassemblies[i][1] >= num_order:
                        self._subassemblies[i][1] = self._subassemblies[i][1] - num_order

                    else:
                        n = num_order - self._subassemblies[i][1]
                        for j in range(len(self._subassemblies)):
                            if self._subassemblies[j][0] == "SA01":
                                if self._subassemblies[j][1] >= n:
                                    self._subassemblies[j][1] = self._subassemblies[j][1] - n
                                    self._subassemblies[i][1] = self._subassemblies[i][1] + n/2
                                else:
                                    m = n - self._subassemblies[j][1]
                                    for k in range(len(self._parts)):
                                        if self._parts[k][0] == "frame_b":
                                            if self._parts[k][2] >= m:
                                                self._parts[k][2] = self._parts[k][2] - m
                                                self._subassemblies[j][1] = self._subassemblies[j][1] + m/2
                                            else:
                                                l = m - self._parts[k][2]
                                                self.procurement(self._parts[k][0], l)
                                        elif self._parts[k][0] == "chain_a":
                                            if self._parts[k][2] >= m:
                                                self._parts[k][2] = self._parts[k][2] - m
                                                self._subassemblies[j][1] = self._subassemblies[j][1] + m/2
                                            else:
                                                l = m - self._parts[k][2]
                                                self.procurement(self._parts[k][0], l)
                                        else:
                                            pass
                            elif self._subassemblies[j][0] == "SA02":
                                if self._subassemblies[j][1] >= n:
                                    self._subassemblies[j][1] = self._subassemblies[j][1] - n
                                    self._subassemblies[i][1] = self._subassemblies[i][1] + n/2
                                else:
                                    m = n - self._subassemblies[j][1]
                                    for k in range(len(self._parts)):
                                        if self._parts[k][0] == "tire_a":
                                            if self._parts[k][2] >= 2 * m:
                                                self._parts[k][2] = self._parts[k][2] - 2 * m
                                                self._subassemblies[j][1] = self._subassemblies[j][1] + m/2
                                            else:
                                                l = 2 * m - self._parts[k][2]
                                                self.procurement(self._parts[k][0], l)
                                        elif self._parts[k][0] == "wheel_a":
                                            if self._parts[k][2] >= 2 * m:
                                                self._parts[k][2] = self._parts[k][2] - 2 * m
                                                self._subassemblies[j][1] = self._subassemblies[j][1] + m/2
                                            else:
                                                l = 2 * m - self._parts[k][2]
                                                self.procurement(self._parts[k][0], l)
                                        else:
                                            pass
                            else:
                                pass
                        return self.execute_order(product, num_order)
                elif self._subassemblies[i][0] == "SA04":
                    if self._subassemblies[i][1] >= num_order:
                        self._subassemblies[i][1] = self._subassemblies[i][1] - num_order
                    else:
                        n = num_order - self._subassemblies[i][1]
                        for j in range(len(self._parts)):
                            if self._parts[j][0] == "handlebar_c":
                                if self._parts[j][2] >= n:
                                    self._parts[j][2] = self._parts[j][2] - n
                                    self._subassemblies[i][1] = self._subassemblies[i][1] + n/2
                                else:
                                    m = n - self._parts[j][2]
                                    self.procurement(self._parts[j][0], m)
                            elif self._parts[j][0] == "rubberhandle_a":
                                if self._parts[j][2] >= 2 * n:
                                    self._parts[j][2] = self._parts[j][2] - 2 * n
                                    self._subassemblies[i][1] = self._subassemblies[i][1] + n/2
                                else:
                                    m = 2 * n - self._parts[j][2]
                                    self.procurement(self._parts[j][0], m)
                            else:
                                pass
                        return self.execute_order(product, num_order)
                else:
                    pass
            if num_order > 5:
                n = int(num_order/3)
                for i in range(len(self._subassemblies)):
                    if self._subassemblies[i][0] == "SA01":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + n
                    elif self._subassemblies[i][0] == "SA02":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + n
                    elif self._subassemblies[i][0] == "SA03":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + n
                    elif self._subassemblies[i][0] == "SA04":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + n
                    else:
                        pass
            else:
                for i in range(len(self._subassemblies)):
                    if self._subassemblies[i][0] == "SA01":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + 1
                    elif self._subassemblies[i][0] == "SA02":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + 1
                    elif self._subassemblies[i][0] == "SA03":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + 1
                    elif self._subassemblies[i][0] == "SA04":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + 1
                    else:
                        pass

        elif product == "boringbike":
            for i in range(len(self._subassemblies)):
                if self._subassemblies[i][0] == "SA05":

                    if self._subassemblies[i][1] >= num_order:
                        self._subassemblies[i][1] = self._subassemblies[i][1] - num_order
                    else:
                        n = num_order - self._subassemblies[i][1]
                        for k in range(len(self._parts)):
                            if self._parts[k][0] == "completewheel_a":
                                if self._parts[k][2] >= 2 * n:
                                    self._parts[k][2] = self._parts[k][2] - 2 * n
                                    self._subassemblies[i][1] = self._subassemblies[i][1] + n/2
                                else:
                                    m = 2 * n - self._parts[k][2]
                                    self.procurement(self._parts[k][0], m)
                            else:
                                pass
                        for j in range(len(self._subassemblies)):
                            if self._subassemblies[j][0] == "SA06":
                                if self._subassemblies[j][1] >= n:
                                    self._subassemblies[j][1] = self._subassemblies[j][1] - n
                                    self._subassemblies[i][1] = self._subassemblies[i][1] + n/2
                                else:
                                    m = n - self._subassemblies[j][1]
                                    for k in range(len(self._parts)):
                                        if self._parts[k][0] == "frame_a":
                                            if self._parts[k][2] >= m:
                                                self._parts[k][2] = self._parts[k][2] - m
                                                self._subassemblies[j][1] = self._subassemblies[j][1] + m/2
                                            else:
                                                l = m - self._parts[k][2]
                                                self.procurement(self._parts[k][0], l)
                                        elif self._parts[k][0] == "chain_b":
                                            if self._parts[k][2] >= m:
                                                self._parts[k][2] = self._parts[k][2] - m
                                                self._subassemblies[j][1] = self._subassemblies[j][1] + m/2
                                            else:
                                                l = m - self._parts[k][2]
                                                self.procurement(self._parts[k][0], l)
                                        else:
                                            pass
                                if self._subassemblies[j][1] >= n:
                                    self._subassemblies[j][1] = self._subassemblies[j][1] - n
                                    self._subassemblies[i][1] = self._subassemblies[i][1] + n/2
                                else:
                                    pass
                            else:
                                pass
                        return self.execute_order(product, num_order)
                elif self._subassemblies[i][0] == "SA04":
                    if self._subassemblies[4][1] == num_order:
                        self._subassemblies[4][1] = self._subassemblies[4][1] - num_order
                        break
                    else:
                        pass
                    if self._subassemblies[i][1] >= num_order:
                        self._subassemblies[i][1] = self._subassemblies[i][1] - num_order
                    else:
                        n = num_order - self._subassemblies[i][1]
                        for j in range(len(self._parts)):
                            if self._parts[j][0] == "handlebar_c":
                                if self._parts[j][2] >= n:
                                    self._parts[j][2] = self._parts[j][2] - n
                                    self._subassemblies[i][1] = self._subassemblies[i][1] + n/2
                                else:
                                    m = n - self._parts[j][2]
                                    self.procurement(self._parts[j][0], m)
                            elif self._parts[j][0] == "rubberhandle_a":
                                if self._parts[j][2] >= 2 * n:
                                    self._parts[j][2] = self._parts[j][2] - 2 * n
                                    self._subassemblies[i][1] = self._subassemblies[i][1] + n/2
                                else:
                                    m = 2 * n - self._parts[j][2]
                                    self.procurement(self._parts[j][0], m)
                            else:
                                pass
                        return self.execute_order(product, num_order)
                else:
                    pass
            if num_order > 5:
                n = int(num_order/3)
                for i in range(len(self._subassemblies)):
                    if self._subassemblies[i][0] == "SA04":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + n
                    elif self._subassemblies[i][0] == "SA05":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + n
                    elif self._subassemblies[i][0] == "SA06":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + n
                    else:
                        pass
            else:
                for i in range(len(self._subassemblies)):
                    if self._subassemblies[i][0] == "SA04":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + 1
                    elif self._subassemblies[i][0] == "SA05":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + 1
                    elif self._subassemblies[i][0] == "SA06":
                        self._subassemblies[i][1] = self._subassemblies[i][1] + 1
                    else:
                        pass
        else:
            product = input("{0} produce cool bike or boring bike.\n Please order again.: ")
            return self.execute_order(product, num_order)
        for i in range(len(self._parts)):
            self._parts[i][2] = round(self._parts[i][2])
            self._parts[i][3] = round(self._parts[i][3])
        for i in range(len(self._subassemblies)):
            self._subassemblies[i][1] = round(self._subassemblies[i][1])
        return print("{0} produce {1} {2}s successfully".format(self._company, num_order, product))


    def get_expense(self):
        return print("Total expense of {0} is ${1}".format(self._company, self.__expense))





if __name__ == '__main__':
    # code for your demo here
    c = MRP("UNICLE")
    c.storage_parts()
    c.storage_subassemblies()
    print(c._parts)
    print(c._subassemblies)
    print("{0} can produce {1} cool bikes.".format(c._company, c.calculate_and_verify("coolbike")))
    print("{0} can produce {1} boring bikes.".format(c._company, c.calculate_and_verify("boringbike")))
    c.calculate_and_verify("bike")
    c.get_expense()
    c.procurement("frame_a", 8)
    c.procurement("completewheel_a", 3)
    print(c._parts)
    c.get_expense()
    c.execute_order("coolbike", 11) # 2 SA01, 4 SA02, 6 SA03, 1 SA04 produced. So 2 frb, 2 cha, 8 tia, 8 wha, 1 hac, and 2 rha used
    print(c._parts)
    print(c._subassemblies)
    c.execute_order("boringbike", 4) # 4 SA05, 4 SA06, 1 SA04 produced. So, 8 cwa, 4 fra, 4 chb, 1 hac, and 2 rha used
    print(c._parts)
    print(c._subassemblies)
    c.get_expense()