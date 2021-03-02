# Theater-Seating

Overview:
Design and write a seat assignment program to maximize both customer satisfaction and customer safety. For the purpose of public safety, assume that a buffer of three seats and/or one row is required.

Possible solution 1: Taking all the inputs based on the number of seats requrest and spacing customers out the max to prioritize safety. However, this wouldn't be practical since customers are given their seats as they purchase their tickets.

Possible solution 2: Prioritizing seating so customers in close rows don't sit in the same column; having someone taller sit in front of you can be super annoying. However, since a minimum of one row is required between customers, this most likely won't be an issue.

Possible solution 3: After taking all the possible solutions into account, this one seemd the most practical. Since customers require a spacing of one row, every other row was eliminated and will not be used. Starting with the most optimal row and ending with the least optimal (D, F, H, J, B), customers will be placed on the left hand side of the row. Once every row has at least one customer on the left hand side, the customers will then be placed on the right hand side of each row. Once each row has at least one customer on the right hand side, the customers will continue being placed on the right hand side with a minimum of three seats between each group. If all available seating is filled, no more customers will be able to reserve seats. This solution helps to prioritize safety and satisfaction of the customer.

A file containing one line of input for each reservation request is used. The order of the lines in the file reflects the order in which the reservationp requests were received. Each line in the fill will be comprised of a reservation identifier, followed by a space, and then the number of seats requested. By using this input file when we run the theater.py file, the program will output a file containing the seating assignemnt for each request. 
