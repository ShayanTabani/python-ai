# Front Desk Design: City Care Clinic

### 1. Intents
| Intent | Keywords | Reply |
| :--- | :--- | :--- |
| Complaint / Urgent | complaint, late, refund | Sorry about that. A manager will call you within 1 hour. |
| Timings | hours, timing, open, close | We are open 9 am to 10 pm, every day. |
| Location | location, address, where | We are located at Main Boulevard, Lahore. |
| Fees | fee, consultation, price | Basic consultation is 1,500 PKR. |
| Greeting | hi, hello, hey | Hello! How can I help you today? |

### 2. Business Rules
| Rule | Value |
| :--- | :--- |
| Item Prices | checkup = 1500, blood_test = 2000, xray = 3500 |
| Bulk Discount | 10% off if quantity is 3 or more |
| Delivery / Home Visit Fee | 500 PKR, free if total is above 5000 PKR |
| Private Words | phone, cnic, address |

### 3. Rule Tests
| You type | Expected | Pass? |
| :--- | :--- | :--- |
| WHAT are your hours | Hours (capitals and spaces handled) | Yes |
| which cake is best? | Fallback, not a greeting | Yes |
| my order is late | Manager reply (complaint rule first) | Yes |
| /quote, 1 checkup | Delivery/Visit fee charged | Yes |
| /quote, 4 xrays | Delivery free (above limit) | Yes |
| /quote, 3 blood_tests | Discount applied (10%) | Yes |
| /quote, pizza | "Not on our menu", no crash | Yes |
| my phone is 03001234567 | Routed to local model, cost 0 | Yes |
| (Press Enter) | Asks again | Yes |
| BYE | Goodbye + session report | Yes |