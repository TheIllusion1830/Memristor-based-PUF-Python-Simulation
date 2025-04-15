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

Initalization of Memristor Array:


![image](https://github.com/user-attachments/assets/9769ff0d-a68d-423a-96ee-094b585d27da)

Menu Driven Choices:

![image](https://github.com/user-attachments/assets/c3f98dc8-609b-42e2-92e0-1c961b986b58)

Initial Read of current array(Will always default to only 1s as the response bit):

![image](https://github.com/user-attachments/assets/cabd1c0d-dbf6-42f3-9660-8c927b88c58d)

Write Mode with sample Challenge Bit:

![image](https://github.com/user-attachments/assets/01f8ac7c-cc95-4a57-8ea9-e4f54b2639cd)

![image](https://github.com/user-attachments/assets/284b7210-a331-4010-9c23-f034ed1c4f00)

![image](https://github.com/user-attachments/assets/8ae7a086-f256-4daf-acc7-790736f945f4)

Read After Writing with inputted Challenge Bit:

![image](https://github.com/user-attachments/assets/b38fc046-4ea4-45fc-9cc9-be3dc6d1e53f)

Resetting Array of Memristors to HRS:

![image](https://github.com/user-attachments/assets/a61e2309-c68a-48cd-bab6-d17559187454)

After Resetting, Writing with the same Challenge Bit and then Reading:

![image](https://github.com/user-attachments/assets/d87c6125-8016-4b17-9c0c-bf73e2f7bd26)

![image](https://github.com/user-attachments/assets/c901bed5-d8a4-4cb2-b8d1-2f8c6cc7c384)

![image](https://github.com/user-attachments/assets/d2274d5b-87dc-40ba-aebe-6b774c033a53)

The same Response Bit is observed. This will always hold true for this array and a different Challenge-Response Pair will be observed for a new array.



