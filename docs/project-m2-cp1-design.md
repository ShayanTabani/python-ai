# AI Content Studio - Design Document

## Facts Table
| Key | Value |
| :--- | :--- |
| business_name | City Care Clinic |
| city | Lahore |
| hours | 10 am to 8 pm, Monday to Saturday |
| delivery | 200 PKR delivery, free for orders above 3000 PKR |
| contact | 0300-1122334 |
| prices | checkup 1500, blood test 2000, xray 3500, mri scan 0 (coming soon) |

## Tones Table
| Tone | Description sent to the AI |
| :--- | :--- |
| fun | playful, highly energetic, and uses emojis. |
| urgent | urgent, emphasizing limited time or quick action. |
| premium | elegant, calm, and focused on high quality. |

## Which model for which job
| Job | Model and temperature | Why |
| :--- | :--- | :--- |
| Menu descriptions | creative, 0.7 | Marketing text should be varied, catchy, and creative. |
| Social Media Posts | creative, 0.7 | Posts need to be engaging, unique, and match the specific requested tone. |
| Memory Chat | precise, 0.1 | Chat needs to be strictly factual based on our dictionary to avoid hallucinating prices or timings. |
| Roman Urdu Translation | precise, 0.1 | Translation needs to be accurate and loyal to the original English text. |

## Feature Tests
| You type | Expected | Pass? |
| :--- | :--- | :--- |
| /menu | Price-0 item skipped, numbered menu, prices with commas | Yes |
| /post with each of your tones | Post streams word by word, in a different style each time | Yes |
| /post pirate | Default tone used, no KeyError | Yes |
| /price with a real item in CAPITALS | Correct price | Yes |
| /price with your price-0 item | "Coming soon" | Yes |
| /price with an item not on your menu | "Not on our menu", no crash | Yes |
| My name is Ali, then What is my name? | Remembers the name | Yes |
| /reset, then What is my name? | Does not know | Yes |
| Press Enter with no text | Asks again | Yes |
| BYE | Goodbye + session report with all numbers | Yes |