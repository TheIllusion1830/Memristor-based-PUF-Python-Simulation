**Description:**

This project models an infinitely scalable memristor crossbar array in Python to simulate challenge-response behavior in Physical Unclonable Functions (PUFs). The user can specify the size of the crossbar by choosing the number of challenge and response bits (according to given constraints). The system generates unique responses for the same challenge across different memristor arrays due to inherent physical variations. However, within the same simulation, the same challenge input always produces the same response output. This behavior is useful in security applications such as generating unique cryptographic keys.


**Features:**

-Create Crossbar Array: Allows users to define the size of the memristor crossbar array using number of Challenge bits and Response bits.

-Write Mode: Users input challenge bit strings, influencing memristor states.

-Read Mode: Returns the response bit string based on the challenge input and the memristor crossbar configuration.

-Reset Mode: Resets all memristors to their High Resistance State (HRS), allowing for a fresh start while maintaining the same memristors.

-Exit: Terminates the simulation.


**Usage:**

-Run the program using: python PUF-Simulation.py

-Users will be prompted to enter the number of challenge and response bits, ensuring they meet the power-of-2 constraint. They can then input challenge bit strings using the Write mode and retrieve corresponding response bit strings with the Read mode. If needed, the Reset mode restores all memristors to HRS before running new simulations.



**Example Output:**

Enter number of responses: _4_

Enter number of challenges: _4_

Enter Choice......

1. Write Mode
2. Read Mode
3. Reset
4. Create New Array
5. Exit..

Choose Conversion: _1_

Enter Challenge Input: _1010_

Memristors Driven by C0(Value = 1):

Updated State of Memristor  1.0 :  0.34388551981814797 (HRS --> LRS)

Voltage does not pass Memristor  2.0 s threshold: > -1.802453097683689  < 1.805775297448798

Voltage does not pass Memristor  3.0 s threshold: > -1.795828044066066  < 1.802869773965156

Voltage does not pass Memristor  4.0 s threshold: > -1.80379304541303  < 1.806200050651933

Updated State of Memristor  5.0 :  0.38949369284835267 (HRS --> LRS)

Updated State of Memristor  6.0 :  0.0663387551436958 (HRS --> LRS)

Voltage does not pass Memristor  7.0 s threshold: > -1.8055884370676  < 1.805536288938775

Updated State of Memristor  8.0 :  0.061713846746373924 (HRS --> LRS)



Memristors Driven by -C0(Value = False):


Inverted Challenge Memristor  9.0  unchanged.

Inverted Challenge Memristor  10.0  unchanged.

Inverted Challenge Memristor  11.0  unchanged.

Inverted Challenge Memristor  12.0  unchanged.

Inverted Challenge Memristor  13.0  unchanged.

Inverted Challenge Memristor  14.0  unchanged.

Inverted Challenge Memristor  15.0  unchanged.

Inverted Challenge Memristor  16.0  unchanged.



Memristors Driven by C1(Value = 0):


True Challenge Memristor  17.0  unchanged (Voltage not above threshold)

True Challenge Memristor  18.0  unchanged (Voltage not above threshold)

True Challenge Memristor  19.0  unchanged (Voltage not above threshold)

True Challenge Memristor  20.0  unchanged (Voltage not above threshold)

True Challenge Memristor  21.0  unchanged (Voltage not above threshold)

True Challenge Memristor  22.0  unchanged (Voltage not above threshold)

True Challenge Memristor  23.0  unchanged (Voltage not above threshold)

True Challenge Memristor  24.0  unchanged (Voltage not above threshold)



Memristors Driven by -C1(Value = True):


Voltage does not pass Memristor  25.0 s threshold: > -1.800244513981869  < 1.806260112008126

Updated State of Memristor  26.0 :  0.16548770106875355 (HRS --> LRS)

Voltage does not pass Memristor  27.0 s threshold: > -1.797320330862527  < 1.80498909819651

Voltage does not pass Memristor  28.0 s threshold: > -1.796604234793125  < 1.809005774955367

Voltage does not pass Memristor  29.0 s threshold: > -1.805785454892186  < 1.803847385654892

Voltage does not pass Memristor  30.0 s threshold: > -1.809578542334906  < 1.802498220776585

Voltage does not pass Memristor  31.0 s threshold: > -1.806446616379512  < 1.80959640088421

Updated State of Memristor  32.0 :  0.1250028307992299 (HRS --> LRS)



Memristors Driven by C2(Value = 1):


Voltage does not pass Memristor  33.0 s threshold: > -1.80317723282061  < 1.808995418163403

Updated State of Memristor  34.0 :  -0.03865080231515694 (HRS --> LRS)

