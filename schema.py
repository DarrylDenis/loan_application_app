import pandera as pa
from pandera import Column, DataFrameSchema,Check


schema = DataFrameSchema(
    {
        "loan_amnt": Column(float,Check(lambda x: x>0), nullable=False),
        "term":Column(str,Check(lambda x: x in ['36 months', '60 months']), nullable=False),
        "int_rate": Column(int, Check(lambda x:x>0),nullable=False),
        "installment": Column(float, Check(lambda x:x>0),nullable= False),
        "grade":Column(str,nullable=False),
        "sub-grade": Column(str,nullable=False),
        "emp_title": Column(str,nullable=True),
        "emp_length": Column(str,nullable = True),
        "home_ownership": Column(str,Check(lambda x: x in ["MORTGAGE", "RENT", "OWN", "OTHER","ANY","NONE"]) ,nullable=False),
        "annual_inc": Column(float, Check(lambda x:x>0), nullable=False),
        "verification_status": Column(str, nullable=False),
        "issue_d": Column(str, nullable=False),
        "loan_status": Column(str,Check(lambda x: x in ["Fully Paid", "Charged Off"]),nullable=False),
        "purpose": Column(str, nullable=False),
        "title": Column(str, nullable=True),
        "dti": Column(float, Check(lambda x:x>=0), nullable=False),
        "earliest_cr_line": Column(str, nullable=False),
        "open_acc": Column(float, Check(lambda x:x>=0), nullable=False),
        "pub_rec": Column(float, Check(lambda x:x>=0), nullable=False),
        "revol_bal": Column(float, Check(lambda x:x>=0), nullable=False),
        "revol_util": Column(float, Check(lambda x: 0<=x<=100), nullable=True),
        "total_acc": Column(float, Check(lambda x:x>=0), nullable=False),
        "initial_list_status": Column(str, nullable=False),
        "application_type": Column(str, nullable=False),
        "mort_acc": Column(float, Check(lambda x:x>=0), nullable=True),
        "pub_rec_bankruptcies": Column(float, Check(lambda x:x>=0), nullable=True),
        "address": Column(str, nullable=False)
                    
})

  