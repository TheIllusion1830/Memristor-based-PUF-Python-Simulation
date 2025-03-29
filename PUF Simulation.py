import numpy as np
import pandas as pd
import math
import time
import os


class Memristor:
    def __init__(self, params):
        self.ID = params['ID']
        self.row = params['row']
        self.col = params['col']
        self.a1 = params['a1']
        self.a2 = params['a2']
        self.b = params['b']
        self.xp = params['xp']
        self.xn = params['xn']
        self.Vn = params['Vn']
        self.Vp = params['Vp']
        self.eta = params['eta']
        self.x0 = params['x0']

    def update(self, V, dt):
        if V == "Low":
            print("Inverted Challenge Memristor ",self.ID," unchanged.")
            return 0
        dx = self.eta * (self.a1 * abs(V) + self.a2) * np.exp(-self.b * self.x0) * dt
        if self.x0 >= 0.5:
            if V >= self.Vp or V <= self.Vn:
                self.x0 = self.x0 - dx
                print("Updated State of Memristor ", self.ID, ": ", self.x0, "(HRS --> LRS)")
            else:
                print("Voltage does not pass Memristor ", self.ID, "s threshold: >", self.Vn, " <",self.Vp)

        else:
            if V >= self.Vp or V <= self.Vn:
                self.x0 = self.x0 + dx
                print("Updated State of Memristor ", self.ID, ": ", self.x0, "(LRS --> HRS)")

    def reset(self):
        if self.x0 < 0.5:
            self.update(1.8,timer[1]-timer[0])
            
    def get_resistance(self):
        if self.x0 >= 0.5:
            return 360
        else:
            return 40

class Yakopcic_Random():
    def __init__(self, input, **kwargs):
        self.type = "Yakopcic model"

        self.input = input
        self.V = input
        self.x0 = kwargs.get("x0", 0.1 + np.random.uniform(0.4,0.9))
        
        # Default parameters with slight random variations
        self.a1 = kwargs.get("a1", 1 + np.random.uniform(-0.01, 0.01))
        self.a2 = kwargs.get("a2", 1 + np.random.uniform(-0.01, 0.01))
        self.b = kwargs.get("b", 0.05 + np.random.uniform(-0.01, 0.01))
        self.Ap = kwargs.get("Ap", 4000 + np.random.randint(-100, 100))
        self.An = kwargs.get("An", 4000 + np.random.randint(-100, 100))
        self.Vp = kwargs.get("Vp", 1.8 + np.random.uniform(-0.01, 0.01))
        self.Vn = kwargs.get("Vn", -1.8 + np.random.uniform(-0.01, 0.01))
        self.alphap = kwargs.get("alphap", 1 + np.random.uniform(-0.1, 0.1))
        self.alphan = kwargs.get("alphan", 5 + np.random.uniform(-0.1, 0.1))
        self.xp = kwargs.get("xp", 0.3 + np.random.uniform(-0.05, 0.05))
        self.xn = kwargs.get("xn", 0.5 + np.random.uniform(-0.05, 0.05))
        self.eta = kwargs.get("eta", 1 + np.random.uniform(-0.1, 0.1))

        self.passed_parameters = kwargs
        self.passed_parameters.pop("x0", None)


def generate_and_save_memristors(file_type):
    """
    Generates 'num_memristors' instances of the Yakopcic memristor model,
    stores their parameters in a CSV or Excel file, and saves the file.

    Parameters:
    - num_memristors: The number of memristors to generate (default is 50).
    - file_type: The type of file to save ('csv' or 'excel').

    Returns:
    - None
    """
    
    k = True
    while(k):
        res = int(input("Enter number of responses: "))
        if not(math.log2(res).is_integer()):
            print("Number of responses must be a power of 2.")
            continue
        cha = int(input("Enter number of challenges: "))
        if not(math.log2(cha).is_integer()):
            print("Number of challenges must be a power of 2.")
            continue
        elif res > cha:
            print("Number of challenges must be greater or equal to number of responses.")       
            continue
        k = False

    num = res * cha
    row = cha*2
    col = res*2
    # Initialize list to store memristor parameters
    memristor_data = []
    k=0
    # Create 'num_memristors' memristors and collect their parameters
    for i in range(row):
        for j in range(col):

            memristor = Yakopcic_Random(input=None)  # You can modify initialization as needed

            # Extracting memristor parameters (assuming they exist in the memristor object)
            memristor_params = {
                'Memristor_ID': k+1,
                'Mem_Row' : int(i*((1/row)+1)+1),
                'Mem_Col' : int(j+1),
                'a1': memristor.a1,
                'a2': memristor.a2,
                'b': memristor.b,
                'xp': memristor.xp,
                'xn': memristor.xn,
                'Vn': memristor.Vn,
                'Vp': memristor.Vp,
                'alphap': memristor.alphap,
                'alphan': memristor.alphan,
                'eta': memristor.eta,
                'x0': memristor.x0  # Assuming x0 is a parameter
            }
            k+=1
            memristor_data.append(memristor_params)
            

    # Create a DataFrame from the list of memristor parameters
    df = pd.DataFrame(memristor_data)

    # Save the DataFrame to a CSV or Excel file
    if file_type == 'csv':
        df.to_csv('memristor_parameters.csv', index=False)
    elif file_type == 'excel':
        df.to_excel('memristor_parameters.xlsx', index=False)
    else:
        raise ValueError("Unsupported file type. Choose either 'csv' or 'excel'.")

    print("Array of {} X {} Memristors created inputing {} challenges and outputting {} responses\n".format(row,col,cha,res))


