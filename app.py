import streamlit as st
import joblib
import pandas as pd

# ── Load Model ───────────────────────────────────────────────
model = joblib.load('loan_model.pkl')

# ── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title='Loan Approval Prediction',
    page_icon='🏦',
    layout='centered'
)

st.title('🏦 Loan Approval Prediction')
st.divider()
st.markdown('Fill in the applicant details below to predict loan approval.')

# ── Input Form ───────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    Age                       = st.number_input('Age',                          min_value=18,    max_value=100,    value=35)
    AnnualIncome              = st.number_input('Annual Income ($)',             min_value=0,     max_value=500000, value=60000,  step=1000)
    CreditScore               = st.number_input('Credit Score',                 min_value=300,   max_value=850,    value=650)
    Experience                = st.number_input('Experience (years)',            min_value=0,     max_value=50,     value=5)
    LoanAmount                = st.number_input('Loan Amount ($)',               min_value=1000,  max_value=500000, value=20000, step=500)
    LoanDuration              = st.number_input('Loan Duration (months)',        min_value=6,     max_value=360,    value=60)
    NumberOfDependents        = st.number_input('Number of Dependents',         min_value=0,     max_value=10,     value=0)
    MonthlyDebtPayments       = st.number_input('Monthly Debt Payments ($)',    min_value=0,     max_value=50000,  value=500,   step=50)
    CreditCardUtilizationRate = st.number_input('Credit Card Utilization Rate', min_value=0.0,   max_value=1.0,    value=0.3,   step=0.01)
    NumberOfOpenCreditLines   = st.number_input('Number of Open Credit Lines',  min_value=0,     max_value=20,     value=3)
    NumberOfCreditInquiries   = st.number_input('Number of Credit Inquiries',   min_value=0,     max_value=20,     value=1)
    DebtToIncomeRatio         = st.number_input('Debt-to-Income Ratio',         min_value=0.0,   max_value=1.0,    value=0.3,   step=0.01)
    TotalDebtToIncomeRatio    = st.number_input('Total Debt-to-Income Ratio',   min_value=0.0,   max_value=1.0,    value=0.4,   step=0.01)
    NetWorth                  = st.number_input('Net Worth ($)',                 min_value=-500000, max_value=5000000, value=50000, step=1000)
    JobTenure                 = st.number_input('Job Tenure (years)',            min_value=0,     max_value=50,     value=3)

with col2:
    EmploymentStatus          = st.selectbox('Employment Status',    ['Employed', 'Self-Employed', 'Unemployed', 'Retired'])
    EducationLevel            = st.selectbox('Education Level',      ['High School', 'Associate', 'Bachelor', 'Master', 'Doctorate'])
    MaritalStatus             = st.selectbox('Marital Status',       ['Single', 'Married', 'Divorced', 'Widowed'])
    HomeOwnershipStatus       = st.selectbox('Home Ownership',       ['Own', 'Mortgage', 'Rent'])
    LoanPurpose               = st.selectbox('Loan Purpose',         ['Home', 'Auto', 'Education', 'Personal', 'Business', 'Debt Consolidation'])
    PaymentHistory            = st.number_input('Payment History Score',         min_value=0,   max_value=100,    value=80)
    LengthOfCreditHistory     = st.number_input('Length of Credit History (yrs)',min_value=0,   max_value=50,     value=5)
    SavingsAccountBalance     = st.number_input('Savings Account Balance ($)',   min_value=0,   max_value=500000, value=10000, step=500)
    CheckingAccountBalance    = st.number_input('Checking Account Balance ($)',  min_value=0,   max_value=500000, value=5000,  step=500)
    TotalAssets               = st.number_input('Total Assets ($)',              min_value=0,   max_value=5000000,value=100000,step=1000)
    TotalLiabilities          = st.number_input('Total Liabilities ($)',         min_value=0,   max_value=5000000,value=30000, step=1000)
    MonthlyIncome             = st.number_input('Monthly Income ($)',            min_value=0,   max_value=100000, value=5000,  step=100)
    UtilityBillsPaymentHistory= st.number_input('Utility Bills Payment History',min_value=0.0, max_value=1.0,    value=0.9,   step=0.01)
    BankruptcyHistory         = st.selectbox('Bankruptcy History',   ['No (0)', 'Yes (1)'])
    PreviousLoanDefaults      = st.number_input('Previous Loan Defaults',        min_value=0,   max_value=10,     value=0)

# ── Predict Button ───────────────────────────────────────────
st.divider()
if st.button('🔍 Predict Loan Approval', use_container_width=True):

    input_data = pd.DataFrame([{
        'Age'                       : Age,
        'AnnualIncome'              : AnnualIncome,
        'CreditScore'               : CreditScore,
        'EmploymentStatus'          : EmploymentStatus,
        'EducationLevel'            : EducationLevel,
        'Experience'                : Experience,
        'LoanAmount'                : LoanAmount,
        'LoanDuration'              : LoanDuration,
        'MaritalStatus'             : MaritalStatus,
        'NumberOfDependents'        : NumberOfDependents,
        'HomeOwnershipStatus'       : HomeOwnershipStatus,
        'MonthlyDebtPayments'       : MonthlyDebtPayments,
        'CreditCardUtilizationRate' : CreditCardUtilizationRate,
        'NumberOfOpenCreditLines'   : NumberOfOpenCreditLines,
        'NumberOfCreditInquiries'   : NumberOfCreditInquiries,
        'DebtToIncomeRatio'         : DebtToIncomeRatio,
        'BankruptcyHistory'         : 1 if BankruptcyHistory == 'Yes (1)' else 0,
        'LoanPurpose'               : LoanPurpose,
        'PreviousLoanDefaults'      : PreviousLoanDefaults,
        'PaymentHistory'            : PaymentHistory,
        'LengthOfCreditHistory'     : LengthOfCreditHistory,
        'SavingsAccountBalance'     : SavingsAccountBalance,
        'CheckingAccountBalance'    : CheckingAccountBalance,
        'TotalAssets'               : TotalAssets,
        'TotalLiabilities'          : TotalLiabilities,
        'MonthlyIncome'             : MonthlyIncome,
        'UtilityBillsPaymentHistory': UtilityBillsPaymentHistory,
        'JobTenure'                 : JobTenure,
        'NetWorth'                  : NetWorth,
        'TotalDebtToIncomeRatio'    : TotalDebtToIncomeRatio,
    }])

    prediction  = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.divider()
    if prediction == 1:
        st.success('✅ Loan APPROVED')
        st.metric('Approval Probability', f'{probability[1]*100:.1f}%')
    else:
        st.error('❌ Loan REJECTED')
        st.metric('Rejection Probability', f'{probability[0]*100:.1f}%')

    col_a, col_b = st.columns(2)
    col_a.metric('Approved', f'{probability[1]*100:.1f}%')
    col_b.metric('Rejected', f'{probability[0]*100:.1f}%')
    st.progress(float(probability[1]))