Updated State of Memristor  35.0 :  0.08624273377865244 (HRS --> LRS)

Voltage does not pass Memristor  36.0 s threshold: > -1.796518553977105  < 1.80527402519885

Updated State of Memristor  37.0 :  0.22803115582071765 (HRS --> LRS)

Voltage does not pass Memristor  38.0 s threshold: > -1.790499625036719  < 1.805132316032017

Voltage does not pass Memristor  39.0 s threshold: > -1.797441156961521  < 1.807769737221068

Voltage does not pass Memristor  40.0 s threshold: > -1.808251308307077  < 1.808085632951377



Memristors Driven by -C2(Value = False):


Inverted Challenge Memristor  41.0  unchanged.

Inverted Challenge Memristor  42.0  unchanged.

Inverted Challenge Memristor  43.0  unchanged.

Inverted Challenge Memristor  44.0  unchanged.

Inverted Challenge Memristor  45.0  unchanged.

Inverted Challenge Memristor  46.0  unchanged.

Inverted Challenge Memristor  47.0  unchanged.

Inverted Challenge Memristor  48.0  unchanged.



Memristors Driven by C3(Value = 0):


True Challenge Memristor  49.0  unchanged (Voltage not above threshold)

True Challenge Memristor  50.0  unchanged (Voltage not above threshold)

True Challenge Memristor  51.0  unchanged (Voltage not above threshold)

True Challenge Memristor  52.0  unchanged (Voltage not above threshold)

True Challenge Memristor  53.0  unchanged (Voltage not above threshold)

True Challenge Memristor  54.0  unchanged (Voltage not above threshold)

True Challenge Memristor  55.0  unchanged (Voltage not above threshold)

True Challenge Memristor  56.0  unchanged (Voltage not above threshold)



Memristors Driven by -C3(Value = True):


Voltage does not pass Memristor  57.0 s threshold: > -1.791471144347307  < 1.803613949936717

Voltage does not pass Memristor  58.0 s threshold: > -1.795550159645437  < 1.80539011351905

Updated State of Memristor  59.0 :  0.018198332029040754 (HRS --> LRS)

Voltage does not pass Memristor  60.0 s threshold: > -1.796224532798904  < 1.804983761063777

Voltage does not pass Memristor  61.0 s threshold: > -1.792019095506138  < 1.80464206033555

Updated State of Memristor  62.0 :  0.2571201712010829 (HRS --> LRS)

Voltage does not pass Memristor  63.0 s threshold: > -1.79930162806858  < 1.804174623215907

Updated State of Memristor  64.0 :  0.016284660015840613 (HRS --> LRS)



Enter Choice......

1. Write Mode
2. Read Mode
3. Reset
4. Create New Array
5. Exit..

Choose Conversion: _2_

22.500000000000007

15.0

15.0

45.0

15.0

15.000000000000004

45.0

11.250000000000002

Response Bits are:  [1, 0, 0, 1]

Enter Choice......

1. Write Mode
2. Read Mode
3. Reset
4. Create New Array
5. Exit..

Choose Conversion: _3_

Updated State of Memristor  1.0 :  0.8916653043521929 (LRS --> HRS)

Updated State of Memristor  5.0 :  0.9909312054663653 (LRS --> HRS)

Updated State of Memristor  6.0 :  0.6454024867065369 (LRS --> HRS)

Updated State of Memristor  8.0 :  0.6346360569574965 (LRS --> HRS)

Updated State of Memristor  26.0 :  0.6654769363507362 (LRS --> HRS)

Updated State of Memristor  32.0 :  0.6480698675135559 (LRS --> HRS)

Updated State of Memristor  34.0 :  0.5176220198922505 (LRS --> HRS)

Updated State of Memristor  35.0 :  0.6816256256434188 (LRS --> HRS)

Updated State of Memristor  37.0 :  0.7750791229876659 (LRS --> HRS)

Updated State of Memristor  59.0 :  0.5630890802909024 (LRS --> HRS)

Updated State of Memristor  62.0 :  0.7888787127888183 (LRS --> HRS)

Updated State of Memristor  64.0 :  0.6037680357308755 (LRS --> HRS)

Enter Choice......

1. Write Mode
2. Read Mode
3. Reset
4. Create New Array
5. Exit..

Choose Conversion: _2_

45.0

45.0

45.0

45.0

45.0

45.0

45.0

45.0

Response Bits are:  [1, 1, 1, 1]

Enter Choice......

1. Write Mode
2. Read Mode
3. Reset
4. Create New Array
5. Exit..
   
Choose Conversion: _5_