def write():
    k = 0
    n = True
    while(n == True):
        cr = input("Enter Challenge Input: ")
        if all(c in "01" for c in cr) and len(cr) == row/2:
            n = False
        else:
            print("Input is either larger than length of challenge input or is not in binary format")
            print("Length of challenge input = " , int(row/2))
    for i in range(int(row/2)):
        cn = "Low"
        print("Memristors Driven by C{}(Value = {}):\n".format(i,int(cr[i])))
        for j in range(col):
            c = int(cr[i])
            mem = Memristor(memristors[k])
            if c==0:
                cn = 1.8
                print("True Challenge Memristor ",mem.ID," unchanged (Voltage not above threshold)")
                k+=1
            else:
                mem.update(1.8,timer[1] - timer[0])
                memristors[k]["x0"] = mem.x0
                k+=1

        print("\n")
        print("Memristors Driven by -C{}(Value = {}):\n".format(i,not(int(cr[i]))))
        for j in range(col):
            mem = Memristor(memristors[k])
            mem.update(cn,timer[1] - timer[0])
            memristors[k]["x0"] = mem.x0
            k+=1
        print("\n")

def thresh(ResNo):
    R1 = []
    R2 = []
    R1f = 0
    R2f = 0
    for i in range(2*ResNo,row*col,col):
        mem = Memristor(memristors[i])
        R1.append(mem.get_resistance())

    for i in range(2*ResNo+1,row*col,col):
        mem = Memristor(memristors[i])
        R2.append(mem.get_resistance())


    for i in range(row):
        R1f += 1/R1[i]
    R1f = 1/R1f
    print("Total Resistance of Coloumn 1 for Response Bit {}: ".format(ResNo+1),R1f)


    for i in range(row):
        R2f += 1/R2[i]
    R2f = 1/R2f
    print("Total Resistance of Coloumn 2 for Response Bit {}: ".format(ResNo+1),R1f)

    if R2f > R1f:
        return 0
    else:
        return 1

def read():
    Vrd = 0.9       #Read Voltage
    Vbt = 0.5       #Voltage Threshold for Buffer
    HRS = 400      #High State Resistance
    LRS = 40        #Low State Resistance
    Rld = HRS/(row*2)   #Load Resistance
    Responses = []
    for i in range(int(col/2)):
        Responses.append(thresh(i))

    print("Response Bits are: ", Responses)

def reset():
    for i in range(row*col):
        mem = Memristor(memristors[i])
        mem.reset()
        memristors[i]["x0"] = mem.x0
    print("\nAll Memristors reset to HRS.\n")


def read_file():
    global memristors,row,col
    file_path = 'memristor_parameters.xlsx'
    if not os.path.exists(file_path):
        generate_and_save_memristors('excel')
    data = pd.read_excel(file_path)
    memristors = []
    for i, row in data.iterrows():
        memristors.append({
            'ID':row['Memristor_ID'],'row':row['Mem_Row'],'col':row['Mem_Col'], 'a1': row['a1'], 'a2': row['a2'], 'b': row['b'], 'xp': row['xp'], 'xn': row['xn'],
            'Vn': row['Vn'], 'Vp': row['Vp'], 'alphap': row['alphap'], 'alphan': row['alphan'],
            'eta': row['eta'], 'x0': row['x0']
        })

    row = data['Mem_Row'].max()
    col = data['Mem_Col'].max()  

def write_file(file_type):

    memristor_data = []
    for i in memristors:
        memristor_params = {
        'Memristor_ID': i.get("ID"),
        'Mem_Row' : i.get("row"),
        'Mem_Col' : i.get("col"),
        'a1': i.get("a1"),
        'a2': i.get("a2"),
        'b': i.get("b"),
        'xp': i.get("xp"),
        'xn': i.get("xn"),
        'Vn': i.get("Vn"),
        'Vp': i.get("Vp"),
        'alphap': i.get("alphap"),
        'alphan': i.get("alphan"),
        'eta': i.get("eta"),
        'x0': i.get("x0")  # Assuming x0 is a parameter
    }
        memristor_data.append(memristor_params)
            

    # Create a DataFrame from the list of memristor parameters
    df = pd.DataFrame(memristor_data)

    # Save the DataFrame to a CSV or Excel file
    if file_type == 'csv':
        df.to_csv('memristor_parameters.csv', index=False)
    elif file_type == 'excel':
        df.to_excel('memristor_parameters.xlsx', index=False)
    else:
        raise ValueError("Unsupported file type. Choose either 'csv' or 'excel'.")



timer = np.linspace(0, 1, 6)


read_file()
g = 1
while g == 1:
    print("Enter Choice......")
    print("1. Write Mode")
    print("2. Read Mode")
    print("3. Reset")
    print("4. Create New Array")
    print("5. Exit..")
    opt = int(input("Choose Mode: "))

    if opt == 1:
        write()
        write_file('excel')
    elif opt == 2:
        read_file()
        read()
    elif opt == 3:
        reset()
        write_file('excel')
        read_file()
    elif opt == 4:
        generate_and_save_memristors('excel')
        read_file()
    elif opt == 5:
        g += 1
    else:
        print("Enter Valid Choice.......")






