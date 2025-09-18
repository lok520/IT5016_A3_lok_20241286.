# IT5016_A3_lok_20241286.

Requisition System 

1. Staff Information
The system begins by collecting essential details from the staff member. Users are prompted to provide the date, their staff ID, and name. This ensures every requisition is correctly linked to the person submitting it.

2. Item Requisition
Staff can record the items they want to request. For each item, the program asks for the name and the cost. The total cost is calculated automatically, allowing multiple items to be processed in a single requisition.

3. Approval Workflow
The program evaluates the total cost to determine the approval status. Requisitions under $500 are automatically approved. Those between $500 and $1000 are marked as pending and require manager approval. Requests exceeding $1000 are automatically not approved.

4. Manager Review
Pending requisitions can be reviewed by the manager, who can approve or reject the request. Approved requisitions receive a unique approval reference number for tracking purposes.

5. Requisition Summary
After processing, the program displays a clear summary that includes staff details, total cost, approval status, and the reference number. This ensures transparency and easy record-keeping.

6. Statistics Tracking
The system keeps track of all requisitions, showing the total number submitted, approved, pending, and rejected. This feature provides a quick overview of overall activity and helps in decision-making.

7. Educational Value
While practical, the program also serves as a demonstration of fundamental Python concepts, including classes, methods, loops, conditionals, and user input. It is beginner-friendly and provides a realistic example of how an office requisition workflow can be automated.
