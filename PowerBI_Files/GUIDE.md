# Hum Power BI kyun use kar rahe hain?

Suppose kisi ne poocha:     Mohali me average rent kitna hai?

* Python me:
    -- Code run karo
    -- Graph banao

* Power BI me:
    --Dashboard kholo
    -- Mohali select karo
    -- Answer instantly mil jayega.

Isi liye Power BI use karte hain.

### Views in PowerBI
* # Report View
    -- Yahi dashboard banta hai.
Yahi hum charts, KPIs aur slicers add karenge.

* # Data View
    -- Ye Excel jaisa dikhta hai.

Isme sirf check karte hain:
    Data sahi import hua?
    Columns sahi hain?
    Datatypes sahi hain?

* # Model View
    -- Ye tab kaam aata hai jab multiple tables hoti hain.
Abhi hamare paas sirf 1 table hai.
Isliye isko abhi ignore kar sakte hain.


---------------------------------------------------------


# What is Power Query?
"in short data cleaning krna in PowerBI"
CSV
   │
   ▼
Power Query
   │
   ▼
Power BI

Power Query can:

*   Rename columns
*   Remove duplicates
*   Change data types
*   Split columns
*   Filter rows
*   Merge datasets

We have already done all of this in Pandas.

So why does Power Query exist?
Because many analysts receive raw Excel or CSV files directly and clean them inside Power BI instead of Python.
