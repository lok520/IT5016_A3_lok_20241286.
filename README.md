# IT5016_A3_lok_20241286.

Requisition System Overview.


The Requisition System is meant to automate and simplify the process of ordering office supplies or resources as well as being a realistic demonstration of the Python programming principles. It is highly structured and is based on the KISS (Keep It Simple, Stupid) principle, with its design being more simple, clear, and modular. This principle promotes that each component of the system fulfills one, clear-cut task without any redundant complexity that is simple to comprehend, maintain and have extensions.

Staff Information.
The system will start by collecting the necessary information concerning the staff member who will start the requisition. This will involve the date of request, staff ID and staff name. Since this step (gathering staff information) is kept to the bare minimum of gathering information, the program is in compliance with the Single Responsibility Principle and the KISS principle is followed by not binding this task with any other logic. Obtaining this information is important in order to make sure that every requisition is well linked with the person requesting, which is essential in accountability and record-keeping.

Item Requisition.
Once staff information is received, the employees are allowed to write down the things they would desire. The program requests the name and the cost of each item and enables one to add several items to one requisition. The overall cost is automatically determined. The system is simple and easy to follow as entry and cost calculation has been isolated into one method, which is also an example of KISS. Input validation is also provided so as to have the right data entry without having to complicate the logic. The modular system allows it to be easy to add or change features of entering items in the future.
Approval Workflow.
The system considers the overall cost of the requisition to ascertain whether it will be approved or not. Any request below 500 would be automatically approved, requests between 500 to 1000 would be tagged as pending to be reviewed by management and above 1000 would automatically be rejected. This approach is a threshold-based approach which is easy and clear and sees the principle of KISS in action. The system does not overcomplicate the logic of decision making by keeping the automatic approval and pending approval separate.

Manager Review.
The manager reviews pending requisitions and approves or rejects them. The approval of requisitions is given a special reference number to help it be tracked. The program is modular and simple to follow because of this separation of this managerial review and automatic approval and is another example of KISS in action.

Requisition Summary.
The program produces an understandable summary of the requisition, such as the staff information, the final cost, the condition, and the reference numbers. This approach is simple and may be easily read, which is KISS. The summary is also transparent and helps in keeping records.

Statistics Tracking.
System also provides overall statistics, i.e. total requisitions, approved, pending and rejected requests. This option enables one to in a glance scan through office activity, which is useful in making a decision and the logic is easy.
Educational Value.
Besides serving a functional role, the program illustrates such technical concepts in Python as classes, methods, loops, conditionals, and input processing. It is designed in a KISS way and all the functions are devoted to one task, which made the program an excellent learning tool.

All in all, the Requisition System is both practical and yet simple and yet it shows that office processes in real-life can be effectively automated with the code being understandable, modular, and readable.
